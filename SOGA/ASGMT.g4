grammar ASGMT; 

assignment: symvars '=' (const | add | mul | pow);

const: NUM ((sum|sub) NUM)*?;
add: monom ((sum|sub) monom)*?;
mul: (NUM '*')? vars '*' vars;
pow: vars '^2';

monom: (NUM '*')? vars | NUM;
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

fragment 
ALPHA : [a-zA-Z];
DIGIT : [0-9];