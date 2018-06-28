import sys
import io
from antlr4 import *
from JSONLexer import JSONLexer
from JSONParser import JSONParser
 
def traducir(json_text):
    input = InputStream(json_text)
    lexer = JSONLexer(input)
    stream = CommonTokenStream(lexer)
    parser = JSONParser(stream)
    tree = parser.json()
 
if __name__ == '__main__':
    # json = open('ejemplo.json').read()
    json = sys.stdin.read()
    traducir(json)
