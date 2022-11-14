# Contains the functions for computing the resulting distribution when an assignment instruction is encountered (in state nodes).

# SOGA (defined in SOGA.py)
# |- update_rule
#    |- sym_expr
#    |- update_gaussian



from libSOGAshared import *


def update_rule(dist, expr):
    """ Applies expr to dist by calling update_gaussian on each component """
    if expr == 'skip':
        return dist
    else:
        aux_dist, aux_expr = extract_aux(dist, expr)
        target, rule = sym_expr(aux_expr)
        d = len(dist.var_list)
        new_mu = []
        new_sigma = []
        for k in range(aux_dist.gm.n_comp()):
            comp = Dist(aux_dist.var_list, aux_dist.gm.comp(k))
            mu, sigma = update_gaussian(target, rule, comp)     
            new_mu.append(mu[:d])
            new_sigma.append(sigma[:d,:d])
        return Dist(dist.var_list, GaussianMix(aux_dist.gm.pi, new_mu, new_sigma))        
        
    
def sym_expr(expr):
    """ Returns a pair (target, rule), where target variable that is being assigned the symbolic expression rule """
    target, rule = expr.split('=')
    rule = sympify(rule)
    return target, rule


def update_gaussian(target, rule, comp):
    """ Assigns rule to target in comp, where comp is a distribution having as gm a single component. Returns mu, sigma of the updated distribution """
    
    rule = substitute_deltas(comp, rule)
    i = comp.var_list.index(target)
    mu = comp.gm.mu[0]
    sigma = comp.gm.sigma[0]
    var_name = comp.var_list
    
    def E(i,j):
        """
        Computes expectation of X_iX_j where X_i, X_j are components of a vector normally distributed with mean mu and 
        covariance matrix sigma
        """
        return sigma[i,j] + mu[i]*mu[j]

    new_mu = deepcopy(mu)
    new_sigma = deepcopy(sigma)
    
    # If the rule is x_i = x_j^2 
    if rule.is_Pow:
        for arg in rule.args:
            if arg.is_Number:
                exp = float(arg)
                if exp != 2:
                    raise Warning('Power with exponent different than 2 not supported!')
            if arg.is_Symbol:
                j = var_name.index(str(arg))
            new_mu[i] = E(j,j)
            new_sigma[i,i] = 2*sigma[j,j]**2 + 4*(mu[j]**2)*sigma[j,j]
            for k in range(len(mu)):
                if k!=i:
                    new_sigma[i,k] = new_sigma[k,i] = 2*mu[j]*E(j,k)-2*mu[j]**2*mu[k]
        return new_mu, new_sigma
        
    # If the rule is x_i = c*x_j(*x_k)?
    if rule.is_Mul:
        const = 1
        prod_var = []
        for arg in rule.args:
            if arg.is_Number:
                const = const*float(arg)
            if arg.is_Symbol:
                prod_var.append(str(arg))
        #Two options: product of two variables or a variable and a constant:
        if len(prod_var) == 1:
            j = var_name.index(prod_var[0])
            new_mu[i] = const*mu[j]
            new_sigma[i,i] = (const**2)*sigma[j,j]
            for k in range(len(mu)):
                if k!=i:
                    new_sigma[i,k] = new_sigma[k,i] = const*sigma[j,k]
        if len(prod_var) == 2:
            j = var_name.index(prod_var[0])
            k = var_name.index(prod_var[1])
            new_mu[i] = const*E(j,k)
            new_sigma[i,i] = const**2*(sigma[j,k]**2 + 2*sigma[j,k]*mu[j]*mu[k] + sigma[j,j]*sigma[k,k] + sigma[j,j]*mu[k]**2 + sigma[k,k]*mu[j]**2)
            for s in range(len(mu)):
                if s!=i:
                    new_sigma[i,s] = new_sigma[s,i] = const*(mu[j]*E(k,s)+mu[k]*E(j,s)-2*mu[j]*mu[k]*mu[s])
        return new_mu, new_sigma           
                
    # If the rule is x_i = c_1*x_1 + ... + c_nx_n + c
    if rule.is_Add:    
        alpha = np.zeros(len(mu))
        c = 0
        for arg in rule.args:
            if arg.is_Number:
                c = c + float(arg)
            if arg.is_Symbol:
                j = var_name.index(str(arg))
                alpha[j] = 1
            if arg.is_Mul:
                j = None
                for subarg in arg.args:
                    if subarg.is_Number:
                        const = float(subarg)
                    if subarg.is_Symbol:
                        j = var_name.index(str(subarg))
                if j is not None:
                    alpha[j] = const
        new_mu[i] = sum([alpha[s]*mu[s] for s in range(len(mu))]) + c
        new_sigma[i,i] = sum([alpha[s]**2*sigma[s,s] for s in range(len(mu))])
        new_sigma[i,i] = new_sigma[i,i] + sum([2*alpha[s]*alpha[t]*sigma[s,t] for s in range(len(mu)) for t in range(s+1, len(mu)) ])
        for j in range(len(mu)):
            if j!=i:
                new_sigma[i,j] = new_sigma[j,i] = sum([alpha[s]*sigma[s,j] for s in range(len(mu))])
        return new_mu, new_sigma
    
    # If the rule is x_i = c
    if rule.is_Number:
        new_mu[i] = float(rule)
        for k in range(len(mu)):
            new_sigma[i,k] = new_sigma[k,i] = 0
        return new_mu, new_sigma
    
    # If the rule is x_i = x_j
    if rule.is_Symbol:
        j = var_name.index(str(rule))
        new_mu[i] = mu[j]
        for k in range(len(mu)):
            if k!= i:
                new_sigma[i,k] = new_sigma[k,i] = sigma[j,k]
            else:
                new_sigma[i,k] = sigma[j,j]
        return new_mu, new_sigma
    
    
    