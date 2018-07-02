import sys
import io
from antlr4 import *
from JSONLexer import JSONLexer
from JSONParser import JSONParser
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener( ErrorListener ):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("\n" + str(line) + ":" + str(column) + ": Error de sintaxis: " + str(msg))
        sys.exit()

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print("\n" +"Error de ambigüedad: " + str(configs))
        sys.exit()

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print("\n" +"Error: " + str(configs))
        sys.exit()

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print("\n" +"Error de contexto: " + str(configs))
        sys.exit()


def traducir(json_text):
    input = InputStream(json_text)
    lexer = JSONLexer(input)
    stream = CommonTokenStream(lexer)
    parser = JSONParser(stream)
    parser._listeners = [ MyErrorListener() ]
    tree = parser.json()
 	
if __name__ == '__main__':
    # json = open('ejemplo.json').read()
    json = sys.stdin.read()
    traducir(json)

