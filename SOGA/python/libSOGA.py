from libSOGAtruncate import *
from libSOGAupdate import *
from libSOGAmerge import *

### MAIN ALGORITHM 

def start_SOGA(cfg):
    var_list = cfg.ID_list
    gm = GaussianMix([1.], [np.array([0.]*len(var_list))], [np.zeros((len(var_list),len(var_list)))])
    init_dist = Dist(var_list, gm)
    SOGA(cfg.root, 1, init_dist, None)
    p, current_dist = merge(cfg.node_list['exit'].list_dist)
    cfg.node_list['exit'].list_dist = []
    return p, current_dist

def SOGA(node, current_p, current_dist, current_trunc):
    
    # starts execution
    if node.type == 'entry':
        for child in node.children:
            SOGA(child, deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc))
    
    # if tests saves LBC and calls on children
    if node.type == 'test':
        current_trunc = node.LBC
        for child in node.children:
            SOGA(child, deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc))
     
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
        SOGA(node.children[0], deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc))
            
    # if observe truncates to LBC and calls on children
    if node.type == 'observe':
        current_trunc = node.LBC
        _, current_dist = truncate(current_dist, current_trunc)
        for child in node.children:
            SOGA(child, deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc))

    # if merge checks whether all paths have been explored.
    # Either returns or merge distributions and calls on children
    if node.type == 'merge':
        if len(node.list_dist) != len(node.parent):
            return
        else:
            current_p, current_dist = merge(node.list_dist)        ### see libSOGAmerge
            node.list_dist = []
            for child in node.children:
                SOGA(child, deepcopy(current_p), deepcopy(current_dist), deepcopy(current_trunc))
            
    if node.type == 'exit':
        return
