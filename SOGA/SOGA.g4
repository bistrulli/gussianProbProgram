grammar SOGA; 

progr : (instr ';')*;

instr : assignment | conditional | merge;

assignment: ID '=' (lexpr|expr) | 'skip';

conditional: ifclause elseclause 'end if';
ifclause : 'if' bexpr '{' block '}';
elseclause : 'else' '{' block '}';
block : (instr ';')+;

merge : 'merge';

lexpr : 'norm' | ID | NUM | NUM '*' lexpr | lexpr ('+'|'-') lexpr;
bexpr : lexpr ('<'|'<='|'=='|'>='|'>') NUM;
expr : lexpr | expr '*' expr | expr '^2';

ID : ALPHA (ALPHA|DIGIT)*;
NUM : DIGIT+ ('.' DIGIT*)?;

COMM : '/*' .*? '*/' -> skip;
WS : (' '|'\t'|'\r'|'\n') -> skip;

fragment 
ALPHA : [a-zA-Z];
DIGIT : [0-9];