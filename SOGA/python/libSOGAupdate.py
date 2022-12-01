# Contains the functions for computing the resulting distribution when an assignment instruction is encountered (in state nodes).

# SOGA (defined in SOGA.py)
# |- update_rule
#    |- sym_expr
#    |- update_gaussian

from libSOGAshared import *
from ASGMTListener import *
from ASGMTParser import * 
from ASGMTLexer import *

class AsgmtRule(ASGMTListener):
    
    def __init__(self, var_list):
        self.var_list = var_list
        self.func = None           # stores the function
        self.target = None         # stores the index of the target variable
        
        self.aux_pis = []          # stores the weights of auxiliary variables
        self.aux_means = []        # stores the means of auxiliary variables
        self.aux_covs = []         # stores the cov matrices of auxiliary variables
        
    def enterAssignment(self, ctx):
        self.target = self.var_list.index(ctx.symvars().getText())
        
    def enterConst(self, ctx):
        c = float(eval(ctx.getText()))
        
        def const_func(comp):
            i = self.target
            new_mu = deepcopy(comp.gm.mu[0])
            new_sigma = deepcopy(comp.gm.sigma[0])
            new_mu[i] = c
            for k in range(len(new_mu)):
                new_sigma[i,k] = new_sigma[k,i] = 0
            return GaussianMix(comp.gm.pi, [new_mu], [new_sigma])
        
        self.func = const_func
       
    def enterAdd(self, ctx):
                
        self.add_coeff = [0.]*len(self.var_list)
        self.add_const = 0
        self.flag_sign = 1.
            
    def exitAdd(self, ctx):
        
                       
        def add_func(comp):
            i = self.target
            mu = comp.gm.mu[0]
            sigma = comp.gm.sigma[0]
            final_pi = []
            final_mu = []
            final_sigma = []
            for part in product(*[range(len(mean)) for mean in self.aux_means]):
                # STEP 1: for a given combination of components of the auxiliary variables, creates a new component extending comp
                aux_pi = 1
                aux_mean = list(deepcopy(mu))
                aux_sigma = []
                for p,q in zip(range(len(self.aux_means)), part):
                    aux_pi = aux_pi*self.aux_pis[p][q]
                    aux_mean.append(self.aux_means[p][q])
                    aux_sigma.append(self.aux_covs[p][q])
                aux_mean = np.array(aux_mean)
                aux_sigma = np.diag(aux_sigma)
                aux_cov = np.block([[sigma, np.zeros((len(sigma), len(aux_sigma)))], [np.zeros((len(aux_sigma), len(sigma))), aux_sigma]])
                # STEP 2: computes mean and covariance matrix for the extended component
                new_mu = deepcopy(mu)
                new_mu[i] = sum([self.add_coeff[s]*aux_mean[s] for s in range(len(aux_mean))]) + self.add_const
                new_sigma = deepcopy(sigma)
                new_sigma[i,i] = sum([self.add_coeff[s]**2*aux_cov[s,s] for s in range(len(aux_mean))])
                new_sigma[i,i] = new_sigma[i,i] + sum([2*self.add_coeff[s]*self.add_coeff[t]*aux_cov[s,t] for s in range(len(aux_mean)) for t in range(s+1, len(aux_mean)) ])
                for j in range(len(mu)):
                    if j!=i:
                        new_sigma[i,j] = new_sigma[j,i] = sum([self.add_coeff[s]*aux_cov[s,j] for s in range(len(aux_mean))])
                # STEP 3: appends weight, new mean and new covariance matrix to the final vectors
                final_pi.append(aux_pi)
                final_mu.append(new_mu)
                final_sigma.append(new_sigma)
            return GaussianMix(final_pi, final_mu, final_sigma)
        
        self.func = add_func
        
        
    def enterMonom(self,ctx):
        if not ctx.vars_() is None:
            if not ctx.vars_().ID() is None:
                ID = ctx.vars_().ID().getText()
                if not ctx.NUM() is None:
                    coeff = self.flag_sign*float(ctx.NUM().getText())
                else:
                    coeff = self.flag_sign
                idx = self.var_list.index(ID)
                self.add_coeff[idx] = coeff
            elif not ctx.vars_().gm() is None:
                self.aux_pis.append(eval(ctx.vars_().gm().list_()[0].getText()))
                self.aux_means.append(eval(ctx.vars_().gm().list_()[1].getText()))
                self.aux_covs.append(np.array(eval(ctx.vars_().gm().list_()[2].getText()))**2)
                if not ctx.NUM() is None:
                    self.add_coeff.append(self.flag_sign*float(ctx.NUM().getText()))
                else: 
                    self.add_coeff.append(self.flag_sign)
        else:
            self.add_const = self.add_const + self.flag_sign*float(ctx.NUM().getText())
            
            
    def enterSub(self, ctx):
        self.flag_sign = -1.
        
    def enterSum(self, ctx):
        self.flag_sign = 1.
        
    def enterMul(self, ctx):
        
        self.mul_const = 1
        self.mul_idx = []
        
        if not ctx.NUM() is None:
            self.mul_const = float(ctx.NUM().getText())
        for var in ctx.vars_():
            if not var.ID() is None:
                self.mul_idx.append(self.var_list.index(var.ID().getText()))
            elif not var.gm() is None:
                self.aux_pis.append(eval(var.gm().list_()[0].getText()))
                self.aux_means.append(eval(var.gm().list_()[1].getText()))
                self.aux_covs.append(np.array(eval(var.gm().list_()[2].getText()))**2)
                self.mul_idx.append(int(len(self.var_list)+len(self.aux_pis)-1))
        
        def mul_func(comp):
            i = self.target
            j, k = self.mul_idx
            mu = comp.gm.mu[0]
            sigma = comp.gm.sigma[0]
            final_pi = []
            final_mu = []
            final_sigma = []
            for part in product(*[range(len(mean)) for mean in self.aux_means]):
                # STEP 1: for a given combination of components of the auxiliary variables, creates a new component extending comp
                aux_pi = 1
                aux_mean = list(deepcopy(mu))
                aux_sigma = []
                for p,q in zip(range(len(self.aux_means)), part):
                    aux_pi = aux_pi*self.aux_pis[p][q]
                    aux_mean.append(self.aux_means[p][q])
                    aux_sigma.append(self.aux_covs[p][q])
                aux_mean = np.array(aux_mean)
                aux_sigma = np.diag(aux_sigma)
                aux_cov = np.block([[sigma, np.zeros((len(sigma), len(aux_sigma)))], [np.zeros((len(aux_sigma), len(sigma))), aux_sigma]])
                # STEP 2: computes mean and covariance matrix for the extended component
                new_mu = deepcopy(mu)
                new_mu[i] = self.mul_const*(aux_cov[j,k] + aux_mean[j]*aux_mean[k])
                new_sigma = deepcopy(sigma)
                new_sigma[i,i] = self.mul_const**2*(aux_cov[j,k]**2 + 2*aux_cov[j,k]*aux_mean[j]*aux_mean[k] + aux_cov[j,j]*aux_cov[k,k] + aux_cov[j,j]*aux_mean[k]**2 + aux_cov[k,k]*aux_mean[j]**2)
                for s in range(len(mu)):
                    if s!=i:
                        new_sigma[i,s] = new_sigma[s,i] = self.mul_const*(aux_mean[j]*(aux_cov[k,s] + aux_mean[k]*aux_mean[s]) + aux_mean[k]*(aux_cov[j,s] + aux_mean[j]*aux_mean[s]) - 2*aux_mean[j]*aux_mean[k]*aux_mean[s])
                # STEP 3: appends weight, new mean and new covariance matrix to the final vectors
                final_pi.append(aux_pi)
                final_mu.append(new_mu)
                final_sigma.append(new_sigma)
            return GaussianMix(final_pi, final_mu, final_sigma)
                        
        self.func = mul_func
        
    def enterPow(self, ctx):
        
        self.pow_vars = deepcopy(self.var_list)
        self.pow_idx = None
        
        if not ctx.vars_().ID() is None:
            self.pow_idx = int(self.var_list.index(ctx.vars_().ID().getText()))
        elif not ctx.vars_().gm() is None:
            self.pow_vars.append('aux{}'.format(len(self.aux_pis)))
            self.aux_pis.append(eval(ctx.vars_().gm().list_()[0].getText()))
            self.aux_means.append(eval(ctx.vars_().gm().list_()[1].getText()))
            self.aux_covs.append(np.array(eval(ctx.vars_().gm().list_()[2].getText()))**2)
            self.pow_idx = len(self.pow_vars)-1
            
        def pow_func(comp):
            i = self.target
            j = self.pow_idx
            mu = comp.gm.mu[0]
            sigma = comp.gm.sigma[0]
            final_pi = []
            final_mu = []
            final_sigma = []
            for part in product(*[range(len(mean)) for mean in self.aux_means]):
                # STEP 1: for a given combination of components of the auxiliary variables, creates a new component extending comp
                aux_pi = 1
                aux_mean = list(deepcopy(mu))
                aux_sigma = []
                for p,q in zip(range(len(self.aux_means)), part):
                    aux_pi = aux_pi*self.aux_pis[p][q]
                    aux_mean.append(self.aux_means[p][q])
                    aux_sigma.append(self.aux_covs[p][q])
                aux_mean = np.array(aux_mean)
                aux_sigma = np.diag(aux_sigma)
                aux_cov = np.block([[sigma, np.zeros((len(sigma), len(aux_sigma)))], [np.zeros((len(aux_sigma), len(sigma))), aux_sigma]])
                # STEP 2: computes mean and covariance matrix for the extended component
                new_mu = deepcopy(mu)
                new_mu[i] = aux_cov[j,j] + aux_mean[j]*aux_mean[j]
                new_sigma = deepcopy(sigma)
                new_sigma[i,i] = 2*aux_cov[j,j]**2 + 4*(aux_mean[j]**2)*aux_cov[j,j]
                for k in range(len(mu)):
                    if k!=i:
                        new_sigma[i,k] = new_sigma[k,i] = 2*aux_mean[j]*(aux_cov[j,k] + aux_mean[j]*aux_mean[k])-2*aux_mean[j]**2*aux_mean[k]
                # STEP 3: appends weight, new mean and new covariance matrix to the final vectors
                final_pi.append(aux_pi)
                final_mu.append(new_mu)
                final_sigma.append(new_sigma)
            return GaussianMix(final_pi, final_mu, final_sigma)
        
        self.func = pow_func

def asgmt_parse(var_list, expr):
    """ Parses expr using ANTLR4. Returns a function """
    lexer = ASGMTLexer(InputStream(expr))
    stream = CommonTokenStream(lexer)
    parser = ASGMTParser(stream)
    tree = parser.assignment()
    asgmt_rule = AsgmtRule(var_list)
    walker = ParseTreeWalker()
    walker.walk(asgmt_rule, tree) 
    return asgmt_rule.func
        
        
def update_rule(dist, expr):
    """ Applies expr to dist. It first parses expr using the function asgmt_parse, implemented as an ANTLR listener. asgmt_parse returns a function rule_func, such that, rule_func(GaussianMix) returns a new GaussianMix object obtained applying expr to the initial distribution. rule_func is applied to each component of dist, and the resulting Gaussian mixtures are stored in a single GaussianMix object."""
    if expr == 'skip':
        return dist
    else:
        rule_func = asgmt_parse(dist.var_list, expr)    # define function
        new_pi = []
        new_mu = []
        new_sigma = []
        for k in range(dist.gm.n_comp()):
            comp = Dist(dist.var_list, dist.gm.comp(k))
            new_mix = rule_func(comp)
            for h in range(new_mix.n_comp()):
                new_pi.append(dist.gm.pi[k]*new_mix.pi[h])
                new_mu.append(new_mix.mu[h])
                new_sigma.append(new_mix.sigma[h])
        return Dist(dist.var_list, GaussianMix(new_pi, new_mu, new_sigma))
    
    


    
    
    