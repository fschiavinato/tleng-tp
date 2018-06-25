import sys
from antlr4 import *
from JSONLexer import JSONLexer
from JSONParser import JSONParser
 
def main(argv):
    input = sys.stdin.read()
    print('original:\n' + input)
    lexer = JSONLexer(input)
    stream = CommonTokenStream(lexer)
    parser = JSONParser(stream)
    tree = parser.obj()
 
if __name__ == '__main__':
    main(sys.argv)
