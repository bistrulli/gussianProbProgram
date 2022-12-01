# Generated from ASGMT.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,1,
        0,1,0,3,0,31,8,0,1,1,1,1,1,1,3,1,36,8,1,1,1,1,1,5,1,40,8,1,10,1,
        12,1,43,9,1,1,2,1,2,1,2,3,2,48,8,2,1,2,1,2,5,2,52,8,2,10,2,12,2,
        55,9,2,1,3,1,3,3,3,59,8,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,3,
        5,70,8,5,1,5,1,5,3,5,74,8,5,1,6,1,6,3,6,78,8,6,1,7,1,7,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,94,8,9,10,9,12,9,97,9,
        9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,3,41,53,95,0,12,0,2,4,6,8,10,
        12,14,16,18,20,22,0,0,104,0,24,1,0,0,0,2,32,1,0,0,0,4,44,1,0,0,0,
        6,58,1,0,0,0,8,64,1,0,0,0,10,73,1,0,0,0,12,77,1,0,0,0,14,79,1,0,
        0,0,16,81,1,0,0,0,18,89,1,0,0,0,20,100,1,0,0,0,22,102,1,0,0,0,24,
        25,3,14,7,0,25,30,5,1,0,0,26,31,3,2,1,0,27,31,3,4,2,0,28,31,3,6,
        3,0,29,31,3,8,4,0,30,26,1,0,0,0,30,27,1,0,0,0,30,28,1,0,0,0,30,29,
        1,0,0,0,31,1,1,0,0,0,32,41,5,12,0,0,33,36,3,20,10,0,34,36,3,22,11,
        0,35,33,1,0,0,0,35,34,1,0,0,0,36,37,1,0,0,0,37,38,5,12,0,0,38,40,
        1,0,0,0,39,35,1,0,0,0,40,43,1,0,0,0,41,42,1,0,0,0,41,39,1,0,0,0,
        42,3,1,0,0,0,43,41,1,0,0,0,44,53,3,10,5,0,45,48,3,20,10,0,46,48,
        3,22,11,0,47,45,1,0,0,0,47,46,1,0,0,0,48,49,1,0,0,0,49,50,3,10,5,
        0,50,52,1,0,0,0,51,47,1,0,0,0,52,55,1,0,0,0,53,54,1,0,0,0,53,51,
        1,0,0,0,54,5,1,0,0,0,55,53,1,0,0,0,56,57,5,12,0,0,57,59,5,2,0,0,
        58,56,1,0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,61,3,12,6,0,61,62,5,
        2,0,0,62,63,3,12,6,0,63,7,1,0,0,0,64,65,3,12,6,0,65,66,5,3,0,0,66,
        9,1,0,0,0,67,68,5,12,0,0,68,70,5,2,0,0,69,67,1,0,0,0,69,70,1,0,0,
        0,70,71,1,0,0,0,71,74,3,12,6,0,72,74,5,12,0,0,73,69,1,0,0,0,73,72,
        1,0,0,0,74,11,1,0,0,0,75,78,5,11,0,0,76,78,3,16,8,0,77,75,1,0,0,
        0,77,76,1,0,0,0,78,13,1,0,0,0,79,80,5,11,0,0,80,15,1,0,0,0,81,82,
        5,4,0,0,82,83,3,18,9,0,83,84,5,5,0,0,84,85,3,18,9,0,85,86,5,5,0,
        0,86,87,3,18,9,0,87,88,5,6,0,0,88,17,1,0,0,0,89,90,5,7,0,0,90,95,
        5,12,0,0,91,92,5,5,0,0,92,94,5,12,0,0,93,91,1,0,0,0,94,97,1,0,0,
        0,95,96,1,0,0,0,95,93,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,99,
        5,8,0,0,99,19,1,0,0,0,100,101,5,9,0,0,101,21,1,0,0,0,102,103,5,10,
        0,0,103,23,1,0,0,0,10,30,35,41,47,53,58,69,73,77,95
    ]

class ASGMTParser ( Parser ):

    grammarFileName = "ASGMT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'*'", "'^2'", "'gm('", "','", 
                     "')'", "'['", "']'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUM", 
                      "COMM", "WS", "DIGIT" ]

    RULE_assignment = 0
    RULE_const = 1
    RULE_add = 2
    RULE_mul = 3
    RULE_pow = 4
    RULE_monom = 5
    RULE_vars = 6
    RULE_symvars = 7
    RULE_gm = 8
    RULE_list = 9
    RULE_sum = 10
    RULE_sub = 11

    ruleNames =  [ "assignment", "const", "add", "mul", "pow", "monom", 
                   "vars", "symvars", "gm", "list", "sum", "sub" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ID=11
    NUM=12
    COMM=13
    WS=14
    DIGIT=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symvars(self):
            return self.getTypedRuleContext(ASGMTParser.SymvarsContext,0)


        def const(self):
            return self.getTypedRuleContext(ASGMTParser.ConstContext,0)


        def add(self):
            return self.getTypedRuleContext(ASGMTParser.AddContext,0)


        def mul(self):
            return self.getTypedRuleContext(ASGMTParser.MulContext,0)


        def pow_(self):
            return self.getTypedRuleContext(ASGMTParser.PowContext,0)


        def getRuleIndex(self):
            return ASGMTParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ASGMTParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.symvars()
            self.state = 25
            self.match(ASGMTParser.T__0)
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 26
                self.const()
                pass

            elif la_ == 2:
                self.state = 27
                self.add()
                pass

            elif la_ == 3:
                self.state = 28
                self.mul()
                pass

            elif la_ == 4:
                self.state = 29
                self.pow_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ASGMTParser.NUM)
            else:
                return self.getToken(ASGMTParser.NUM, i)

        def sum_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASGMTParser.SumContext)
            else:
                return self.getTypedRuleContext(ASGMTParser.SumContext,i)


        def sub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASGMTParser.SubContext)
            else:
                return self.getTypedRuleContext(ASGMTParser.SubContext,i)


        def getRuleIndex(self):
            return ASGMTParser.RULE_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst" ):
                listener.enterConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst" ):
                listener.exitConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst" ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)




    def const(self):

        localctx = ASGMTParser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(ASGMTParser.NUM)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 35
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ASGMTParser.T__8]:
                        self.state = 33
                        self.sum_()
                        pass
                    elif token in [ASGMTParser.T__9]:
                        self.state = 34
                        self.sub()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 37
                    self.match(ASGMTParser.NUM) 
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def monom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASGMTParser.MonomContext)
            else:
                return self.getTypedRuleContext(ASGMTParser.MonomContext,i)


        def sum_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASGMTParser.SumContext)
            else:
                return self.getTypedRuleContext(ASGMTParser.SumContext,i)


        def sub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASGMTParser.SubContext)
            else:
                return self.getTypedRuleContext(ASGMTParser.SubContext,i)


        def getRuleIndex(self):
            return ASGMTParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)




    def add(self):

        localctx = ASGMTParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.monom()
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 47
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ASGMTParser.T__8]:
                        self.state = 45
                        self.sum_()
                        pass
                    elif token in [ASGMTParser.T__9]:
                        self.state = 46
                        self.sub()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 49
                    self.monom() 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASGMTParser.VarsContext)
            else:
                return self.getTypedRuleContext(ASGMTParser.VarsContext,i)


        def NUM(self):
            return self.getToken(ASGMTParser.NUM, 0)

        def getRuleIndex(self):
            return ASGMTParser.RULE_mul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)




    def mul(self):

        localctx = ASGMTParser.MulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mul)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ASGMTParser.NUM:
                self.state = 56
                self.match(ASGMTParser.NUM)
                self.state = 57
                self.match(ASGMTParser.T__1)


            self.state = 60
            self.vars_()
            self.state = 61
            self.match(ASGMTParser.T__1)
            self.state = 62
            self.vars_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self):
            return self.getTypedRuleContext(ASGMTParser.VarsContext,0)


        def getRuleIndex(self):
            return ASGMTParser.RULE_pow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow" ):
                listener.enterPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow" ):
                listener.exitPow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow" ):
                return visitor.visitPow(self)
            else:
                return visitor.visitChildren(self)




    def pow_(self):

        localctx = ASGMTParser.PowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.vars_()
            self.state = 65
            self.match(ASGMTParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MonomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_(self):
            return self.getTypedRuleContext(ASGMTParser.VarsContext,0)


        def NUM(self):
            return self.getToken(ASGMTParser.NUM, 0)

        def getRuleIndex(self):
            return ASGMTParser.RULE_monom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMonom" ):
                listener.enterMonom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMonom" ):
                listener.exitMonom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMonom" ):
                return visitor.visitMonom(self)
            else:
                return visitor.visitChildren(self)




    def monom(self):

        localctx = ASGMTParser.MonomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_monom)
        self._la = 0 # Token type
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ASGMTParser.NUM:
                    self.state = 67
                    self.match(ASGMTParser.NUM)
                    self.state = 68
                    self.match(ASGMTParser.T__1)


                self.state = 71
                self.vars_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(ASGMTParser.NUM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ASGMTParser.ID, 0)

        def gm(self):
            return self.getTypedRuleContext(ASGMTParser.GmContext,0)


        def getRuleIndex(self):
            return ASGMTParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars" ):
                return visitor.visitVars(self)
            else:
                return visitor.visitChildren(self)




    def vars_(self):

        localctx = ASGMTParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vars)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ASGMTParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(ASGMTParser.ID)
                pass
            elif token in [ASGMTParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.gm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymvarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ASGMTParser.ID, 0)

        def getRuleIndex(self):
            return ASGMTParser.RULE_symvars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymvars" ):
                listener.enterSymvars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymvars" ):
                listener.exitSymvars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymvars" ):
                return visitor.visitSymvars(self)
            else:
                return visitor.visitChildren(self)




    def symvars(self):

        localctx = ASGMTParser.SymvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_symvars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(ASGMTParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASGMTParser.ListContext)
            else:
                return self.getTypedRuleContext(ASGMTParser.ListContext,i)


        def getRuleIndex(self):
            return ASGMTParser.RULE_gm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGm" ):
                listener.enterGm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGm" ):
                listener.exitGm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGm" ):
                return visitor.visitGm(self)
            else:
                return visitor.visitChildren(self)




    def gm(self):

        localctx = ASGMTParser.GmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_gm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(ASGMTParser.T__3)
            self.state = 82
            self.list_()
            self.state = 83
            self.match(ASGMTParser.T__4)
            self.state = 84
            self.list_()
            self.state = 85
            self.match(ASGMTParser.T__4)
            self.state = 86
            self.list_()
            self.state = 87
            self.match(ASGMTParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ASGMTParser.NUM)
            else:
                return self.getToken(ASGMTParser.NUM, i)

        def getRuleIndex(self):
            return ASGMTParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = ASGMTParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(ASGMTParser.T__6)
            self.state = 90
            self.match(ASGMTParser.NUM)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 91
                    self.match(ASGMTParser.T__4)
                    self.state = 92
                    self.match(ASGMTParser.NUM) 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 98
            self.match(ASGMTParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ASGMTParser.RULE_sum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum" ):
                listener.enterSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum" ):
                listener.exitSum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum" ):
                return visitor.visitSum(self)
            else:
                return visitor.visitChildren(self)




    def sum_(self):

        localctx = ASGMTParser.SumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ASGMTParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ASGMTParser.RULE_sub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)




    def sub(self):

        localctx = ASGMTParser.SubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(ASGMTParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





