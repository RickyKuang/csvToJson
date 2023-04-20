grammar CSV;

file: row (CRLF row)* CRLF? EOF;
row: field (',' field);
field: TEXT | QUOTED_TEXT;
TEXT: ~[,\n"]+;
QUOTED_TEXT: '"' ('""' | ~'"') '"';
CRLF: '\r'? '\n';
WS: [ \t]+ -> skip;
