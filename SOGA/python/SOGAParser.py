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
        4,1,24,103,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,3,2,40,8,2,1,
        2,3,2,43,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,4,6,63,8,6,11,6,12,6,64,1,7,1,7,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,3,8,76,8,8,1,8,1,8,1,8,5,8,81,8,8,10,8,12,8,84,9,
        8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,98,
        8,10,10,10,12,10,101,9,10,1,10,0,2,16,20,11,0,2,4,6,8,10,12,14,16,
        18,20,0,2,1,0,12,13,1,0,14,18,103,0,27,1,0,0,0,2,33,1,0,0,0,4,42,
        1,0,0,0,6,44,1,0,0,0,8,48,1,0,0,0,10,54,1,0,0,0,12,62,1,0,0,0,14,
        66,1,0,0,0,16,75,1,0,0,0,18,85,1,0,0,0,20,89,1,0,0,0,22,23,3,2,1,
        0,23,24,5,1,0,0,24,26,1,0,0,0,25,22,1,0,0,0,26,29,1,0,0,0,27,25,
        1,0,0,0,27,28,1,0,0,0,28,1,1,0,0,0,29,27,1,0,0,0,30,34,3,4,2,0,31,
        34,3,6,3,0,32,34,3,14,7,0,33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,
        0,0,34,3,1,0,0,0,35,36,5,20,0,0,36,39,5,2,0,0,37,40,3,16,8,0,38,
        40,3,20,10,0,39,37,1,0,0,0,39,38,1,0,0,0,40,43,1,0,0,0,41,43,5,3,
        0,0,42,35,1,0,0,0,42,41,1,0,0,0,43,5,1,0,0,0,44,45,3,8,4,0,45,46,
        3,10,5,0,46,47,5,4,0,0,47,7,1,0,0,0,48,49,5,5,0,0,49,50,3,18,9,0,
        50,51,5,6,0,0,51,52,3,12,6,0,52,53,5,7,0,0,53,9,1,0,0,0,54,55,5,
        8,0,0,55,56,5,6,0,0,56,57,3,12,6,0,57,58,5,7,0,0,58,11,1,0,0,0,59,
        60,3,2,1,0,60,61,5,1,0,0,61,63,1,0,0,0,62,59,1,0,0,0,63,64,1,0,0,
        0,64,62,1,0,0,0,64,65,1,0,0,0,65,13,1,0,0,0,66,67,5,9,0,0,67,15,
        1,0,0,0,68,69,6,8,-1,0,69,76,5,10,0,0,70,76,5,20,0,0,71,76,5,21,
        0,0,72,73,5,21,0,0,73,74,5,11,0,0,74,76,3,16,8,2,75,68,1,0,0,0,75,
        70,1,0,0,0,75,71,1,0,0,0,75,72,1,0,0,0,76,82,1,0,0,0,77,78,10,1,
        0,0,78,79,7,0,0,0,79,81,3,16,8,2,80,77,1,0,0,0,81,84,1,0,0,0,82,
        80,1,0,0,0,82,83,1,0,0,0,83,17,1,0,0,0,84,82,1,0,0,0,85,86,3,16,
        8,0,86,87,7,1,0,0,87,88,5,21,0,0,88,19,1,0,0,0,89,90,6,10,-1,0,90,
        91,3,16,8,0,91,99,1,0,0,0,92,93,10,2,0,0,93,94,5,11,0,0,94,98,3,
        20,10,3,95,96,10,1,0,0,96,98,5,19,0,0,97,92,1,0,0,0,97,95,1,0,0,
        0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,21,1,0,0,0,101,
        99,1,0,0,0,9,27,33,39,42,64,75,82,97,99
    ]

class SOGAParser ( Parser ):

    grammarFileName = "SOGA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'skip'", "'end if'", "'if'", 
                     "'{'", "'}'", "'else'", "'merge'", "'norm'", "'*'", 
                     "'+'", "'-'", "'<'", "'<='", "'=='", "'>='", "'>'", 
                     "'^2'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUM", "COMM", "WS", "DIGIT" ]

    RULE_progr = 0
    RULE_instr = 1
    RULE_assignment = 2
    RULE_conditional = 3
    RULE_ifclause = 4
    RULE_elseclause = 5
    RULE_block = 6
    RULE_merge = 7
    RULE_lexpr = 8
    RULE_bexpr = 9
    RULE_expr = 10

    ruleNames =  [ "progr", "instr", "assignment", "conditional", "ifclause", 
                   "elseclause", "block", "merge", "lexpr", "bexpr", "expr" ]

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
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__2) | (1 << SOGAParser.T__4) | (1 << SOGAParser.T__8) | (1 << SOGAParser.ID))) != 0):
                self.state = 22
                self.instr()
                self.state = 23
                self.match(SOGAParser.T__0)
                self.state = 29
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

        def assignment(self):
            return self.getTypedRuleContext(SOGAParser.AssignmentContext,0)


        def conditional(self):
            return self.getTypedRuleContext(SOGAParser.ConditionalContext,0)


        def merge(self):
            return self.getTypedRuleContext(SOGAParser.MergeContext,0)


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
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.T__2, SOGAParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.assignment()
                pass
            elif token in [SOGAParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.conditional()
                pass
            elif token in [SOGAParser.T__8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.merge()
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


    class AssignmentContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return SOGAParser.RULE_assignment

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

        localctx = SOGAParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SOGAParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(SOGAParser.ID)
                self.state = 36
                self.match(SOGAParser.T__1)
                self.state = 39
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 37
                    self.lexpr(0)
                    pass

                elif la_ == 2:
                    self.state = 38
                    self.expr(0)
                    pass


                pass
            elif token in [SOGAParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(SOGAParser.T__2)
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


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifclause(self):
            return self.getTypedRuleContext(SOGAParser.IfclauseContext,0)


        def elseclause(self):
            return self.getTypedRuleContext(SOGAParser.ElseclauseContext,0)


        def getRuleIndex(self):
            return SOGAParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = SOGAParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.ifclause()
            self.state = 45
            self.elseclause()
            self.state = 46
            self.match(SOGAParser.T__3)
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
        self.enterRule(localctx, 8, self.RULE_ifclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(SOGAParser.T__4)
            self.state = 49
            self.bexpr()
            self.state = 50
            self.match(SOGAParser.T__5)
            self.state = 51
            self.block()
            self.state = 52
            self.match(SOGAParser.T__6)
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
        self.enterRule(localctx, 10, self.RULE_elseclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(SOGAParser.T__7)
            self.state = 55
            self.match(SOGAParser.T__5)
            self.state = 56
            self.block()
            self.state = 57
            self.match(SOGAParser.T__6)
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
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.instr()
                self.state = 60
                self.match(SOGAParser.T__0)
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__2) | (1 << SOGAParser.T__4) | (1 << SOGAParser.T__8) | (1 << SOGAParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MergeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SOGAParser.RULE_merge

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMerge" ):
                listener.enterMerge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMerge" ):
                listener.exitMerge(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMerge" ):
                return visitor.visitMerge(self)
            else:
                return visitor.visitChildren(self)




    def merge(self):

        localctx = SOGAParser.MergeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_merge)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(SOGAParser.T__8)
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_lexpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 69
                self.match(SOGAParser.T__9)
                pass

            elif la_ == 2:
                self.state = 70
                self.match(SOGAParser.ID)
                pass

            elif la_ == 3:
                self.state = 71
                self.match(SOGAParser.NUM)
                pass

            elif la_ == 4:
                self.state = 72
                self.match(SOGAParser.NUM)
                self.state = 73
                self.match(SOGAParser.T__10)
                self.state = 74
                self.lexpr(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SOGAParser.LexprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_lexpr)
                    self.state = 77
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 78
                    _la = self._input.LA(1)
                    if not(_la==SOGAParser.T__11 or _la==SOGAParser.T__12):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 79
                    self.lexpr(2) 
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_bexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.lexpr(0)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SOGAParser.T__13) | (1 << SOGAParser.T__14) | (1 << SOGAParser.T__15) | (1 << SOGAParser.T__16) | (1 << SOGAParser.T__17))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 87
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.lexpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 97
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = SOGAParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 92
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 93
                        self.match(SOGAParser.T__10)
                        self.state = 94
                        self.expr(3)
                        pass

                    elif la_ == 2:
                        localctx = SOGAParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 95
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 96
                        self.match(SOGAParser.T__18)
                        pass

             
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self._predicates[8] = self.lexpr_sempred
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def lexpr_sempred(self, localctx:LexprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




