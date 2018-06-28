# Generated from JSON.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def putval(x):
    x = x.replace('\"', '')
    if ':' in x or '-' in x or '\\n' in x:
        x = '\"' + x + '\"'
    print(x, end = '')

def put(x):
    print(x, end = '')

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5+\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\65\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tO\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\\\n\n\3")
        buf.write("\13\3\13\5\13`\n\13\3\f\3\f\5\fd\n\f\3\f\2\2\r\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\2\2\2g\2\30\3\2\2\2\4\32\3\2\2\2\6")
        buf.write("\36\3\2\2\2\b*\3\2\2\2\n\64\3\2\2\2\f\66\3\2\2\2\16:\3")
        buf.write("\2\2\2\20N\3\2\2\2\22[\3\2\2\2\24_\3\2\2\2\26c\3\2\2\2")
        buf.write("\30\31\5\26\f\2\31\3\3\2\2\2\32\33\7\3\2\2\33\34\5\b\5")
        buf.write("\2\34\35\7\4\2\2\35\5\3\2\2\2\36\37\7\3\2\2\37 \7\4\2")
        buf.write("\2 !\b\4\1\2!\7\3\2\2\2\"#\b\5\1\2#+\5\n\6\2$%\b\5\1\2")
        buf.write("%&\5\n\6\2&\'\b\5\1\2\'(\7\5\2\2()\5\b\5\2)+\3\2\2\2*")
        buf.write("\"\3\2\2\2*$\3\2\2\2+\t\3\2\2\2,-\7\f\2\2-.\7\6\2\2./")
        buf.write("\b\6\1\2/\65\5\22\n\2\60\61\7\f\2\2\61\62\7\6\2\2\62\63")
        buf.write("\b\6\1\2\63\65\5\24\13\2\64,\3\2\2\2\64\60\3\2\2\2\65")
        buf.write("\13\3\2\2\2\66\67\7\7\2\2\678\5\20\t\289\7\b\2\29\r\3")
        buf.write("\2\2\2:;\7\7\2\2;<\7\b\2\2<=\b\b\1\2=\17\3\2\2\2>?\b\t")
        buf.write("\1\2?O\5\22\n\2@A\b\t\1\2AO\5\24\13\2BC\b\t\1\2CD\5\22")
        buf.write("\n\2DE\b\t\1\2EF\7\5\2\2FG\5\20\t\2GO\3\2\2\2HI\b\t\1")
        buf.write("\2IJ\5\24\13\2JK\b\t\1\2KL\7\5\2\2LM\5\20\t\2MO\3\2\2")
        buf.write("\2N>\3\2\2\2N@\3\2\2\2NB\3\2\2\2NH\3\2\2\2O\21\3\2\2\2")
        buf.write("PQ\7\f\2\2Q\\\b\n\1\2RS\7\r\2\2S\\\b\n\1\2TU\7\t\2\2U")
        buf.write("\\\b\n\1\2VW\7\n\2\2W\\\b\n\1\2X\\\7\13\2\2Y\\\5\6\4\2")
        buf.write("Z\\\5\16\b\2[P\3\2\2\2[R\3\2\2\2[T\3\2\2\2[V\3\2\2\2[")
        buf.write("X\3\2\2\2[Y\3\2\2\2[Z\3\2\2\2\\\23\3\2\2\2]`\5\4\3\2^")
        buf.write("`\5\f\7\2_]\3\2\2\2_^\3\2\2\2`\25\3\2\2\2ad\5\24\13\2")
        buf.write("bd\5\22\n\2ca\3\2\2\2cb\3\2\2\2d\27\3\2\2\2\b*\64N[_c")
        return buf.getvalue()


class JSONParser ( Parser ):

    grammarFileName = "JSON.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "','", "':'", "'['", "']'", 
                     "'true'", "'false'", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "NUMBER", "WS" ]

    RULE_json = 0
    RULE_obj = 1
    RULE_emptyobj = 2
    RULE_members = 3
    RULE_pair = 4
    RULE_array = 5
    RULE_emptyarray = 6
    RULE_elements = 7
    RULE_simplevalue = 8
    RULE_compoundvalue = 9
    RULE_value = 10

    ruleNames =  [ "json", "obj", "emptyobj", "members", "pair", "array", 
                   "emptyarray", "elements", "simplevalue", "compoundvalue", 
                   "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    STRING=10
    NUMBER=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class JsonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)




    def json(self):

        localctx = JSONParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.value(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, level=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.level = None
            self.level = level

        def members(self):
            return self.getTypedRuleContext(JSONParser.MembersContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_obj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObj" ):
                listener.enterObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObj" ):
                listener.exitObj(self)




    def obj(self, level):

        localctx = JSONParser.ObjContext(self, self._ctx, self.state, level)
        self.enterRule(localctx, 2, self.RULE_obj)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(JSONParser.T__0)
            self.state = 25
            self.members(localctx.level)
            self.state = 26
            self.match(JSONParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EmptyobjContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONParser.RULE_emptyobj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyobj" ):
                listener.enterEmptyobj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyobj" ):
                listener.exitEmptyobj(self)




    def emptyobj(self):

        localctx = JSONParser.EmptyobjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_emptyobj)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(JSONParser.T__0)
            self.state = 29
            self.match(JSONParser.T__1)
            put('{}')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MembersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, level=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.level = None
            self.claves = None
            self.level = level

        def pair(self):
            return self.getTypedRuleContext(JSONParser.PairContext,0)


        def members(self):
            return self.getTypedRuleContext(JSONParser.MembersContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_members

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMembers" ):
                listener.enterMembers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMembers" ):
                listener.exitMembers(self)




    def members(self, level):

        localctx = JSONParser.MembersContext(self, self._ctx, self.state, level)
        self.enterRule(localctx, 6, self.RULE_members)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                put(level * '  ')
                self.state = 33
                self.pair(localctx.level)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                put(level * '  ')
                self.state = 35
                self.pair(localctx.level)
                put('\n')
                self.state = 37
                self.match(JSONParser.T__2)
                self.state = 38
                self.members(localctx.level)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, level=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.level = None
            self._STRING = None # Token
            self.level = level

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def simplevalue(self):
            return self.getTypedRuleContext(JSONParser.SimplevalueContext,0)


        def compoundvalue(self):
            return self.getTypedRuleContext(JSONParser.CompoundvalueContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self, level):

        localctx = JSONParser.PairContext(self, self._ctx, self.state, level)
        self.enterRule(localctx, 8, self.RULE_pair)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                localctx._STRING = self.match(JSONParser.STRING)
                self.state = 43
                self.match(JSONParser.T__3)
                putval((None if localctx._STRING is None else localctx._STRING.text)); put(': ')
                self.state = 45
                self.simplevalue(localctx.level+1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                localctx._STRING = self.match(JSONParser.STRING)
                self.state = 47
                self.match(JSONParser.T__3)
                putval((None if localctx._STRING is None else localctx._STRING.text)); put(':\n')
                self.state = 49
                self.compoundvalue(localctx.level+1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, level=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.level = None
            self.level = level

        def elements(self):
            return self.getTypedRuleContext(JSONParser.ElementsContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self, level):

        localctx = JSONParser.ArrayContext(self, self._ctx, self.state, level)
        self.enterRule(localctx, 10, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(JSONParser.T__4)
            self.state = 53
            self.elements(localctx.level)
            self.state = 54
            self.match(JSONParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EmptyarrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONParser.RULE_emptyarray

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyarray" ):
                listener.enterEmptyarray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyarray" ):
                listener.exitEmptyarray(self)




    def emptyarray(self):

        localctx = JSONParser.EmptyarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_emptyarray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(JSONParser.T__4)
            self.state = 57
            self.match(JSONParser.T__5)
            put('[]')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, level=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.level = None
            self.level = level

        def simplevalue(self):
            return self.getTypedRuleContext(JSONParser.SimplevalueContext,0)


        def compoundvalue(self):
            return self.getTypedRuleContext(JSONParser.CompoundvalueContext,0)


        def elements(self):
            return self.getTypedRuleContext(JSONParser.ElementsContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElements" ):
                listener.enterElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElements" ):
                listener.exitElements(self)




    def elements(self, level):

        localctx = JSONParser.ElementsContext(self, self._ctx, self.state, level)
        self.enterRule(localctx, 14, self.RULE_elements)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                put(level * '  ' + '- ')
                self.state = 61
                self.simplevalue(localctx.level + 1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                put(level * '  ' + '- \n')
                self.state = 63
                self.compoundvalue(localctx.level + 1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                put(level * '  ' + '- ')
                self.state = 65
                self.simplevalue(localctx.level + 1)
                put('\n')
                self.state = 67
                self.match(JSONParser.T__2)
                self.state = 68
                self.elements(localctx.level)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                put(level * '  ' + '- \n')
                self.state = 71
                self.compoundvalue(localctx.level + 1)
                put('\n')
                self.state = 73
                self.match(JSONParser.T__2)
                self.state = 74
                self.elements(localctx.level)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimplevalueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, level=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.level = None
            self._STRING = None # Token
            self._NUMBER = None # Token
            self.level = level

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(JSONParser.NUMBER, 0)

        def emptyobj(self):
            return self.getTypedRuleContext(JSONParser.EmptyobjContext,0)


        def emptyarray(self):
            return self.getTypedRuleContext(JSONParser.EmptyarrayContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_simplevalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimplevalue" ):
                listener.enterSimplevalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimplevalue" ):
                listener.exitSimplevalue(self)




    def simplevalue(self, level):

        localctx = JSONParser.SimplevalueContext(self, self._ctx, self.state, level)
        self.enterRule(localctx, 16, self.RULE_simplevalue)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                localctx._STRING = self.match(JSONParser.STRING)
                putval((None if localctx._STRING is None else localctx._STRING.text))
                pass
            elif token in [JSONParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                localctx._NUMBER = self.match(JSONParser.NUMBER)
                putval((None if localctx._NUMBER is None else localctx._NUMBER.text))
                pass
            elif token in [JSONParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.match(JSONParser.T__6)
                put('true')
                pass
            elif token in [JSONParser.T__7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.match(JSONParser.T__7)
                put('false')
                pass
            elif token in [JSONParser.T__8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 86
                self.match(JSONParser.T__8)
                pass
            elif token in [JSONParser.T__0]:
                self.enterOuterAlt(localctx, 6)
                self.state = 87
                self.emptyobj()
                pass
            elif token in [JSONParser.T__4]:
                self.enterOuterAlt(localctx, 7)
                self.state = 88
                self.emptyarray()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompoundvalueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, level=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.level = None
            self.level = level

        def obj(self):
            return self.getTypedRuleContext(JSONParser.ObjContext,0)


        def array(self):
            return self.getTypedRuleContext(JSONParser.ArrayContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_compoundvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundvalue" ):
                listener.enterCompoundvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundvalue" ):
                listener.exitCompoundvalue(self)




    def compoundvalue(self, level):

        localctx = JSONParser.CompoundvalueContext(self, self._ctx, self.state, level)
        self.enterRule(localctx, 18, self.RULE_compoundvalue)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.obj(localctx.level)
                pass
            elif token in [JSONParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.array(localctx.level)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, level=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.level = None
            self.level = level

        def compoundvalue(self):
            return self.getTypedRuleContext(JSONParser.CompoundvalueContext,0)


        def simplevalue(self):
            return self.getTypedRuleContext(JSONParser.SimplevalueContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self, level):

        localctx = JSONParser.ValueContext(self, self._ctx, self.state, level)
        self.enterRule(localctx, 20, self.RULE_value)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.compoundvalue(level)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.simplevalue(level)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





