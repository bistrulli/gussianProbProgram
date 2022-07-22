from antlr4 import *
from parser import source_grammarLexer
from parser import source_grammarVisitor
from parser import source_grammarParser
import sys
from pprint import pprint


##  grammar arithmetic;
##  
##  start : expr ;
##  
##  expr  : left=expr op=('*'|'/') right=expr #opExpr
##        | left=expr op=('+'|'-') right=expr #opExpr
##        | '(' expr ')'                      #parenExpr
##        | atom=INT                          #atomExpr
##        ;
##  
##  INT   : ('0'..'9')+ ;
##  
##  WS    : [ \t\r\n]+ -> skip ;

import codecs
import sys

class EvalVisitor(source_grammarVisitor):
    
    def visitOpExpr(self, ctx):

        #print("visitOpExpr",ctx.getText())

        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text;

        # for attr in dir(ctx.op): ########### BEST 
        #   print("ctx.op.%s = %r" % (attr, getattr(ctx.op, attr)))
        #print("visitOpExpr",dir(ctx.op),left,right)

        opchar1=op[0]
        if opchar1 == '*':
            val = left * right 
        elif opchar1 == '/':
            val = left / right 
        elif opchar1 == '+':
            val = left + right 
        elif opchar1 == '-':
            val = left - right
        else:
            raise ValueError("Unknown operator " + op) 
        print("visitOpExpr",opchar1,left,right,val)
        return val 

    def visitStart(self, ctx):
        print("visitStart",ctx.getText())
        return self.visit(ctx.expr())

    def visitAtomExpr(self, ctx):
        print("visitAtomExpr",int(ctx.getText()))
        return int(ctx.getText())

    def visitParenExpr(self, ctx):
        print("visitParenExpr",ctx.getText())
        return self.visit(ctx.expr())

def main():
    #lexer = arithmeticLexer(StdinStream())
    #expression = "(( 4 - 10 ) * ( 3 + 4 )) / (( 2 - 5 ) * ( 3 + 4 ))"
    expression="(1-1)*3"
    lexer = source_grammarLexer(InputStream(expression))
    stream = CommonTokenStream(lexer)
    parser = source_grammarParser(stream)
    tree = parser.start()
    answer = EvalVisitor().visit(tree) 
    print(answer)

if __name__ == '__main__':
    main()