# Generated from ASGMT.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ASGMTParser import ASGMTParser
else:
    from ASGMTParser import ASGMTParser

# This class defines a complete generic visitor for a parse tree produced by ASGMTParser.

class ASGMTVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ASGMTParser#assignment.
    def visitAssignment(self, ctx:ASGMTParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASGMTParser#const.
    def visitConst(self, ctx:ASGMTParser.ConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASGMTParser#add.
    def visitAdd(self, ctx:ASGMTParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASGMTParser#mul.
    def visitMul(self, ctx:ASGMTParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASGMTParser#pow.
    def visitPow(self, ctx:ASGMTParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASGMTParser#monom.
    def visitMonom(self, ctx:ASGMTParser.MonomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASGMTParser#vars.
    def visitVars(self, ctx:ASGMTParser.VarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASGMTParser#symvars.
    def visitSymvars(self, ctx:ASGMTParser.SymvarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASGMTParser#gm.
    def visitGm(self, ctx:ASGMTParser.GmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASGMTParser#list.
    def visitList(self, ctx:ASGMTParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASGMTParser#sum.
    def visitSum(self, ctx:ASGMTParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASGMTParser#sub.
    def visitSub(self, ctx:ASGMTParser.SubContext):
        return self.visitChildren(ctx)



del ASGMTParser