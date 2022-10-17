from libSOGAshared import *


def merge(list_dist):
    """
    Given a list of couples (p,dist), where each dist is a GaussianMix object, computes a couple (current_p, current_dist),     in which current_pi is the sum of p and current_dist is a single GaussianMix object.
    """
    final_pi = []
    final_mu = []
    final_sigma = []
    current_p = 0
    # creates a single mixture
    for (p, dist) in list_dist:
        if p > 0:
            current_p += p
            final_pi = final_pi + list(p*np.array(dist.gm.pi))
            final_mu = final_mu + list(dist.gm.mu)
            final_sigma = final_sigma + list(dist.gm.sigma)
    if len(final_pi) == 0:
        d = len(list_dist[0][1].gm.mu[0])
        #print('no components found')
        return 0, Dist(list_dist[0][1].var_list, GaussianMix([0], [np.array([0]*d)], [np.zeros((d,d))]))
    final_pi = list(np.array(final_pi)/current_p)
    # deletes components with probability less than tol
    zero_list = np.where(np.array(final_pi) < prob_tol)[0]
    if len(zero_list)>0:
        if len(zero_list) == len(final_pi):
            d = len(dist.gm.mu[0])
            #print('no components found')
            return 0, Dist(list_dist[0][1].var_list, GaussianMix([0], [np.array([0]*d)], [np.zeros((d,d))]))
        else:
            for index in sorted(zero_list, reverse=True):
                del final_pi[index]
                del final_mu[index]
                del final_sigma[index]
    current_dist = Dist(list_dist[0][1].var_list, GaussianMix(final_pi, final_mu, final_sigma))
    return current_p, current_dist
