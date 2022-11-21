# Contains the classes definition for CFG objects and the function produce_cfg, that extracts a CFG from a program script in a .txt file. 

# A CFGnode object can belong to six different subclasses (EntryNode, StateNode, TestNode, ObserveNode, MergeNode and ExitNode). All subclasses share the following attributes:
# - node_name, containing a string with a unique name for the node (usually in the form 'nodetypeX' with X integer progressively assigned);
# - node_type, containing a string with the node type;
# - parent, a list containing pointers to the parent nodes;
# - children, a list containing pointers to the children nodes;

# Furthermore some node have additional attributes and methods.

# StateNode objects have:
# - an expr attribute storing a string with a valid assignment instruction generated from the SOGA grammar reported in 'SOGA.g4';
# - a cond attribute which can take value True, False or None;
# - the methods set_expr, set_cond to set the values of the previous attributes to specific values.

# TestNode and ObserveNode objects have:
# - an LBC attribute storing a string with a valid LBC condition generated from the SOGA grammar;
# - the method set_LBC to set the values of the previous attribute to specific values.

# MergeNode objects have:
# - an attribute list_dist storing a list, initialized to the empty string.

# The class CFG is a subclass of the class SOGAListener automatically generetad by ANTLR4 from the grammar contained in 'SOGA.g4'. CFG extends the methods of SOGAListener so that when called on the parse tree of a valid SOGA script, the CFG representing the program in the script is created and stored in the attribute root of the class. Other attributes store relevant information about the structure of the CFG. Finally the method plot_edges, is used to print the edges of the CFG for sebugging purposes.

# The function produce_cfg is invoked on a .txt file containing the valid script of a SOGA program. It uses the libraries SOGALexer and SOGAParser (automatically generated using ANTLR4) to create the parse tree of the program and subsequently explores it recursively using the customized CFG listener. Returns the CFG object generated from the program script.

# TO DO:
# - add controls on set_expr and set_cond
# - instead of storing strings parse assignment instructions, LBC and observe conditions according to suitably defined grammars
# - add instruction to convert uniform (and possibly other distributions) to GMs

from antlr4 import *
from SOGALexer import *
from SOGAParser import *
from SOGAListener import *

class CFGnode:
    
    def __init__(self, node_name, node_type):
        self.name = node_name
        self.type = node_type
        self.parent = []
        self.children = []
        
class EntryNode(CFGnode):
    
    def __init__(self, node_name):
        super().__init__(node_name, 'entry')
        
    def __str__(self):
        return 'EntryNode<>'
    
    def __repr__(self):
        return str(self)
        
class StateNode(CFGnode):
    
    def __init__(self, node_name):
        super().__init__(node_name, 'state')
        self.expr = None
        self.cond = None
        
    def set_expr(self, expr):
        self.expr = expr
        
    def set_cond(self, cond):
        self.cond = cond
        
    def __str__(self):
        return 'StateNode<{},{},{}>'.format(self.name,self.cond,self.expr)
    
    def __repr__(self):
        return str(self)
        
class TestNode(CFGnode):
    
    def __init__(self, node_name):
        super().__init__(node_name, 'test')
        self.LBC = None
        
    def set_LBC(self, LBC):
        self.LBC = LBC
        
    def __str__(self):
        return 'TestNode<{},{}>'.format(self.name,self.LBC)
    
    def __repr__(self):
        return str(self)
        
class ObserveNode(CFGnode):
    
    def __init__(self, node_name):
        super().__init__(node_name, 'observe')
        self.LBC = None
        
    def set_LBC(self, LBC):
        self.LBC = LBC
        
    def __str__(self):
        return 'ObserveNode<{},{}>'.format(self.name,self.LBC)
  
    def __repr__(self):
        return str(self)
    
class MergeNode(CFGnode):
    
    def __init__(self, node_name):
        super().__init__(node_name, 'merge')
        self.list_dist = []
        
    def __str__(self):
        return 'MergeNode<{}>'.format(self.name)
    
    def __repr__(self):
        return str(self)
    
class ExitNode(CFGnode):
    
    def __init__(self, node_name):
        super().__init__(node_name, 'exit')
        self.list_dist = []
        
    def __str__(self):
        return 'ExitNode<>'
    
    def __repr__(self):
        return str(self)

    
class CFG(SOGAListener):
    
    def __init__(self):
        # counters for nodes of different types
        self.n_state = 0
        self.n_test = 0
        self.n_merge = 0
        self.n_observe = 0
        # root of the CFG
        self.root = EntryNode('entry')
        # dictionary keeping track of the nodes in CFG 
        self.node_list = {}
        self.ID_list = []
        # hidden variables used in the construction of the CFG
        self._current_node = self.root
        self._flag = None
        self._subroot = []
        
    def enterAssignment(self, ctx):
        """ When an Assignment instruction is entered a new StateNode is added to the CFG, storing a string with the assignment instruction. Dependence from a TestNode, encoded in the variable _flag, is checked to initialize the attribute cond."""
        node = StateNode('state{}'.format(self.n_state))
        self.n_state += 1
        if self._flag is not None:
            node.cond = self._flag
            self._flag = None
        node.expr = ctx.getText()
        node.parent.append(self._current_node)
        self._current_node.children.append(node)
        self._current_node = node
        self.node_list[node.name] = node

    def enterConditional(self, ctx):
        """ When a Conditional statement is entered a new TestNode is added to the CFG and to the stack _subroot."""
        node = TestNode('test{}'.format(self.n_test))
        self.n_test += 1
        node.parent.append(self._current_node)
        self._current_node.children.append(node)
        self._current_node = node
        self._subroot.append(self._current_node)
        self.node_list[node.name] = node

    def enterIfclause(self, ctx):
        """ When the Ifclause of a conditional statement is entered the LBC is stored as a string in the LBC attribute of the corresponding TestNode and _flag is set to True."""
        self._current_node.LBC = ctx.bexpr().getText()
        self._flag = True
        
    def exitIfclause(self, ctx):
        """ When the Ifclause of a conditional statement is exited the current_node is set to the last added subroot (pointing to the last created TestNode)."""
        self._current_node = self._subroot[-1]
        
    def enterElseclause(self, ctx):
        """ When the Elseclause of a conditional statement is entered _flag is set to False."""
        self._flag = False
        
    def exitElseclause(self, ctx):
        """ When the Elseclause of a conditional statement is exited the last added subroot is deleted from the stack."""
        self._current_node = self._subroot.pop()
        
    def enterObserve(self, ctx):
        """ When an Observe statement is entered an ObserveNode is added to the CFG, storing the LBC condition in the attribute LBC."""
        node = ObserveNode('observe{}'.format(self.n_observe))
        node.LBC = ctx.bexpr().getText()
        self.n_observe += 1
        node.parent.append(self._current_node)
        self._current_node.children.append(node)
        self._current_node = node
        self.node_list[node.name] = node
        
    def enterMerge(self, ctx):
        """ When a merge statement is entered a new MergeNode is added to the CFG."""
        node = MergeNode('merge{}'.format(self.n_merge))
        self.n_merge += 1
        node.parent = self.get_leaves(self._current_node, [])
        for parent in node.parent:
            parent.children.append(node)
        self._current_node = node
        self.node_list[node.name] = node
        
    def exitProgr(self, ctx):
        """ When the end of the program is reached an ExitNode is added to the CFG and all leaves are linked to it."""
        node = ExitNode('exit')
        node.parent = self.get_leaves(self._current_node, [])
        for parent in node.parent:
            parent.children.append(node)
        self._current_node = node
        self.node_list[node.name] = node
        
    def enterSymvars(self, ctx):
        """ Symbolic variables names encountered during the parsing are stored in the attribute list ID_list."""
        var = ctx.getText()
        if 'gm(' not in var and var not in self.ID_list:
                self.ID_list.append(var)
                             
    def get_leaves(self, node, leaves):
        """ Recursively finds all the leaves of the subtree starting in node."""
        if len(node.children) == 0:
            if node not in leaves:
                leaves.append(node)
            return leaves
        else:
            for child in node.children:
                leaves = self.get_leaves(child, leaves)
            return leaves     
    
    def plot_edges(self):
        """ Recursively plots all the edges of the tree."""
        def _plot_edges(node, edges = []):
            if len(node.children) == 0:
                return edges
            else:
                for child in node.children:
                    edge = '(' + node.name + ',' + child.name + ')'
                    if edge not in edges:
                        edges.append(edge)
                for child in node.children:
                    edges = _plot_edges(child, edges)
                return edges
            
        edges = _plot_edges(self.root)
        print(edges)
        
        
def produce_cfg(filename):
    """ Parses filename using ANTLR4. Returns a CFG object. """
    input_file =  open('../script/'+ filename + '.txt', 'r').read()
    lexer = SOGALexer(InputStream(input_file))
    stream = CommonTokenStream(lexer)
    parser = SOGAParser(stream)
    tree = parser.progr()
    cfg = CFG()
    walker = ParseTreeWalker()
    walker.walk(cfg, tree) 
    return cfg