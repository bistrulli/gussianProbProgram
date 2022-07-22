# Generated from source_grammar.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .source_grammarParser import source_grammarParser
else:
    from source_grammarParser import source_grammarParser

# This class defines a complete listener for a parse tree produced by source_grammarParser.
class source_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by source_grammarParser#start.
    def enterStart(self, ctx:source_grammarParser.StartContext):
        pass

    # Exit a parse tree produced by source_grammarParser#start.
    def exitStart(self, ctx:source_grammarParser.StartContext):
        pass


    # Enter a parse tree produced by source_grammarParser#opExpr.
    def enterOpExpr(self, ctx:source_grammarParser.OpExprContext):
        pass

    # Exit a parse tree produced by source_grammarParser#opExpr.
    def exitOpExpr(self, ctx:source_grammarParser.OpExprContext):
        pass


    # Enter a parse tree produced by source_grammarParser#atomExpr.
    def enterAtomExpr(self, ctx:source_grammarParser.AtomExprContext):
        pass

    # Exit a parse tree produced by source_grammarParser#atomExpr.
    def exitAtomExpr(self, ctx:source_grammarParser.AtomExprContext):
        pass


    # Enter a parse tree produced by source_grammarParser#parenExpr.
    def enterParenExpr(self, ctx:source_grammarParser.ParenExprContext):
        pass

    # Exit a parse tree produced by source_grammarParser#parenExpr.
    def exitParenExpr(self, ctx:source_grammarParser.ParenExprContext):
        pass



del source_grammarParser