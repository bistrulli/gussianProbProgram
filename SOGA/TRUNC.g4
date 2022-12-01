grammar TRUNC; 

trunc: ineq | eq;

ineq: lexpr inop NUM;
inop: '<=' | '<' | '>' | '>=';

eq: symvars eqop NUM;
eqop: '==' | '!=';

lexpr: monom ((sum|sub) monom)*?;
monom: (NUM '*')? vars;
vars: ID | gm;
symvars : ID;
gm: 'gm(' list ',' list ',' list ')';
list: '[' NUM (',' NUM)*? ']';

sum: '+';
sub: '-';

ID : ALPHA (ALPHA|DIGIT)*;
NUM : '-'? DIGIT+ ('.' DIGIT*)?; 

COMM : '/*' .*? '*/' -> skip;
WS : (' '|'\t'|'\r'|'\n') -> skip;
 
ALPHA : [a-zA-Z];
DIGIT : [0-9];