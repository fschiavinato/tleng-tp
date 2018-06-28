grammar JSON;

@header {
def put(x):
    print(x, end = '')
}

json
   :  value[0] 
   ;

obj[level]
   : '{' members[$level] '}' {put('\n')} 
   | '{' '}' {put('{}')}
   ;

members[level]
   : pair[$level]
   | pair[$level] ',' members[$level]  
   ;

pair[level]
   : STRING {put($STRING.text)} ':' {put($STRING.text); put(':')} value[$level+1]
   ;

array[level]
   : {put('-')} '[' elements[$level+1] ']'
   | '[' ']'
   ;

elements[level]
   : value[$level]
   | value[$level] ',' elements[$level]
   ;

value[level]
   : STRING {put($STRING.text)}
   | NUMBER {put($NUMBER.text)}
   | obj[$level]
   | array[$level]
   | 'true' {put('true')}
   | 'false' {put('false')}
   | 'null' {put('null')}
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
