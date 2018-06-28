grammar JSON;

@header {
def p(x):
    print(x, end = '')
}

json
   :  {$value.level = 0} value 
   ;

obj[level]
   : '{' {$members.level = $level} members '}' {p('\n')} 
   | '{' '}' {p('{}')}
   ;

members[level]
   : pair
   | pair ',' members  
   ;

pair[level]
   : STRING {p($STRING.text)} ':' {p($STRING.text); p(':'); $value.level = $level + 1} value
   ;

array[level]
   : {p('-')} '[' elements ']' {$elements.level = $level}
   | '[' ']'
   ;

elements[level]
   : value
   | value ',' elements
   ;

value[level]
   : STRING {p($STRING.text)}
   | NUMBER {p($NUMBER.text)}
   | obj
   | array
   | 'true' {p('true')}
   | 'false' {p('false')}
   | 'null' {p('null')}
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
