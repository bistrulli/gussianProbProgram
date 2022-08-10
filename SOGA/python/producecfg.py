from antlr4 import *
from SOGALexer import *
from SOGAVisitor import *
from SOGAParser import *
from SOGAListener import *
from CFG import *

class mylistener(SOGAListener):
    
    def __init__(self):
        # counters for nodes of different types
        self.n_state = 0
        self.n_test = 0
        self.n_merge = 0
        # root of the CFG
        self.root = EntryNode('entry')
        # dictionary keeping track of the nodes in CFG 
        self.node_list = {}
        
        # hidden variables used in the construction of the CFG
        self._current_node = self.root
        self._flag = None
        self._subroot = []
        
    def enterAssignment(self, ctx):
        node = StateNode('state{}'.format(self.n_state))
        self.n_state += 1
        node.expr = ctx.getText()
        if self._flag is not None:
            node.cond = self._flag
            self._flag = None
        node.parent.append(self._current_node)
        self._current_node.children.append(node)
        self._current_node = node
        self.node_list[node.name] = node

    def enterConditional(self, ctx):
        node = TestNode('test{}'.format(self.n_test))
        self.n_test += 1
        node.parent.append(self._current_node)
        self._current_node.children.append(node)
        self._current_node = node
        self.node_list[node.name] = node

    def enterIfclause(self, ctx):
        self._current_node.LBC = ctx.bexpr().getText()
        self._flag = True
        self._subroot.append(self._current_node)
        
    def exitIfclause(self, ctx):
        self._current_node = self._subroot[-1]
        
    def enterElseclause(self, ctx):
        self._flag = False
        
    def exitElseclause(self, ctx):
        self._current_node = self._subroot.pop()
        
    def enterMerge(self, ctx):
        node = MergeNode('merge{}'.format(self.n_merge))
        self.n_merge += 1
        node.parent = self.get_leaves(self._current_node, [])
        for parent in node.parent:
            parent.children.append(node)
        self._current_node = node
        self.node_list[node.name] = node
        
    def exitProgr(self, ctx):
        node = ExitNode('exit')
        node.parent = self.get_leaves(self._current_node, [])
        for parent in node.parent:
            parent.children.append(node)
        self._current_node = node
        self.node_list[node.name] = node
        
    def get_leaves(self, node, leaves):
        if len(node.children) == 0:
            leaves.append(node)
            return leaves
        else:
            for child in node.children:
                leaves = self.get_leaves(child, leaves)
            return leaves     
    
    def plot_edges(self):
        
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
    input_file =  open('../script/'+ filename + '.txt', 'r').read()
    lexer = SOGALexer(InputStream(input_file))
    stream = CommonTokenStream(lexer)
    parser = SOGAParser(stream)
    tree = parser.progr()
    listener = mylistener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree) 
    return listener