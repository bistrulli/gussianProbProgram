# Generated from SOGA.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SOGAParser import SOGAParser
else:
    from SOGAParser import SOGAParser

# This class defines a complete listener for a parse tree produced by SOGAParser.
class SOGAListener(ParseTreeListener):

    # Enter a parse tree produced by SOGAParser#progr.
    def enterProgr(self, ctx:SOGAParser.ProgrContext):
        pass

    # Exit a parse tree produced by SOGAParser#progr.
    def exitProgr(self, ctx:SOGAParser.ProgrContext):
        pass


    # Enter a parse tree produced by SOGAParser#instr.
    def enterInstr(self, ctx:SOGAParser.InstrContext):
        pass

    # Exit a parse tree produced by SOGAParser#instr.
    def exitInstr(self, ctx:SOGAParser.InstrContext):
        pass


    # Enter a parse tree produced by SOGAParser#assignment.
    def enterAssignment(self, ctx:SOGAParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SOGAParser#assignment.
    def exitAssignment(self, ctx:SOGAParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SOGAParser#conditional.
    def enterConditional(self, ctx:SOGAParser.ConditionalContext):
        pass

    # Exit a parse tree produced by SOGAParser#conditional.
    def exitConditional(self, ctx:SOGAParser.ConditionalContext):
        pass


    # Enter a parse tree produced by SOGAParser#ifclause.
    def enterIfclause(self, ctx:SOGAParser.IfclauseContext):
        pass

    # Exit a parse tree produced by SOGAParser#ifclause.
    def exitIfclause(self, ctx:SOGAParser.IfclauseContext):
        pass


    # Enter a parse tree produced by SOGAParser#elseclause.
    def enterElseclause(self, ctx:SOGAParser.ElseclauseContext):
        pass

    # Exit a parse tree produced by SOGAParser#elseclause.
    def exitElseclause(self, ctx:SOGAParser.ElseclauseContext):
        pass


    # Enter a parse tree produced by SOGAParser#block.
    def enterBlock(self, ctx:SOGAParser.BlockContext):
        pass

    # Exit a parse tree produced by SOGAParser#block.
    def exitBlock(self, ctx:SOGAParser.BlockContext):
        pass


    # Enter a parse tree produced by SOGAParser#merge.
    def enterMerge(self, ctx:SOGAParser.MergeContext):
        pass

    # Exit a parse tree produced by SOGAParser#merge.
    def exitMerge(self, ctx:SOGAParser.MergeContext):
        pass


    # Enter a parse tree produced by SOGAParser#lexpr.
    def enterLexpr(self, ctx:SOGAParser.LexprContext):
        pass

    # Exit a parse tree produced by SOGAParser#lexpr.
    def exitLexpr(self, ctx:SOGAParser.LexprContext):
        pass


    # Enter a parse tree produced by SOGAParser#bexpr.
    def enterBexpr(self, ctx:SOGAParser.BexprContext):
        pass

    # Exit a parse tree produced by SOGAParser#bexpr.
    def exitBexpr(self, ctx:SOGAParser.BexprContext):
        pass


    # Enter a parse tree produced by SOGAParser#expr.
    def enterExpr(self, ctx:SOGAParser.ExprContext):
        pass

    # Exit a parse tree produced by SOGAParser#expr.
    def exitExpr(self, ctx:SOGAParser.ExprContext):
        pass



del SOGAParser