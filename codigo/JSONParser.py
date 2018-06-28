# Generated from JSON.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def p(x):
    print(x, end = '')

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3\37\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\7\5-\n\5\f\5\16\5\60\13\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5\66\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6D\n\6\3\6\2\2\7\2\4\6\b\n\2\2\2J\2\f")
        buf.write("\3\2\2\2\4\36\3\2\2\2\6 \3\2\2\2\b\65\3\2\2\2\nC\3\2\2")
        buf.write("\2\f\r\5\n\6\2\r\16\b\2\1\2\16\3\3\2\2\2\17\20\7\3\2\2")
        buf.write("\20\25\5\6\4\2\21\22\7\4\2\2\22\24\5\6\4\2\23\21\3\2\2")
        buf.write("\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\30\3\2")
        buf.write("\2\2\27\25\3\2\2\2\30\31\7\5\2\2\31\32\b\3\1\2\32\37\3")
        buf.write("\2\2\2\33\34\7\3\2\2\34\35\7\5\2\2\35\37\b\3\1\2\36\17")
        buf.write("\3\2\2\2\36\33\3\2\2\2\37\5\3\2\2\2 !\7\f\2\2!\"\b\4\1")
        buf.write("\2\"#\7\6\2\2#$\b\4\1\2$%\5\n\6\2%\7\3\2\2\2&\'\b\5\1")
        buf.write("\2\'(\7\7\2\2(.\5\n\6\2)*\7\4\2\2*+\b\5\1\2+-\5\n\6\2")
        buf.write(",)\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\61\3\2\2\2")
        buf.write("\60.\3\2\2\2\61\62\7\b\2\2\62\66\3\2\2\2\63\64\7\7\2\2")
        buf.write("\64\66\7\b\2\2\65&\3\2\2\2\65\63\3\2\2\2\66\t\3\2\2\2")
        buf.write("\678\7\f\2\28D\b\6\1\29:\7\r\2\2:D\b\6\1\2;D\5\4\3\2<")
        buf.write("D\5\b\5\2=>\7\t\2\2>D\b\6\1\2?@\7\n\2\2@D\b\6\1\2AB\7")
        buf.write("\13\2\2BD\b\6\1\2C\67\3\2\2\2C9\3\2\2\2C;\3\2\2\2C<\3")
        buf.write("\2\2\2C=\3\2\2\2C?\3\2\2\2CA\3\2\2\2D\13\3\2\2\2\7\25")
        buf.write("\36.\65C")
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
            self._value = None # ValueContext

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
            localctx._value = self.value()
            localctx._value.level = 0
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
            self.level = None
            self._pair = None # PairContext

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
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(JSONParser.T__0)
                self.state = 14
                localctx._pair = self.pair()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.T__1:
                    self.state = 15
                    self.match(JSONParser.T__1)
                    self.state = 16
                    localctx._pair = self.pair()
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 22
                self.match(JSONParser.T__2)
                localctx._pair.level = localctx.level; p('\n')
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(JSONParser.T__0)
                self.state = 26
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
            self.level = None
            self._STRING = None # Token
            self._value = None # ValueContext

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
            self.state = 30
            localctx._STRING = self.match(JSONParser.STRING)
            p((None if localctx._STRING is None else localctx._STRING.text))
            self.state = 32
            self.match(JSONParser.T__3)
            p((None if localctx._STRING is None else localctx._STRING.text)); p(':'); localctx._value.level = localctx.level + 1
            self.state = 34
            localctx._value = self.value()
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
            self.level = None

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
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                p('-')
                self.state = 37
                self.match(JSONParser.T__4)
                self.state = 38
                self.value()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.T__1:
                    self.state = 39
                    self.match(JSONParser.T__1)
                    p('-')
                    self.state = 41
                    self.value()
                    self.state = 46
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 47
                self.match(JSONParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(JSONParser.T__4)
                self.state = 50
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
            self.level = None
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
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                localctx._STRING = self.match(JSONParser.STRING)
                p((None if localctx._STRING is None else localctx._STRING.text))
                pass
            elif token in [JSONParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                localctx._NUMBER = self.match(JSONParser.NUMBER)
                p((None if localctx._NUMBER is None else localctx._NUMBER.text))
                pass
            elif token in [JSONParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.obj()
                pass
            elif token in [JSONParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.array()
                pass
            elif token in [JSONParser.T__6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.match(JSONParser.T__6)
                p('true')
                pass
            elif token in [JSONParser.T__7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 61
                self.match(JSONParser.T__7)
                p('false')
                pass
            elif token in [JSONParser.T__8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 63
                self.match(JSONParser.T__8)
                p('null')
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





