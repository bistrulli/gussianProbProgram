# Generated from SOGA.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SOGAParser import SOGAParser
else:
    from SOGAParser import SOGAParser

# This class defines a complete generic visitor for a parse tree produced by SOGAParser.

class SOGAVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SOGAParser#progr.
    def visitProgr(self, ctx:SOGAParser.ProgrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SOGAParser#instr.
    def visitInstr(self, ctx:SOGAParser.InstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SOGAParser#assignment.
    def visitAssignment(self, ctx:SOGAParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SOGAParser#conditional.
    def visitConditional(self, ctx:SOGAParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SOGAParser#ifclause.
    def visitIfclause(self, ctx:SOGAParser.IfclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SOGAParser#elseclause.
    def visitElseclause(self, ctx:SOGAParser.ElseclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SOGAParser#block.
    def visitBlock(self, ctx:SOGAParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SOGAParser#merge.
    def visitMerge(self, ctx:SOGAParser.MergeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SOGAParser#lexpr.
    def visitLexpr(self, ctx:SOGAParser.LexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SOGAParser#bexpr.
    def visitBexpr(self, ctx:SOGAParser.BexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SOGAParser#expr.
    def visitExpr(self, ctx:SOGAParser.ExprContext):
        return self.visitChildren(ctx)



del SOGAParser