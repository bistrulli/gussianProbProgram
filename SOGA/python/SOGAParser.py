# Generated from SOGA.g4 by ANTLR 4.10.1
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
        4,1,24,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,1,1,1,1,1,1,
        1,3,1,29,8,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,4,4,53,8,4,11,4,12,4,54,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,67,8,5,1,5,1,5,1,5,5,
        5,72,8,5,10,5,12,5,75,9,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,5,7,89,8,7,10,7,12,7,92,9,7,1,7,0,2,10,14,8,0,2,4,6,8,
        10,12,14,0,2,1,0,12,13,1,0,14,18,98,0,21,1,0,0,0,2,36,1,0,0,0,4,
        38,1,0,0,0,6,44,1,0,0,0,8,52,1,0,0,0,10,66,1,0,0,0,12,76,1,0,0,0,
        14,80,1,0,0,0,16,17,3,2,1,0,17,18,5,1,0,0,18,20,1,0,0,0,19,16,1,
        0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,
        21,1,0,0,0,24,25,5,20,0,0,25,28,5,2,0,0,26,29,3,10,5,0,27,29,3,14,
        7,0,28,26,1,0,0,0,28,27,1,0,0,0,29,37,1,0,0,0,30,31,3,4,2,0,31,32,
        3,6,3,0,32,33,5,3,0,0,33,37,1,0,0,0,34,37,5,4,0,0,35,37,5,5,0,0,
        36,24,1,0,0,0,36,30,1,0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,37,3,1,0,
        0,0,38,39,5,6,0,0,39,40,3,12,6,0,40,41,5,7,0,0,41,42,3,8,4,0,42,
        43,5,8,0,0,43,5,1,0,0,0,44,45,5,9,0,0,45,46,5,7,0,0,46,47,3,8,4,
        0,47,48,5,8,0,0,48,7,1,0,0,0,49,50,3,2,1,0,50,51,5,1,0,0,51,53,1,
        0,0,0,52,49,1,0,0,0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,
        9,1,0,0,0,56,57,6,5,-1,0,57,67,5,10,0,0,58,67,5,20,0,0,59,67,5,21,
        0,0,60,61,5,21,0,0,61,62,5,11,0,0,62,67,5,20,0,0,63,64,5,21,0,0,
        64,65,5,11,0,0,65,67,3,10,5,1,66,56,1,0,0,0,66,58,1,0,0,0,66,59,
        1,0,0,0,66,60,1,0,0,0,66,63,1,0,0,0,67,73,1,0,0,0,68,69,10,2,0,0,
        69,70,7,0,0,0,70,72,3,10,5,3,71,68,1,0,0,0,72,75,1,0,0,0,73,71,1,
        0,0,0,73,74,1,0,0,0,74,11,1,0,0,0,75,73,1,0,0,0,76,77,3,10,5,0,77,
        78,7,1,0,0,78,79,5,21,0,0,79,13,1,0,0,0,80,81,6,7,-1,0,81,82,3,10,
        5,0,82,90,1,0,0,0,83,84,10,2,0,0,84,85,5,11,0,0,85,89,3,14,7,3,86,
        87,10,1,0,0,87,89,5,19,0,0,88,83,1,0,0,0,88,86,1,0,0,0,89,92,1,0,
        0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,15,1,0,0,0,92,90,1,0,0,0,8,21,
        28,36,54,66,73,88,90
    ]

class SOGAParser ( Parser ):

    grammarFileName = "SOGA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'end if'", "'skip'", "'merge'", 
                     "'if'", "'{'", "'}'", "'else'", "'norm'", "'*'", "'+'", 
                     "'-'", "'<'", "'<='", "'=='", "'>='", "'>'", "'^2'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUM", "COMM", "WS", "DIGIT" ]

    RULE_progr = 0
    RULE_instr = 1
    RULE_ifclause = 2
    RULE_elseclause = 3
    RULE_block = 4
    RULE_lexpr = 5
    RULE_bexpr = 6
    RULE_expr = 7

    ruleNames =  [ "progr", "instr", "ifclause", "elseclause", "block", 
                   "lexpr", "bexpr", "expr" ]

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
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    ID=20
    NUM=21
    COMM=22
    WS=23
    DIGIT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.InstrContext)
            else:
                return self.getTypedRuleContext(SOGAParser.InstrContext,i)


        def getRuleIndex(self):
            return SOGAParser.RULE_progr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgr" ):
                listener.enterProgr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgr" ):
                listener.exitProgr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgr" ):
                return visitor.visitProgr(self)
            else:
                return visitor.visitChildren(self)




    def progr(self):

        localctx = SOGAParser.ProgrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_progr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__3) | (1 << SOGAParser.T__4) | (1 << SOGAParser.T__5) | (1 << SOGAParser.ID))) != 0):
                self.state = 16
                self.instr()
                self.state = 17
                self.match(SOGAParser.T__0)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SOGAParser.ID, 0)

        def lexpr(self):
            return self.getTypedRuleContext(SOGAParser.LexprContext,0)


        def expr(self):
            return self.getTypedRuleContext(SOGAParser.ExprContext,0)


        def ifclause(self):
            return self.getTypedRuleContext(SOGAParser.IfclauseContext,0)


        def elseclause(self):
            return self.getTypedRuleContext(SOGAParser.ElseclauseContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_instr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstr" ):
                listener.enterInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstr" ):
                listener.exitInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstr" ):
                return visitor.visitInstr(self)
            else:
                return visitor.visitChildren(self)




    def instr(self):

        localctx = SOGAParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instr)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(SOGAParser.ID)
                self.state = 25
                self.match(SOGAParser.T__1)
                self.state = 28
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 26
                    self.lexpr(0)
                    pass

                elif la_ == 2:
                    self.state = 27
                    self.expr(0)
                    pass


                pass
            elif token in [SOGAParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.ifclause()
                self.state = 31
                self.elseclause()
                self.state = 32
                self.match(SOGAParser.T__2)
                pass
            elif token in [SOGAParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.match(SOGAParser.T__3)
                pass
            elif token in [SOGAParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(SOGAParser.T__4)
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


    class IfclauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bexpr(self):
            return self.getTypedRuleContext(SOGAParser.BexprContext,0)


        def block(self):
            return self.getTypedRuleContext(SOGAParser.BlockContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_ifclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfclause" ):
                listener.enterIfclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfclause" ):
                listener.exitIfclause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfclause" ):
                return visitor.visitIfclause(self)
            else:
                return visitor.visitChildren(self)




    def ifclause(self):

        localctx = SOGAParser.IfclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(SOGAParser.T__5)
            self.state = 39
            self.bexpr()
            self.state = 40
            self.match(SOGAParser.T__6)
            self.state = 41
            self.block()
            self.state = 42
            self.match(SOGAParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseclauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(SOGAParser.BlockContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_elseclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseclause" ):
                listener.enterElseclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseclause" ):
                listener.exitElseclause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseclause" ):
                return visitor.visitElseclause(self)
            else:
                return visitor.visitChildren(self)




    def elseclause(self):

        localctx = SOGAParser.ElseclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_elseclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(SOGAParser.T__8)
            self.state = 45
            self.match(SOGAParser.T__6)
            self.state = 46
            self.block()
            self.state = 47
            self.match(SOGAParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.InstrContext)
            else:
                return self.getTypedRuleContext(SOGAParser.InstrContext,i)


        def getRuleIndex(self):
            return SOGAParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SOGAParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self.instr()
                self.state = 50
                self.match(SOGAParser.T__0)
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__3) | (1 << SOGAParser.T__4) | (1 << SOGAParser.T__5) | (1 << SOGAParser.ID))) != 0)):
                    break

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

        def ID(self):
            return self.getToken(SOGAParser.ID, 0)

        def NUM(self):
            return self.getToken(SOGAParser.NUM, 0)

        def lexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.LexprContext)
            else:
                return self.getTypedRuleContext(SOGAParser.LexprContext,i)


        def getRuleIndex(self):
            return SOGAParser.RULE_lexpr

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



    def lexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SOGAParser.LexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_lexpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 57
                self.match(SOGAParser.T__9)
                pass

            elif la_ == 2:
                self.state = 58
                self.match(SOGAParser.ID)
                pass

            elif la_ == 3:
                self.state = 59
                self.match(SOGAParser.NUM)
                pass

            elif la_ == 4:
                self.state = 60
                self.match(SOGAParser.NUM)
                self.state = 61
                self.match(SOGAParser.T__10)
                self.state = 62
                self.match(SOGAParser.ID)
                pass

            elif la_ == 5:
                self.state = 63
                self.match(SOGAParser.NUM)
                self.state = 64
                self.match(SOGAParser.T__10)
                self.state = 65
                self.lexpr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SOGAParser.LexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lexpr)
                    self.state = 68
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 69
                    _la = self._input.LA(1)
                    if not(_la==SOGAParser.T__11 or _la==SOGAParser.T__12):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 70
                    self.lexpr(3) 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexpr(self):
            return self.getTypedRuleContext(SOGAParser.LexprContext,0)


        def NUM(self):
            return self.getToken(SOGAParser.NUM, 0)

        def getRuleIndex(self):
            return SOGAParser.RULE_bexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBexpr" ):
                listener.enterBexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBexpr" ):
                listener.exitBexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBexpr" ):
                return visitor.visitBexpr(self)
            else:
                return visitor.visitChildren(self)




    def bexpr(self):

        localctx = SOGAParser.BexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.lexpr(0)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__13) | (1 << SOGAParser.T__14) | (1 << SOGAParser.T__15) | (1 << SOGAParser.T__16) | (1 << SOGAParser.T__17))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 78
            self.match(SOGAParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexpr(self):
            return self.getTypedRuleContext(SOGAParser.LexprContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SOGAParser.ExprContext)
            else:
                return self.getTypedRuleContext(SOGAParser.ExprContext,i)


        def getRuleIndex(self):
            return SOGAParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SOGAParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.lexpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 88
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = SOGAParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 84
                        self.match(SOGAParser.T__10)
                        self.state = 85
                        self.expr(3)
                        pass

                    elif la_ == 2:
                        localctx = SOGAParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 87
                        self.match(SOGAParser.T__18)
                        pass

             
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.lexpr_sempred
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def lexpr_sempred(self, localctx:LexprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




