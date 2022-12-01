# Generated from ASGMT.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ASGMTParser import ASGMTParser
else:
    from ASGMTParser import ASGMTParser

# This class defines a complete listener for a parse tree produced by ASGMTParser.
class ASGMTListener(ParseTreeListener):

    # Enter a parse tree produced by ASGMTParser#assignment.
    def enterAssignment(self, ctx:ASGMTParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ASGMTParser#assignment.
    def exitAssignment(self, ctx:ASGMTParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ASGMTParser#const.
    def enterConst(self, ctx:ASGMTParser.ConstContext):
        pass

    # Exit a parse tree produced by ASGMTParser#const.
    def exitConst(self, ctx:ASGMTParser.ConstContext):
        pass


    # Enter a parse tree produced by ASGMTParser#add.
    def enterAdd(self, ctx:ASGMTParser.AddContext):
        pass

    # Exit a parse tree produced by ASGMTParser#add.
    def exitAdd(self, ctx:ASGMTParser.AddContext):
        pass


    # Enter a parse tree produced by ASGMTParser#mul.
    def enterMul(self, ctx:ASGMTParser.MulContext):
        pass

    # Exit a parse tree produced by ASGMTParser#mul.
    def exitMul(self, ctx:ASGMTParser.MulContext):
        pass


    # Enter a parse tree produced by ASGMTParser#pow.
    def enterPow(self, ctx:ASGMTParser.PowContext):
        pass

    # Exit a parse tree produced by ASGMTParser#pow.
    def exitPow(self, ctx:ASGMTParser.PowContext):
        pass


    # Enter a parse tree produced by ASGMTParser#monom.
    def enterMonom(self, ctx:ASGMTParser.MonomContext):
        pass

    # Exit a parse tree produced by ASGMTParser#monom.
    def exitMonom(self, ctx:ASGMTParser.MonomContext):
        pass


    # Enter a parse tree produced by ASGMTParser#vars.
    def enterVars(self, ctx:ASGMTParser.VarsContext):
        pass

    # Exit a parse tree produced by ASGMTParser#vars.
    def exitVars(self, ctx:ASGMTParser.VarsContext):
        pass


    # Enter a parse tree produced by ASGMTParser#symvars.
    def enterSymvars(self, ctx:ASGMTParser.SymvarsContext):
        pass

    # Exit a parse tree produced by ASGMTParser#symvars.
    def exitSymvars(self, ctx:ASGMTParser.SymvarsContext):
        pass


    # Enter a parse tree produced by ASGMTParser#gm.
    def enterGm(self, ctx:ASGMTParser.GmContext):
        pass

    # Exit a parse tree produced by ASGMTParser#gm.
    def exitGm(self, ctx:ASGMTParser.GmContext):
        pass


    # Enter a parse tree produced by ASGMTParser#list.
    def enterList(self, ctx:ASGMTParser.ListContext):
        pass

    # Exit a parse tree produced by ASGMTParser#list.
    def exitList(self, ctx:ASGMTParser.ListContext):
        pass


    # Enter a parse tree produced by ASGMTParser#sum.
    def enterSum(self, ctx:ASGMTParser.SumContext):
        pass

    # Exit a parse tree produced by ASGMTParser#sum.
    def exitSum(self, ctx:ASGMTParser.SumContext):
        pass


    # Enter a parse tree produced by ASGMTParser#sub.
    def enterSub(self, ctx:ASGMTParser.SubContext):
        pass

    # Exit a parse tree produced by ASGMTParser#sub.
    def exitSub(self, ctx:ASGMTParser.SubContext):
        pass



del ASGMTParser