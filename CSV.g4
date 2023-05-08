grammar CSV;

file: row (END_ROW row)* END_ROW? EOF;
row: field (DELIMITER field)*;
field: TEXT | QUOTED_TEXT;
TEXT: ~[,;\t| \n\r]*
      (~[\n\r,] ~[,;\t| \n\r]*)*;
QUOTED_TEXT: '"' ( ~["\r\n] | '""' )* '"';
DELIMITER:
    ','
    | ';'
    | '|'
    | '\t'
    | ' ';
END_ROW: '\r'? '\n';
WHITESPACE: [ \t]+ -> skip;
