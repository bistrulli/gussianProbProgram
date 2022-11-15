grammar SOGA; 

progr : (instr ';')*;

instr : assignment | conditional | merge | observe;

assignment: symvars '=' (lexpr|expr) | 'skip';

conditional: ifclause elseclause 'end if';
ifclause : 'if' bexpr '{' block '}';
elseclause : 'else' '{' block '}';
block : (instr ';')+;

merge : 'merge';

observe: 'observe(' bexpr ')';

lexpr : vars | NUM | NUM '*' lexpr | lexpr ('+'|'-') lexpr;
bexpr : lexpr ('<'|'<='|'>='|'>') NUM | ID ('=='|'!=') NUM;
expr : lexpr | (NUM '*')? vars '*' vars | vars '^2' ;

vars: ID | 'gm(' list ',' list ',' list ')';
symvars : ID;
list: '[' NUM (',' NUM)*? ']';

ID : ALPHA (ALPHA|DIGIT)*;
NUM : '-'? DIGIT+ ('.' DIGIT*)?;

COMM : '/*' .*? '*/' -> skip;
WS : (' '|'\t'|'\r'|'\n') -> skip;

fragment 
ALPHA : [a-zA-Z];
DIGIT : [0-9];