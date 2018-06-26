# Generated from JSON.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


p = lambda x: print(x, end = '')

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\7\3\23\n\3\f\3\16\3\26\13\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\7\5+\n\5\f\5\16\5.\13\5\3\5\3\5\3\5\3\5\5")
        buf.write("\5\64\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6?\n\6")
        buf.write("\3\6\2\2\7\2\4\6\b\n\2\2\2E\2\f\3\2\2\2\4\35\3\2\2\2\6")
        buf.write("\37\3\2\2\2\b\63\3\2\2\2\n>\3\2\2\2\f\r\5\n\6\2\r\3\3")
        buf.write("\2\2\2\16\17\7\3\2\2\17\24\5\6\4\2\20\21\7\4\2\2\21\23")
        buf.write("\5\6\4\2\22\20\3\2\2\2\23\26\3\2\2\2\24\22\3\2\2\2\24")
        buf.write("\25\3\2\2\2\25\27\3\2\2\2\26\24\3\2\2\2\27\30\7\5\2\2")
        buf.write("\30\31\b\3\1\2\31\36\3\2\2\2\32\33\7\3\2\2\33\34\7\5\2")
        buf.write("\2\34\36\b\3\1\2\35\16\3\2\2\2\35\32\3\2\2\2\36\5\3\2")
        buf.write("\2\2\37 \7\f\2\2 !\7\6\2\2!\"\b\4\1\2\"#\5\n\6\2#\7\3")
        buf.write("\2\2\2$%\b\5\1\2%&\7\7\2\2&,\5\n\6\2\'(\7\4\2\2()\b\5")
        buf.write("\1\2)+\5\n\6\2*\'\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2")
        buf.write("\2-/\3\2\2\2.,\3\2\2\2/\60\7\b\2\2\60\64\3\2\2\2\61\62")
        buf.write("\7\7\2\2\62\64\7\b\2\2\63$\3\2\2\2\63\61\3\2\2\2\64\t")
        buf.write("\3\2\2\2\65\66\7\f\2\2\66?\b\6\1\2\678\7\r\2\28?\b\6\1")
        buf.write("\29?\5\4\3\2:?\5\b\5\2;?\7\t\2\2<?\7\n\2\2=?\7\13\2\2")
        buf.write(">\65\3\2\2\2>\67\3\2\2\2>9\3\2\2\2>:\3\2\2\2>;\3\2\2\2")
        buf.write("><\3\2\2\2>=\3\2\2\2?\13\3\2\2\2\7\24\35,\63>")
        return buf.getvalue()


class JSONParser ( Parser ):

    grammarFileName = "JSON.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "':'", "'['", "']'", 
                     "'true'", "'false'", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "NUMBER", "WS" ]

    RULE_json = 0
    RULE_obj = 1
    RULE_pair = 2
    RULE_array = 3
    RULE_value = 4

    ruleNames =  [ "json", "obj", "pair", "array", "value" ]

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
            self.state = 10
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.PairContext)
            else:
                return self.getTypedRuleContext(JSONParser.PairContext,i)


        def getRuleIndex(self):
            return JSONParser.RULE_obj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObj" ):
                listener.enterObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObj" ):
                listener.exitObj(self)




    def obj(self):

        localctx = JSONParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(JSONParser.T__0)
                self.state = 13
                self.pair()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.T__1:
                    self.state = 14
                    self.match(JSONParser.T__1)
                    self.state = 15
                    self.pair()
                    self.state = 20
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 21
                self.match(JSONParser.T__2)
                print('')
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(JSONParser.T__0)
                self.state = 25
                self.match(JSONParser.T__2)
                p('{}')
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._STRING = None # Token

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




    def pair(self):

        localctx = JSONParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            localctx._STRING = self.match(JSONParser.STRING)
            self.state = 30
            self.match(JSONParser.T__3)
            p((None if localctx._STRING is None else localctx._STRING.text)); p(':')
            self.state = 32
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.ValueContext)
            else:
                return self.getTypedRuleContext(JSONParser.ValueContext,i)


        def getRuleIndex(self):
            return JSONParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = JSONParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                p('-')
                self.state = 35
                self.match(JSONParser.T__4)
                self.state = 36
                self.value()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.T__1:
                    self.state = 37
                    self.match(JSONParser.T__1)
                    p('-')
                    self.state = 39
                    self.value()
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 45
                self.match(JSONParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(JSONParser.T__4)
                self.state = 48
                self.match(JSONParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._STRING = None # Token
            self._NUMBER = None # Token

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




    def value(self):

        localctx = JSONParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                localctx._STRING = self.match(JSONParser.STRING)
                p((None if localctx._STRING is None else localctx._STRING.text))
                pass
            elif token in [JSONParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                localctx._NUMBER = self.match(JSONParser.NUMBER)
                p((None if localctx._NUMBER is None else localctx._NUMBER.text))
                pass
            elif token in [JSONParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.obj()
                pass
            elif token in [JSONParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.array()
                pass
            elif token in [JSONParser.T__6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.match(JSONParser.T__6)
                pass
            elif token in [JSONParser.T__7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.match(JSONParser.T__7)
                pass
            elif token in [JSONParser.T__8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 59
                self.match(JSONParser.T__8)
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





