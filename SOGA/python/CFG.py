class CFGnode:
    
    def __init__(self, node_name, node_type):
        self.name = node_name
        self.type = node_type
        self.parent = []
        self.children = []
        
class EntryNode(CFGnode):
    
    def __init__(self, node_name):
        super().__init__(node_name, 'entry')
        
class StateNode(CFGnode):
    
    def __init__(self, node_name):
        super().__init__(node_name, 'state')
        self.expre = None
        self.cond = None
        
    def set_expr(self, expr):
        self.expr = expr
        
    def set_cond(self, cond):
        self.cond = cond
        
class TestNode(CFGnode):
    
    def __init__(self, node_name):
        super().__init__(node_name, 'test')
        self.LBC = None
        
    def set_LBC(self, LBC):
        self.LBC = LBC
        
class MergeNode(CFGnode):
    
    def __init__(self, node_name):
        super().__init__(node_name, 'merge')
        self.list_dist = []
        
class ExitNode(CFGnode):
    
    def __init__(self, node_name):
        super().__init__(node_name, 'exit')
        self.list_dist = []
        