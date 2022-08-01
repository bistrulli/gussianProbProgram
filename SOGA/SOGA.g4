grammar SOGA; 

progr : (instr ';')*;

instr : ID '=' (lexpr|expr) |
	  ifclause elseclause 'end if'|
	  'skip' | 'merge'; 

ifclause : 'if' bexpr '{' block '}';
elseclause : 'else' '{' block '}';
block : (instr ';')+;

lexpr : 'norm' | ID | NUM | NUM '*' ID | lexpr ('+'|'-') lexpr | NUM '*' lexpr;
bexpr : lexpr ('<'|'<='|'=='|'>='|'>') NUM;
expr : lexpr | expr '*' expr | expr '^2';

ID : ALPHA (ALPHA|DIGIT)*;
NUM : DIGIT+ ('.' DIGIT*)?;

COMM : '/*' .*? '*/' -> skip;
WS : (' '|'\t'|'\r'|'\n') -> skip;

fragment 
ALPHA : [a-zA-Z];
DIGIT : [0-9];