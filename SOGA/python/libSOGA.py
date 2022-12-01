# Contains the function start_soga, which is used to invoke SOGA on a CFG object and the recursive function SOGA, which, depending on the type of the visited node, calls the functions needed to update the current distribution. 

#Such functions are contained in the auxiliary libraries:
# - libSOGAtruncate, containing functions for computing the resulting distribution when a truncation occurs (in conditional or observe instructions);
# - libSOGAupdate, containing functions for computing the resulting distribution after applying an assignment instruction;
# - libSOGAmerge, containing functions for computing the resulting distribution when a merge instruction is encountered;

# Additional functions for general purpose are defined in the library libSOGAshared, which is imported by all previous libraries.

# TO DO:
# - improve dependencies on libraries (all auxiliary libraries import libSOGAshared, maybe there is a more efficient way to do this?)
# - libSOGAmerge: add other pruning  
# - parallelize truncations

from libSOGAtruncate import *
from libSOGAupdate import *
from libSOGAmerge import *
import timing

def start_SOGA(cfg, pruning=None, Kmax=None):
    """ Invokes SOGA on the root of the CFG object cfg, initializing current_distribution to a Dirac delta centered in zero.
        If pruning='classic' implements pruning at the merge nodes with maximum number of component Kmax.
        Returns an object Dist (defined in libSOGAshared) with the final computed distribution."""
    #timing.trunc_time.clear()
    #timing.update_time.clear()
    #timing.merge_time.clear()
    #timing.change_time = 0
    #timing.mom_time = 0
    var_list = cfg.ID_list
    gm = GaussianMix([1.], [np.array([0.]*len(var_list))], [np.zeros((len(var_list),len(var_list)))])
    init_dist = Dist(var_list, gm)
    SOGA(cfg.root, 1, init_dist, None, pruning, Kmax)
    start = time()
    p, current_dist = merge(cfg.node_list['exit'].list_dist, pruning, Kmax)
    end = time()
    #timing.merge_time.append(end-start)
    #print('Truncations:', len(timing.trunc_time), 'total:', sum(timing.trunc_time))
    #print('Updates:', len(timing.update_time), 'total:', sum(timing.update_time))
    #print('Mergings:', len(timing.merge_time), 'total:', sum(timing.merge_time))
    #print('Time for changing coordinates:', timing.change_time, '\tTime for moments computation:', timing.mom_time)
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
            start = time()
            p, current_dist = truncate(current_dist, current_trunc)   ### see libSOGAtruncate
            end = time()
            timing.trunc_time.append(end-start)
            current_p = p*current_p
        if current_p > prob_tol:
            start = time()
            current_dist = update_rule(current_dist, node.expr)         ### see libSOGAupdate
            end = time()
            timing.update_time.append(end-start)
        if node.children[0].type == 'merge' or node.children[0].type == 'exit':
            node.children[0].list_dist.append((current_p, current_dist))
        SOGA(node.children[0], deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc), pruning, Kmax)
            
    # if observe truncates to LBC and calls on children
    if node.type == 'observe':
        current_trunc = node.LBC
        start = time()
        _, current_dist = truncate(current_dist, current_trunc)
        end = time()
        timing.trunc_time.append(end-start)
        for child in node.children:
            SOGA(child, deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc), pruning, Kmax)

    # if merge checks whether all paths have been explored.
    # Either returns or merge distributions and calls on children
    if node.type == 'merge':
        if len(node.list_dist) != len(node.parent):
            return
        else:
            start = time()
            current_p, current_dist = merge(node.list_dist, pruning, Kmax)        ### see libSOGAmerge
            end = time()
            timing.merge_time.append(end-start)
            node.list_dist = []
            for child in node.children:
                SOGA(child, deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc), pruning, Kmax)
    if node.type == 'exit':
        return
