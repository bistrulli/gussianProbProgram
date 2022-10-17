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
        