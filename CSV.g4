grammar CSV;

file: row (CRLF row)* CRLF? EOF;
row: field (DELIMITER field)*;
field: TEXT | QUOTED_TEXT;
TEXT: ~[,;\t| \r\n]*;
QUOTED_TEXT: '"' ( ~["\r\n] | '""' )* '"';
DELIMITER:
    ','
    | ';'
    | '|'
    | '\t'
    | ' ';
CRLF: '\r'? '\n';
WHITESPACE: [ \t]+ -> skip;
