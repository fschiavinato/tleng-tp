# Generated from JSON.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def putval(x):
    specialchar = [':', '-', '\\n', '{', '}', '[', ']', ',', '&', '*', '#', '?', '|', '<', '>', '=', '!', '%', '@', '\\']
    x = x.replace('\"', '', 1)
    x = x[::-1].replace('\"', '', 1)[::-1]
    if any([(c in x) for c in specialchar]):
        x = '\"' + x + '\"'
    print(x, end = '')

def put(x):
    print(x, end = '')

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("o\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5\60\n\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6>\n\6\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tX\n\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\5\ne\n\n\3\13\3\13\5\13i\n")
        buf.write("\13\3\f\3\f\5\fm\n\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\2\2\2p\2\30\3\2\2\2\4\32\3\2\2\2\6\36\3\2\2\2\b/\3")
        buf.write("\2\2\2\n=\3\2\2\2\f?\3\2\2\2\16C\3\2\2\2\20W\3\2\2\2\22")
        buf.write("d\3\2\2\2\24h\3\2\2\2\26l\3\2\2\2\30\31\5\26\f\2\31\3")
        buf.write("\3\2\2\2\32\33\7\3\2\2\33\34\5\b\5\2\34\35\7\4\2\2\35")
        buf.write("\5\3\2\2\2\36\37\7\3\2\2\37 \7\4\2\2 !\b\4\1\2!\7\3\2")
        buf.write("\2\2\"#\b\5\1\2#$\5\n\6\2$%\b\5\1\2%\60\3\2\2\2&\'\b\5")
        buf.write("\1\2\'(\5\n\6\2()\b\5\1\2)*\7\5\2\2*+\5\b\5\2+,\6\5\2")
        buf.write("\3,-\b\5\1\2-.\b\5\1\2.\60\3\2\2\2/\"\3\2\2\2/&\3\2\2")
        buf.write("\2\60\t\3\2\2\2\61\62\7\f\2\2\62\63\7\6\2\2\63\64\b\6")
        buf.write("\1\2\64\65\5\22\n\2\65\66\b\6\1\2\66>\3\2\2\2\678\7\f")
        buf.write("\2\289\7\6\2\29:\b\6\1\2:;\5\24\13\2;<\b\6\1\2<>\3\2\2")
        buf.write("\2=\61\3\2\2\2=\67\3\2\2\2>\13\3\2\2\2?@\7\7\2\2@A\5\20")
        buf.write("\t\2AB\7\b\2\2B\r\3\2\2\2CD\7\7\2\2DE\7\b\2\2EF\b\b\1")
        buf.write("\2F\17\3\2\2\2GH\b\t\1\2HX\5\22\n\2IJ\b\t\1\2JX\5\24\13")
        buf.write("\2KL\b\t\1\2LM\5\22\n\2MN\b\t\1\2NO\7\5\2\2OP\5\20\t\2")
        buf.write("PX\3\2\2\2QR\b\t\1\2RS\5\24\13\2ST\b\t\1\2TU\7\5\2\2U")
        buf.write("V\5\20\t\2VX\3\2\2\2WG\3\2\2\2WI\3\2\2\2WK\3\2\2\2WQ\3")
        buf.write("\2\2\2X\21\3\2\2\2YZ\7\f\2\2Ze\b\n\1\2[\\\7\r\2\2\\e\b")
        buf.write("\n\1\2]^\7\t\2\2^e\b\n\1\2_`\7\n\2\2`e\b\n\1\2ae\7\13")
        buf.write("\2\2be\5\6\4\2ce\5\16\b\2dY\3\2\2\2d[\3\2\2\2d]\3\2\2")
        buf.write("\2d_\3\2\2\2da\3\2\2\2db\3\2\2\2dc\3\2\2\2e\23\3\2\2\2")
        buf.write("fi\5\4\3\2gi\5\f\7\2hf\3\2\2\2hg\3\2\2\2i\25\3\2\2\2j")
        buf.write("m\5\24\13\2km\5\22\n\2lj\3\2\2\2lk\3\2\2\2m\27\3\2\2\2")
        buf.write("\b/=Wdhl")
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
            self.keys = None
            self._pair = None # PairContext
            self._members = None # MembersContext
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
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                put(level * '  ')
                self.state = 33
                localctx._pair = self.pair(localctx.level)
                localctx.keys = {localctx._pair.key: True}
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                put(level * '  ')
                self.state = 37
                localctx._pair = self.pair(localctx.level)
                put('\n')
                self.state = 39
                self.match(JSONParser.T__2)
                self.state = 40
                localctx._members = self.members(localctx.level)
                self.state = 41
                if not localctx._pair.key not in localctx._members.keys:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "$pair.key not in $members.keys")
                localctx.keys = localctx._members.keys
                localctx.keys[localctx._pair.key] = True
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
            self.key = None
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
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                localctx._STRING = self.match(JSONParser.STRING)
                self.state = 48
                self.match(JSONParser.T__3)
                putval((None if localctx._STRING is None else localctx._STRING.text)); put(': ')
                self.state = 50
                self.simplevalue(localctx.level+1)
                localctx.key = (None if localctx._STRING is None else localctx._STRING.text)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                localctx._STRING = self.match(JSONParser.STRING)
                self.state = 54
                self.match(JSONParser.T__3)
                putval((None if localctx._STRING is None else localctx._STRING.text)); put(':\n')
                self.state = 56
                self.compoundvalue(localctx.level+1)
                localctx.key = (None if localctx._STRING is None else localctx._STRING.text)
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
            self.state = 61
            self.match(JSONParser.T__4)
            self.state = 62
            self.elements(localctx.level)
            self.state = 63
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
            self.state = 65
            self.match(JSONParser.T__4)
            self.state = 66
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
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                put(level * '  ' + '- ')
                self.state = 70
                self.simplevalue(localctx.level + 1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                put(level * '  ' + '- \n')
                self.state = 72
                self.compoundvalue(localctx.level + 1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                put(level * '  ' + '- ')
                self.state = 74
                self.simplevalue(localctx.level + 1)
                put('\n')
                self.state = 76
                self.match(JSONParser.T__2)
                self.state = 77
                self.elements(localctx.level)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                put(level * '  ' + '- \n')
                self.state = 80
                self.compoundvalue(localctx.level + 1)
                put('\n')
                self.state = 82
                self.match(JSONParser.T__2)
                self.state = 83
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
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                localctx._STRING = self.match(JSONParser.STRING)
                putval((None if localctx._STRING is None else localctx._STRING.text))
                pass
            elif token in [JSONParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                localctx._NUMBER = self.match(JSONParser.NUMBER)
                putval((None if localctx._NUMBER is None else localctx._NUMBER.text))
                pass
            elif token in [JSONParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.match(JSONParser.T__6)
                put('true')
                pass
            elif token in [JSONParser.T__7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
                self.match(JSONParser.T__7)
                put('false')
                pass
            elif token in [JSONParser.T__8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 95
                self.match(JSONParser.T__8)
                pass
            elif token in [JSONParser.T__0]:
                self.enterOuterAlt(localctx, 6)
                self.state = 96
                self.emptyobj()
                pass
            elif token in [JSONParser.T__4]:
                self.enterOuterAlt(localctx, 7)
                self.state = 97
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
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.obj(localctx.level)
                pass
            elif token in [JSONParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
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
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.compoundvalue(level)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.simplevalue(level)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.members_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def members_sempred(self, localctx:MembersContext, predIndex:int):
            if predIndex == 0:
                return localctx._pair.key not in localctx._members.keys
         




