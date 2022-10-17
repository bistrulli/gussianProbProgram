from libSOGAshared import *

def negate(trunc):
    if '<' in trunc:
        if '<=' in trunc:
            trunc = trunc.replace('<=', '>')
        else:
            trunc = trunc.replace('<', '>=')
    elif '>' in trunc:
        if '>=' in trunc:
            trunc = trunc.replace('>=', '<')
        else:
            trunc = trunc.replace('>', '<=')
    elif '==' in trunc:
        trunc = trunc.replace('==', '!=')
    elif '!=' in turnc:
        trunc = trunc.replace('!=', '==')
    return trunc


def truncate(dist, trunc):
    """ Given a distribution dist computes its truncation to trunc"""
    if trunc == 'true':
        return 1., dist
    elif trunc == 'false':
        return 0., dist
    else:
        d = len(dist.var_list)
        # creates an augmented distribution with new variables appearing in aux_trunc (needed when gm(...) is involved)
        aux_dist, aux_trunc = extract_aux(dist, trunc)
        # converts aux_trunc to symbolic
        aux_trunc = sym_trunc(aux_trunc)
        # iterates on the component and truncates each one of them storing the relative probabilities on trunc
        new_dist = Dist(dist.var_list, GaussianMix([],[],[]))
        new_pi = []
        for k in range(aux_dist.gm.n_comp()):
            comp = Dist(aux_dist.var_list, aux_dist.gm.comp(k))
            p, mu, sigma = truncate_gaussian(comp, aux_trunc) 
            if p > prob_tol:
                new_dist.gm.mu.append(mu[:d])
                new_dist.gm.sigma.append(sigma[:d,:d])
                new_pi.append(aux_dist.gm.pi[k]*p)
        norm_factor = sum(np.array(new_pi))
        if norm_factor > prob_tol:
            new_dist.gm.pi = list(np.array(new_pi)/norm_factor)
        return norm_factor, new_dist


def sym_trunc(trunc):
    """ Returns a symbolic version of trunc """
    if '==' in trunc:
        lhs, rhs = trunc.split('==')
        trunc = Eq(sympify(lhs), sympify(rhs))
        trunc = simplify_logic(trunc)
    elif '!=' in trunc:
        lhs, rhs = trunc.split('!=')
        trunc = Ne(sympify(lhs), sympify(rhs))
        trunc = simplify_logic(trunc)
    else:
        trunc = simplify_logic(sympify(trunc))
    return trunc
 
    
def truncate_gaussian(dist, trunc):
    """ Given a distribution dist whose gm is has a single component computes its truncation to trunc """
    mu = dist.gm.mu[0]
    sigma = dist.gm.sigma[0]
# substitutes deterministic values, if the truncation becomes true or false returns
    trunc = substitute_deltas(dist, trunc)
    if str(trunc) == 'False':
        return 0, mu, sigma
    if str(trunc) == 'True':
        return 1, mu, sigma
    if type(trunc) is Equality:
        return 0, mu, sigma
    if type(trunc) is Unequality:
        return 1, mu, sigma
# extracts the vector (a_1, a_2, ..., a_k) of the truncation and the extremes of the hyper-rectangle
    alpha, c = extract_alpha(trunc, dist.var_list)
# changes coordinates so that the line alpha*x = 0 is one of the axis
    A = find_basis(alpha)
    transl_mu = A.dot(mu)
    transl_sigma = A.dot(sigma).dot(A.transpose())
    #transl_sigma = matrix_check(transl_sigma) 
# finds the indices of the components that needs to be transformed
    transl_alpha = np.zeros(len(transl_mu))
    transl_alpha[0] = 1
    indices = select_indices(transl_alpha, transl_sigma)
# creates reduced vectors taking into account only the coordinates that need to be transformed
    red_transl_alpha = reduce_indices(transl_alpha, indices)
    red_transl_mu = reduce_indices(transl_mu, indices)
    red_transl_sigma = reduce_indices(transl_sigma, indices) 
    #print('Calling control after reduction')
    #red_transl_sigma = matrix_check(red_transl_sigma)
# creates the hyper-rectangle to integrate on
    a = np.ones(len(red_transl_alpha))*(-1.e10)
    b = np.ones(len(red_transl_alpha))*(1.e10)
    if type(trunc) is StrictGreaterThan or type(trunc) is GreaterThan:
        a[0] = c/np.linalg.norm(alpha)
    if type(trunc) is StrictLessThan or type(trunc) is LessThan:
        b[0] = c/np.linalg.norm(alpha)    
# compute moments in the transformed coordinates
    new_P, new_red_transl_mu, new_red_transl_sigma = compute_moments(red_transl_mu, red_transl_sigma, a, b)
    #print('Calling control after truncation')
    #new_red_transl_sigma = matrix_check(new_red_transl_sigma)
# recreates extended vectors
    new_transl_mu = extend_indices(new_red_transl_mu, transl_mu, indices)
    new_transl_sigma = extend_indices(new_red_transl_sigma, transl_sigma, indices)
    #print('Calling control after extension')
    #new_transl_sigma = matrix_check(new_transl_sigma)
# goes back to older coordinates
    A_inv = np.linalg.inv(A)
    new_mu = A_inv.dot(new_transl_mu)
    new_sigma = A_inv.dot(new_transl_sigma).dot(A_inv.transpose())
    #print('Calling control after translating back')
    #new_transl_sigma = matrix_check(new_transl_sigma)
    return new_P, new_mu, new_sigma


def extract_alpha(trunc, var_name):
    # saves the two parts of the inequality in poly_lhs and poly_rhs
    poly_lhs = trunc.args[0]
    poly_rhs = trunc.args[1]
    # computes the constant, changing sign if needed, as if it is on the RHS
    if poly_rhs.is_constant():
        c = float(poly_rhs)
    elif poly_lhs.is_constant():
        c = -float(poly_lhs)
    else:
        c = 0  
    # computes the coefficients of the variables, changing signs if needed, as if they are on the LHS and saves them (ordered as in var_name) to the vector alpha
    coeff_dict = {var:0 for var in var_name}
    for sym in poly_lhs.free_symbols:
        coeff_dict[str(sym)] = float(Poly(poly_lhs).coeff_monomial(str(sym)))
    for sym in poly_rhs.free_symbols:
        coeff_dict[str(sym)] = -float(Poly(poly_rhs).coeff_monomial(str(sym)))
    alpha = np.zeros(len(var_name))
    for i, var in enumerate(var_name):
        alpha[i] = coeff_dict[var]
    return alpha, c

def find_basis(alpha):
    """
    Given alpha (vector of the truncation) returns a matrix A giving the change of variable necessary to make alpha one of the axis
    """
    alpha = alpha/np.linalg.norm(alpha)
    u, s, v = np.linalg.svd([alpha])
    alpha1 = v[:,1:]
    A = np.vstack((alpha.reshape(1,alpha.shape[0]), alpha1.transpose()))
    return A


def select_indices(alpha, sigma):
    """
    Finds the indices of the components that needs to be transformed based on the vector representation of the truncation (alpha)
    and the covariance matrix (sigma)
    """
    
    def enlarge_set(index_set):
        total_set = index_set
        for i in index_set:
            i_indices = list(np.where(sigma[i,:] != 0)[0])
            total_set = list(set(total_set + i_indices))
        return total_set
    
    init_set = list(np.where(alpha!=0)[0])
    new_set = enlarge_set(init_set)
    while set(init_set) != set(new_set):
        init_set = new_set
        new_set = enlarge_set(init_set)   
    return np.sort(new_set)  

def reduce_indices(vec, indices):
    """
    Extracts subvector/submatrix indexed by indices
    """
    try:
        vec = np.array(vec, dtype='float32')
    except np.ComplexWarning:
        print(vec)    
    if len(vec.shape) == 1:
        red_vec = vec[indices]
    if len(vec.shape) == 2:
        red_vec = vec[indices][:,indices]
    return red_vec


def extend_indices(red_vec, old_vec, indices):
    """
    puts red_vec in the indices of old_vec
    """
    red_vec = np.array(red_vec, dtype='float32')
    old_vec = np.array(old_vec, dtype='float32')
    if len(old_vec.shape) == 1:
        for red_i, i in enumerate(indices):
            old_vec[i] = red_vec[red_i]
    if len(old_vec.shape) == 2:
        for red_i, i in enumerate(indices):
            for red_j, j in enumerate(indices):
                old_vec[i,j] = old_vec[j,i] = red_vec[red_i,red_j]
    return old_vec


### compute moments functions

def partitionfunc(n,k,l=0):
    """
    n is the integer to partition, k is the length of partitions, l is the min partition element size
    """
    if k < 1:
        return
    if k == 1:
        if n >= l:
            yield (n,)
        return
    for i in range(l,n+1):
        for result in partitionfunc(n-i,k-1):
            yield (i,)+result


def _prob(mu, sigma, a, b):
    """
    Computes the mass probability of the normal distribution with mean mu and covariance matrix sigma in the 
    hyper-rectangle [a,b].
    Even for one-dimensional distributions, mu, sigma, a, b must be vectors.
    """
    n = len(mu)
    P = 0
    for i_list in product(*[[0,1]]*n):
        x = np.zeros(n)
        for i, idx in enumerate(i_list):
            if idx==0:
                x[i] = a[i]
            else:
                x[i] = b[i]
        try:
            p = mvnorm.cdf(x,mean=mu,cov=sigma,allow_singular=True)
        except ValueError:
            sigma = make_psd(sigma)
            p = mvnorm.cdf(x,mean=mu,cov=sigma,allow_singular=True)
        if np.isnan(p):
            new_x = list(x) + [0]
            new_mu = list(mu) + [0]
            new_sigma = list(sigma)
            for i in range(len(sigma)):
                new_sigma[i] = list(sigma[i]) + [0]
            new_sigma.append([0]*(len(sigma)+1))
            p = mvnorm.cdf(new_x, mean=new_mu, cov=new_sigma, allow_singular=True)
        P = P + ((-1)**(n-sum(i_list)))*p
    #P = norm.cdf(b[0], loc=mu[0], scale=sigma[0,0]) - norm.cdf(a[0], loc=mu[0], scale=sigma[0,0])
    return P
    

def compute_lower_mom(mu, sigma, a, b, trunc_idx, trunc):
    """
    Given a normal with mean mu and cov matrix sigma,  truncated to [a,b] (where a[i] = -inf and b[i] = inf except
    for a[trunc_idx] (if trunc = low) or b[trunc_idx] (if trunc=up)), computes the first two orders moments of a 
    (n-1) dimensional normal distribution with mean \tilde(mu), \tilde(sigma) (as defined in Kan-Robotti).
    """
    n = len(mu)
    c = np.delete(a, trunc_idx)
    d = np.delete(b, trunc_idx)
    # computes the new mean
    if trunc == 'low':
        muj = np.delete(mu, trunc_idx) + ((a[trunc_idx]-mu[trunc_idx])/sigma[trunc_idx, trunc_idx])*np.delete(sigma, trunc_idx, axis=0)[:,trunc_idx]
    elif trunc == 'up':
        muj = np.delete(mu, trunc_idx) + ((b[trunc_idx]-mu[trunc_idx])/sigma[trunc_idx, trunc_idx])*np.delete(sigma, trunc_idx, axis=0)[:,trunc_idx]
    # computes the new covariance matrix
    sigmaj = np.delete(sigma, trunc_idx, axis=0)
    sigmaj = np.delete(sigmaj, trunc_idx, axis=1)
    sigmaj = sigmaj - (1/sigma[trunc_idx, trunc_idx])*np.delete(sigma, trunc_idx, axis=0)[:,trunc_idx].reshape(len(sigma)-1,1) @         np.delete(sigma, trunc_idx, axis=1)[trunc_idx,:].reshape(1,len(sigma)-1)  
    # saves the moments in a dictionary
    dict_mom_lower = {}
    for k in range(3):
        for part in partitionfunc(k, n-1):
            if sum(part) == 0:
                dict_mom_lower[part] = 1
            if sum(part) == 1:
                idx = np.where(np.array(part) == 1)[0][0]
                dict_mom_lower[part] = muj[idx]
            if sum(part) == 2:
                idx_list = np.where(np.array(part)!=0)[0]
                if len(idx_list) == 2:
                    idx1, idx2 = idx_list
                    dict_mom_lower[part] = sigmaj[idx1, idx2] + muj[idx1]*muj[idx2]
                elif len(idx_list) == 1:
                    idx = idx_list[0]
                    dict_mom_lower[part] = sigmaj[idx, idx] + muj[idx]**2
    return dict_mom_lower


def _compute_mom1(n, k, mu, sigma, a, b, trunc_idx, trunc, dict_mom):
    c = np.zeros(n)
    idx = np.where(np.array(k)==1)[0][0]
    if trunc == 'low':
        c[trunc_idx] = norm.pdf(a[trunc_idx], loc=mu[trunc_idx], scale=np.sqrt(sigma[trunc_idx,trunc_idx]))
    elif trunc == 'up':
        c[trunc_idx] = -norm.pdf(b[trunc_idx], loc=mu[trunc_idx], scale=np.sqrt(sigma[trunc_idx,trunc_idx]))
    return mu[idx]*dict_mom[tuple(n*[0])] + np.array(k).dot(sigma).dot(c)           


def _compute_mom2(n, k, mu, sigma, a, b, trunc_idx, trunc, dict_mom, dict_mom_lower):
    c = np.zeros(n)
    index_list = np.where(np.array(k)!=0)[0]
    if len(index_list) == 2:
        idxk, idxe = index_list
        ek = np.zeros(n)
        ek[idxk] = 1
        e = np.zeros(n)
        e[idxe] = 1
        for i in range(n):
            if i == idxk:
                c[i] = dict_mom[tuple(n*[0])]
            if i == trunc_idx:
                if trunc == 'low':
                    c[i] = c[i] + (a[i]**ek[i])*norm.pdf(a[i], loc=mu[i], scale=np.sqrt(sigma[i,i]))*dict_mom_lower[tuple(np.delete(ek,i))]
                elif trunc == 'up':
                    c[i] = c[i] - (b[i]**ek[i])*norm.pdf(b[i], loc=mu[i], scale=np.sqrt(sigma[i,i]))*dict_mom_lower[tuple(np.delete(ek,i))]
        return mu[idxe]*dict_mom[tuple(ek)] + e.dot(sigma).dot(c)   
    elif len(index_list) == 1:
        idx = index_list[0]
        e = np.zeros(n)
        e[idx] = 1
        for i in range(n):
            if i == idx:
                c[i] = dict_mom[tuple(n*[0])]
            if i == trunc_idx:
                if trunc == 'low':
                    c[i] = c[i] + (a[i]**e[i])*norm.pdf(a[i], loc=mu[i], scale=np.sqrt(sigma[i,i]))*dict_mom_lower[tuple(np.delete(e,i))]
                elif trunc == 'up':
                    c[i] = c[i] - (b[i]**e[i])*norm.pdf(b[i], loc=mu[i], scale=np.sqrt(sigma[i,i]))*dict_mom_lower[tuple(np.delete(e,i))]
        return mu[idx]*dict_mom[tuple(e)] + e.dot(sigma).dot(c)           

def compute_moments(mu, sigma, a, b):
    """
    Given a normal distribution with mean mu and covariance matrix sigma, truncated to [a,b], where all a_i=-np.inf and
    all b_i=np.inf except at most one a_i or one b_i, computes exactly the mean and the covariance matrix of the 
    truncated distribution
    """        
    a = np.array(a, dtype='float32')
    b = np.array(b, dtype='float32')
    n = len(a)   
    # truncation in one dimension
    if n==1:
        new_P = norm.cdf(b[0], loc=mu[0], scale=np.sqrt(sigma[0,0])) - norm.cdf(a[0], loc=mu[0], scale=np.sqrt(sigma[0,0]))
        new_mu, new_sigma = truncnorm.stats(loc=mu[0], scale=np.sqrt(sigma[0,0]), a=(a[0]-mu[0])/np.sqrt(sigma[0,0]), b=(b[0]-mu[0])/np.sqrt(sigma[0,0]), moments='mv')
        new_mu = np.array([new_mu])
        new_sigma = np.array([[new_sigma]])
        return new_P, new_mu, new_sigma
    # if in more dimensions applies Kan-Robotti formulas
    # first determines if the truncation is 'low' (i.e. x > c) or 'up' (i.e. x < c)
    trunc_idx = 0
    if a[0] > -1.e10:
        trunc = 'low'
    else:
        trunc = 'up'  
    # returns the moments for the distribution of dimension n-1, in which the trunc_idx component has been removed
    dict_mom_lower = compute_lower_mom(mu, sigma, a, b, trunc_idx, trunc)  
    # computes first two order moments using the recurrence formulas of Kan-Robotti and stores them in a dictionary
    dict_mom = {}
    for k in range(3):
        for part in partitionfunc(k, n): 
            if sum(part) == 0:
                dict_mom[part] = _prob(mu, sigma, a, b)
                if dict_mom[part] < prob_tol:
                    return 0, mu, sigma
            if sum(part) == 1:
                dict_mom[part] = _compute_mom1(n, part, mu, sigma, a, b, trunc_idx, trunc, dict_mom)
            if sum(part) == 2:
                dict_mom[part] = _compute_mom2(n, part, mu, sigma, a, b, trunc_idx, trunc, dict_mom, dict_mom_lower)              
    # assembles the dictionaries result in new_P, new_mu, new_sigma
    new_P = dict_mom[tuple(n*[0])]
    new_mu = np.zeros(n)
    new_sigma = np.zeros((n,n))
    for i in range(n):
        e = np.zeros(n)
        e[i] = 1
        new_mu[i] = dict_mom[tuple(e)]/new_P
        new_sigma[i,i] = dict_mom[tuple(2*e)]/new_P - (dict_mom[tuple(e)]/new_P)**2
        for j in range(i):
            f = np.zeros(n)
            f[j] = 1
            new_sigma[i,j] = new_sigma[j,i] = dict_mom[tuple(e+f)]/new_P - (dict_mom[tuple(e)]/new_P)*(dict_mom[tuple(f)]/new_P)
    return new_P, new_mu, new_sigma
