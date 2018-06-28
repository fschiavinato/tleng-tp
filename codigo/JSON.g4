grammar JSON;

@header {
def putval(x):
    x = x.replace('\"', '')
    if ':' in x or '-' in x or '\\n' in x:
        x = '\"' + x + '\"'
    print(x, end = '')

def put(x):
    print(x, end = '')
}

json
   :  value[0] 
   ;

obj[level]
   : '{' members[$level] '}' 
   ;

emptyobj
   : '{' '}' {put('{}')}
   ;

members[level] returns [claves]
   : {put(level * '  ')} pair[$level]
   | {put(level * '  ')} pair[$level] {put('\n')} ',' members[$level]  
   ;

pair[level]
   : STRING ':' {putval($STRING.text); put(': ')} simplevalue[$level+1]
   | STRING ':' {putval($STRING.text); put(':\n')} compoundvalue[$level+1]
   ;

array[level]
   : '[' elements[$level] ']'
   ;

emptyarray
   : '[' ']' {put('[]')}
   ;

elements[level]
   : {put(level * '  ' + '- ')} simplevalue[$level + 1] 
   | {put(level * '  ' + '- \n')} compoundvalue[$level + 1] 
   | {put(level * '  ' + '- ')} simplevalue[$level + 1] {put('\n')}  ',' elements[$level]
   | {put(level * '  ' + '- \n')} compoundvalue[$level + 1] {put('\n')}  ',' elements[$level]
   ;

simplevalue[level]
   : STRING {putval($STRING.text)}
   | NUMBER {putval($NUMBER.text)}
   | 'true' {put('true')}
   | 'false' {put('false')}
   | 'null' 
   | emptyobj
   | emptyarray
   ;

compoundvalue[level]
   : obj[$level]
   | array[$level]
   ;

value[level] 
   : compoundvalue[level]
   | simplevalue[level]
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
