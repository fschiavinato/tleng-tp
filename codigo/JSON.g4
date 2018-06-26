grammar JSON;
@header {
p = lambda x: print(x, end = '')
}

json
   :  value
   ;

obj
   : '{' pair (',' pair)* '}' {print('')} 
   | '{' '}' {p('{}')}
   ;

pair
   : STRING ':' {p($STRING.text); p(':')} value
   ;

array
   : {p('-')} '[' value (','{p('-')} value)* ']'
   | '[' ']'
   ;

value
   : STRING {p($STRING.text)}
   | NUMBER {p($NUMBER.text)}
   | obj
   | array
   | 'true'
   | 'false'
   | 'null'
   ;


STRING
   : '"' (ESC | SAFECODEPOINT)* '"' 
   ;


fragment ESC
   : '\\' (["\\/bfnrt] | UNICODE)
   ;
fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;
fragment HEX
   : [0-9a-fA-F]
   ;
fragment SAFECODEPOINT
   : ~ ["\\\u0000-\u001F]
   ;


NUMBER
   : '-'? INT ('.' [0-9] +)? EXP?
   ;


fragment INT
   : '0' | [1-9] [0-9]*
   ;

// no leading zeros

fragment EXP
   : [Ee] [+\-]? INT
   ;

// \- since - means "range" inside [...]

WS
   : [ \t\n\r] + -> skip
   ;
