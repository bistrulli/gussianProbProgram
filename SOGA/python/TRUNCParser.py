# Generated from TRUNC.g4 by ANTLR 4.10.1
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
        4,1,20,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        3,0,29,8,0,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,
        5,1,5,3,5,46,8,5,1,5,1,5,5,5,50,8,5,10,5,12,5,53,9,5,1,6,1,6,3,6,
        57,8,6,1,6,1,6,1,7,1,7,3,7,63,8,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,10,1,10,1,10,1,10,5,10,79,8,10,10,10,12,10,82,9,10,1,
        10,1,10,1,11,1,11,1,12,1,12,1,12,2,51,80,0,13,0,2,4,6,8,10,12,14,
        16,18,20,22,24,0,2,1,0,1,4,1,0,5,6,82,0,28,1,0,0,0,2,30,1,0,0,0,
        4,34,1,0,0,0,6,36,1,0,0,0,8,40,1,0,0,0,10,42,1,0,0,0,12,56,1,0,0,
        0,14,62,1,0,0,0,16,64,1,0,0,0,18,66,1,0,0,0,20,74,1,0,0,0,22,85,
        1,0,0,0,24,87,1,0,0,0,26,29,3,2,1,0,27,29,3,6,3,0,28,26,1,0,0,0,
        28,27,1,0,0,0,29,1,1,0,0,0,30,31,3,10,5,0,31,32,3,4,2,0,32,33,5,
        16,0,0,33,3,1,0,0,0,34,35,7,0,0,0,35,5,1,0,0,0,36,37,3,16,8,0,37,
        38,3,8,4,0,38,39,5,16,0,0,39,7,1,0,0,0,40,41,7,1,0,0,41,9,1,0,0,
        0,42,51,3,12,6,0,43,46,3,22,11,0,44,46,3,24,12,0,45,43,1,0,0,0,45,
        44,1,0,0,0,46,47,1,0,0,0,47,48,3,12,6,0,48,50,1,0,0,0,49,45,1,0,
        0,0,50,53,1,0,0,0,51,52,1,0,0,0,51,49,1,0,0,0,52,11,1,0,0,0,53,51,
        1,0,0,0,54,55,5,16,0,0,55,57,5,7,0,0,56,54,1,0,0,0,56,57,1,0,0,0,
        57,58,1,0,0,0,58,59,3,14,7,0,59,13,1,0,0,0,60,63,5,15,0,0,61,63,
        3,18,9,0,62,60,1,0,0,0,62,61,1,0,0,0,63,15,1,0,0,0,64,65,5,15,0,
        0,65,17,1,0,0,0,66,67,5,8,0,0,67,68,3,20,10,0,68,69,5,9,0,0,69,70,
        3,20,10,0,70,71,5,9,0,0,71,72,3,20,10,0,72,73,5,10,0,0,73,19,1,0,
        0,0,74,75,5,11,0,0,75,80,5,16,0,0,76,77,5,9,0,0,77,79,5,16,0,0,78,
        76,1,0,0,0,79,82,1,0,0,0,80,81,1,0,0,0,80,78,1,0,0,0,81,83,1,0,0,
        0,82,80,1,0,0,0,83,84,5,12,0,0,84,21,1,0,0,0,85,86,5,13,0,0,86,23,
        1,0,0,0,87,88,5,14,0,0,88,25,1,0,0,0,6,28,45,51,56,62,80
    ]

class TRUNCParser ( Parser ):

    grammarFileName = "TRUNC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<='", "'<'", "'>'", "'>='", "'=='", 
                     "'!='", "'*'", "'gm('", "','", "')'", "'['", "']'", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUM", 
                      "COMM", "WS", "ALPHA", "DIGIT" ]

    RULE_trunc = 0
    RULE_ineq = 1
    RULE_inop = 2
    RULE_eq = 3
    RULE_eqop = 4
    RULE_lexpr = 5
    RULE_monom = 6
    RULE_vars = 7
    RULE_symvars = 8
    RULE_gm = 9
    RULE_list = 10
    RULE_sum = 11
    RULE_sub = 12

    ruleNames =  [ "trunc", "ineq", "inop", "eq", "eqop", "lexpr", "monom", 
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
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    ID=15
    NUM=16
    COMM=17
    WS=18
    ALPHA=19
    DIGIT=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TruncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ineq(self):
            return self.getTypedRuleContext(TRUNCParser.IneqContext,0)


        def eq(self):
            return self.getTypedRuleContext(TRUNCParser.EqContext,0)


        def getRuleIndex(self):
            return TRUNCParser.RULE_trunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrunc" ):
                listener.enterTrunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrunc" ):
                listener.exitTrunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrunc" ):
                return visitor.visitTrunc(self)
            else:
                return visitor.visitChildren(self)




    def trunc(self):

        localctx = TRUNCParser.TruncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_trunc)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.ineq()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.eq()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IneqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexpr(self):
            return self.getTypedRuleContext(TRUNCParser.LexprContext,0)


        def inop(self):
            return self.getTypedRuleContext(TRUNCParser.InopContext,0)


        def NUM(self):
            return self.getToken(TRUNCParser.NUM, 0)

        def getRuleIndex(self):
            return TRUNCParser.RULE_ineq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIneq" ):
                listener.enterIneq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIneq" ):
                listener.exitIneq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIneq" ):
                return visitor.visitIneq(self)
            else:
                return visitor.visitChildren(self)




    def ineq(self):

        localctx = TRUNCParser.IneqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ineq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.lexpr()
            self.state = 31
            self.inop()
            self.state = 32
            self.match(TRUNCParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TRUNCParser.RULE_inop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInop" ):
                listener.enterInop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInop" ):
                listener.exitInop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInop" ):
                return visitor.visitInop(self)
            else:
                return visitor.visitChildren(self)




    def inop(self):

        localctx = TRUNCParser.InopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_inop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TRUNCParser.T__0) | (1 << TRUNCParser.T__1) | (1 << TRUNCParser.T__2) | (1 << TRUNCParser.T__3))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symvars(self):
            return self.getTypedRuleContext(TRUNCParser.SymvarsContext,0)


        def eqop(self):
            return self.getTypedRuleContext(TRUNCParser.EqopContext,0)


        def NUM(self):
            return self.getToken(TRUNCParser.NUM, 0)

        def getRuleIndex(self):
            return TRUNCParser.RULE_eq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq" ):
                listener.enterEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq" ):
                listener.exitEq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq" ):
                return visitor.visitEq(self)
            else:
                return visitor.visitChildren(self)




    def eq(self):

        localctx = TRUNCParser.EqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_eq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.symvars()
            self.state = 37
            self.eqop()
            self.state = 38
            self.match(TRUNCParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TRUNCParser.RULE_eqop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqop" ):
                listener.enterEqop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqop" ):
                listener.exitEqop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqop" ):
                return visitor.visitEqop(self)
            else:
                return visitor.visitChildren(self)




    def eqop(self):

        localctx = TRUNCParser.EqopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_eqop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not(_la==TRUNCParser.T__4 or _la==TRUNCParser.T__5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def monom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TRUNCParser.MonomContext)
            else:
                return self.getTypedRuleContext(TRUNCParser.MonomContext,i)


        def sum_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TRUNCParser.SumContext)
            else:
                return self.getTypedRuleContext(TRUNCParser.SumContext,i)


        def sub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TRUNCParser.SubContext)
            else:
                return self.getTypedRuleContext(TRUNCParser.SubContext,i)


        def getRuleIndex(self):
            return TRUNCParser.RULE_lexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexpr" ):
                listener.enterLexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexpr" ):
                listener.exitLexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexpr" ):
                return visitor.visitLexpr(self)
            else:
                return visitor.visitChildren(self)




    def lexpr(self):

        localctx = TRUNCParser.LexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.monom()
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 45
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [TRUNCParser.T__12]:
                        self.state = 43
                        self.sum_()
                        pass
                    elif token in [TRUNCParser.T__13]:
                        self.state = 44
                        self.sub()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 47
                    self.monom() 
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
            return self.getTypedRuleContext(TRUNCParser.VarsContext,0)


        def NUM(self):
            return self.getToken(TRUNCParser.NUM, 0)

        def getRuleIndex(self):
            return TRUNCParser.RULE_monom

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

        localctx = TRUNCParser.MonomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_monom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TRUNCParser.NUM:
                self.state = 54
                self.match(TRUNCParser.NUM)
                self.state = 55
                self.match(TRUNCParser.T__6)


            self.state = 58
            self.vars_()
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
            return self.getToken(TRUNCParser.ID, 0)

        def gm(self):
            return self.getTypedRuleContext(TRUNCParser.GmContext,0)


        def getRuleIndex(self):
            return TRUNCParser.RULE_vars

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

        localctx = TRUNCParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vars)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TRUNCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(TRUNCParser.ID)
                pass
            elif token in [TRUNCParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
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
            return self.getToken(TRUNCParser.ID, 0)

        def getRuleIndex(self):
            return TRUNCParser.RULE_symvars

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

        localctx = TRUNCParser.SymvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_symvars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(TRUNCParser.ID)
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
                return self.getTypedRuleContexts(TRUNCParser.ListContext)
            else:
                return self.getTypedRuleContext(TRUNCParser.ListContext,i)


        def getRuleIndex(self):
            return TRUNCParser.RULE_gm

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

        localctx = TRUNCParser.GmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_gm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(TRUNCParser.T__7)
            self.state = 67
            self.list_()
            self.state = 68
            self.match(TRUNCParser.T__8)
            self.state = 69
            self.list_()
            self.state = 70
            self.match(TRUNCParser.T__8)
            self.state = 71
            self.list_()
            self.state = 72
            self.match(TRUNCParser.T__9)
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
                return self.getTokens(TRUNCParser.NUM)
            else:
                return self.getToken(TRUNCParser.NUM, i)

        def getRuleIndex(self):
            return TRUNCParser.RULE_list

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

        localctx = TRUNCParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(TRUNCParser.T__10)
            self.state = 75
            self.match(TRUNCParser.NUM)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 76
                    self.match(TRUNCParser.T__8)
                    self.state = 77
                    self.match(TRUNCParser.NUM) 
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 83
            self.match(TRUNCParser.T__11)
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
            return TRUNCParser.RULE_sum

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

        localctx = TRUNCParser.SumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(TRUNCParser.T__12)
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
            return TRUNCParser.RULE_sub

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

        localctx = TRUNCParser.SubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(TRUNCParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





