# Contains the function start_soga, which is used to invoke SOGA on a CFG object and the recursive function SOGA, which, depending on the type of the visited node, calls the functions needed to update the current distribution. 

#Such functions are contained in the auxiliary libraries:
# - libSOGAtruncate, containing functions for computing the resulting distribution when a truncation occurs (in conditional or observe instructions);
# - libSOGAupdate, containing functions for computing the resulting distribution after applying an assignment instruction;
# - libSOGAmerge, containing functions for computing the resulting distribution when a merge instruction is encountered;

# Additional functions for general purpose are defined in the library libSOGAshared, which is imported by all previous libraries.

# TO DO:
# - improve dependencies on libraries (all auxiliary libraries import libSOGAshared, maybe there is a more efficient way to do this?)
# - libSOGAtruncate: currently raising an error if in continuous conditioning a singular matrix is encountered. It should be possible to deal with these cases without rephrasing the program
# - libSOGAmerge: add other pruning strategies

from libSOGAtruncate import *
from libSOGAupdate import *
from libSOGAmerge import *

def start_SOGA(cfg, pruning=None, Kmax=None):
    """ Invokes SOGA on the root of the CFG object cfg, initializing current_distribution to a Dirac delta centered in zero.
        If pruning='classic' implements pruning at the merge nodes with maximum number of component Kmax.
        Returns an object Dist (defined in libSOGAshared) with the final computed distribution."""
    var_list = cfg.ID_list
    gm = GaussianMix([1.], [np.array([0.]*len(var_list))], [np.zeros((len(var_list),len(var_list)))])
    init_dist = Dist(var_list, gm)
    SOGA(cfg.root, 1, init_dist, None, pruning, Kmax)
    p, current_dist = merge(cfg.node_list['exit'].list_dist, pruning, Kmax)
    cfg.node_list['exit'].list_dist = []
    return current_dist



def SOGA(node, current_p, current_dist, current_trunc, pruning, Kmax):
    
    # starts execution
    if node.type == 'entry':
        for child in node.children:
            SOGA(child, deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc), pruning, Kmax)
    
    # if tests saves LBC and calls on children
    if node.type == 'test':
        current_trunc = node.LBC
        for child in node.children:
            SOGA(child, deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc), pruning, Kmax)
     
    # if state checks wheter cond!=None. If yes, truncates to current_trunc, eventually negating it. In any case applies the rule in expr. Appends the distribution in the next merge node or calls recursively on children.
    if node.type == 'state':
        if node.cond != None:
            if node.cond == False:
                current_trunc = negate(current_trunc) 
            p, current_dist = truncate(current_dist, current_trunc)   ### see libSOGAtruncate
            current_p = p*current_p
        if current_p > prob_tol:
            current_dist = update_rule(current_dist, node.expr)         ### see libSOGAupdate
        if node.children[0].type == 'merge' or node.children[0].type == 'exit':
            node.children[0].list_dist.append((current_p, current_dist))
        SOGA(node.children[0], deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc), pruning, Kmax)
            
    # if observe truncates to LBC and calls on children
    if node.type == 'observe':
        current_trunc = node.LBC
        _, current_dist = truncate(current_dist, current_trunc)
        for child in node.children:
            SOGA(child, deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc), pruning, Kmax)

    # if merge checks whether all paths have been explored.
    # Either returns or merge distributions and calls on children
    if node.type == 'merge':
        if len(node.list_dist) != len(node.parent):
            return
        else:
            current_p, current_dist = merge(node.list_dist, pruning, Kmax)        ### see libSOGAmerge
            node.list_dist = []
            for child in node.children:
                SOGA(child, deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc), pruning, Kmax)
    if node.type == 'exit':
        return
