# Generated from JSON.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def put(x):
    print(x, end = '')

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("H\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\33\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\5\4\"\n\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\61\n\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\5\78\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\5\bF\n\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2J")
        buf.write("\2\20\3\2\2\2\4\32\3\2\2\2\6!\3\2\2\2\b#\3\2\2\2\n\60")
        buf.write("\3\2\2\2\f\67\3\2\2\2\16E\3\2\2\2\20\21\5\16\b\2\21\3")
        buf.write("\3\2\2\2\22\23\7\3\2\2\23\24\5\6\4\2\24\25\7\4\2\2\25")
        buf.write("\26\b\3\1\2\26\33\3\2\2\2\27\30\7\3\2\2\30\31\7\4\2\2")
        buf.write("\31\33\b\3\1\2\32\22\3\2\2\2\32\27\3\2\2\2\33\5\3\2\2")
        buf.write("\2\34\"\5\b\5\2\35\36\5\b\5\2\36\37\7\5\2\2\37 \5\6\4")
        buf.write("\2 \"\3\2\2\2!\34\3\2\2\2!\35\3\2\2\2\"\7\3\2\2\2#$\7")
        buf.write("\f\2\2$%\b\5\1\2%&\7\6\2\2&\'\b\5\1\2\'(\5\16\b\2(\t\3")
        buf.write("\2\2\2)*\b\6\1\2*+\7\7\2\2+,\5\f\7\2,-\7\b\2\2-\61\3\2")
        buf.write("\2\2./\7\7\2\2/\61\7\b\2\2\60)\3\2\2\2\60.\3\2\2\2\61")
        buf.write("\13\3\2\2\2\628\5\16\b\2\63\64\5\16\b\2\64\65\7\5\2\2")
        buf.write("\65\66\5\f\7\2\668\3\2\2\2\67\62\3\2\2\2\67\63\3\2\2\2")
        buf.write("8\r\3\2\2\29:\7\f\2\2:F\b\b\1\2;<\7\r\2\2<F\b\b\1\2=F")
        buf.write("\5\4\3\2>F\5\n\6\2?@\7\t\2\2@F\b\b\1\2AB\7\n\2\2BF\b\b")
        buf.write("\1\2CD\7\13\2\2DF\b\b\1\2E9\3\2\2\2E;\3\2\2\2E=\3\2\2")
        buf.write("\2E>\3\2\2\2E?\3\2\2\2EA\3\2\2\2EC\3\2\2\2F\17\3\2\2\2")
        buf.write("\7\32!\60\67E")
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
    RULE_members = 2
    RULE_pair = 3
    RULE_array = 4
    RULE_elements = 5
    RULE_value = 6

    ruleNames =  [ "json", "obj", "members", "pair", "array", "elements", 
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
            self.state = 14
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
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(JSONParser.T__0)
                self.state = 17
                self.members(localctx.level)
                self.state = 18
                self.match(JSONParser.T__1)
                put('\n')
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(JSONParser.T__0)
                self.state = 22
                self.match(JSONParser.T__1)
                put('{}')
                pass


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
        self.enterRule(localctx, 4, self.RULE_members)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.pair(localctx.level)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.pair(localctx.level)
                self.state = 28
                self.match(JSONParser.T__2)
                self.state = 29
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

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


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
        self.enterRule(localctx, 6, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            localctx._STRING = self.match(JSONParser.STRING)
            put((None if localctx._STRING is None else localctx._STRING.text))
            self.state = 35
            self.match(JSONParser.T__3)
            put((None if localctx._STRING is None else localctx._STRING.text)); put(':')
            self.state = 37
            self.value(localctx.level+1)
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
        self.enterRule(localctx, 8, self.RULE_array)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                put('-')
                self.state = 40
                self.match(JSONParser.T__4)
                self.state = 41
                self.elements(localctx.level+1)
                self.state = 42
                self.match(JSONParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(JSONParser.T__4)
                self.state = 45
                self.match(JSONParser.T__5)
                pass


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

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


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
        self.enterRule(localctx, 10, self.RULE_elements)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.value(localctx.level)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.value(localctx.level)
                self.state = 50
                self.match(JSONParser.T__2)
                self.state = 51
                self.elements(localctx.level)
                pass


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
            self._STRING = None # Token
            self._NUMBER = None # Token
            self.level = level

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(JSONParser.NUMBER, 0)

        def obj(self):
            return self.getTypedRuleContext(JSONParser.ObjContext,0)


        def array(self):
            return self.getTypedRuleContext(JSONParser.ArrayContext,0)


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
        self.enterRule(localctx, 12, self.RULE_value)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                localctx._STRING = self.match(JSONParser.STRING)
                put((None if localctx._STRING is None else localctx._STRING.text))
                pass
            elif token in [JSONParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                localctx._NUMBER = self.match(JSONParser.NUMBER)
                put((None if localctx._NUMBER is None else localctx._NUMBER.text))
                pass
            elif token in [JSONParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.obj(localctx.level)
                pass
            elif token in [JSONParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.array(localctx.level)
                pass
            elif token in [JSONParser.T__6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                self.match(JSONParser.T__6)
                put('true')
                pass
            elif token in [JSONParser.T__7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 63
                self.match(JSONParser.T__7)
                put('false')
                pass
            elif token in [JSONParser.T__8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 65
                self.match(JSONParser.T__8)
                put('null')
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





