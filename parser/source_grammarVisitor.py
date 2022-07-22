# Generated from source_grammar.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .source_grammarParser import source_grammarParser
else:
    from source_grammarParser import source_grammarParser

# This class defines a complete generic visitor for a parse tree produced by source_grammarParser.

class source_grammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by source_grammarParser#start.
    def visitStart(self, ctx:source_grammarParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by source_grammarParser#opExpr.
    def visitOpExpr(self, ctx:source_grammarParser.OpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by source_grammarParser#atomExpr.
    def visitAtomExpr(self, ctx:source_grammarParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by source_grammarParser#parenExpr.
    def visitParenExpr(self, ctx:source_grammarParser.ParenExprContext):
        return self.visitChildren(ctx)



del source_grammarParser