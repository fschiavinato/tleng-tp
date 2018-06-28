# Generated from JSON.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JSONParser import JSONParser
else:
    from JSONParser import JSONParser

def putval(x):
    x = x.replace('\"', '')
    if ':' in x or '-' in x or '\\n' in x:
        x = '\"' + x + '\"'
    print(x, end = '')

def put(x):
    print(x, end = '')


# This class defines a complete listener for a parse tree produced by JSONParser.
class JSONListener(ParseTreeListener):

    # Enter a parse tree produced by JSONParser#json.
    def enterJson(self, ctx:JSONParser.JsonContext):
        pass

    # Exit a parse tree produced by JSONParser#json.
    def exitJson(self, ctx:JSONParser.JsonContext):
        pass


    # Enter a parse tree produced by JSONParser#obj.
    def enterObj(self, ctx:JSONParser.ObjContext):
        pass

    # Exit a parse tree produced by JSONParser#obj.
    def exitObj(self, ctx:JSONParser.ObjContext):
        pass


    # Enter a parse tree produced by JSONParser#emptyobj.
    def enterEmptyobj(self, ctx:JSONParser.EmptyobjContext):
        pass

    # Exit a parse tree produced by JSONParser#emptyobj.
    def exitEmptyobj(self, ctx:JSONParser.EmptyobjContext):
        pass


    # Enter a parse tree produced by JSONParser#members.
    def enterMembers(self, ctx:JSONParser.MembersContext):
        pass

    # Exit a parse tree produced by JSONParser#members.
    def exitMembers(self, ctx:JSONParser.MembersContext):
        pass


    # Enter a parse tree produced by JSONParser#pair.
    def enterPair(self, ctx:JSONParser.PairContext):
        pass

    # Exit a parse tree produced by JSONParser#pair.
    def exitPair(self, ctx:JSONParser.PairContext):
        pass


    # Enter a parse tree produced by JSONParser#array.
    def enterArray(self, ctx:JSONParser.ArrayContext):
        pass

    # Exit a parse tree produced by JSONParser#array.
    def exitArray(self, ctx:JSONParser.ArrayContext):
        pass


    # Enter a parse tree produced by JSONParser#emptyarray.
    def enterEmptyarray(self, ctx:JSONParser.EmptyarrayContext):
        pass

    # Exit a parse tree produced by JSONParser#emptyarray.
    def exitEmptyarray(self, ctx:JSONParser.EmptyarrayContext):
        pass


    # Enter a parse tree produced by JSONParser#elements.
    def enterElements(self, ctx:JSONParser.ElementsContext):
        pass

    # Exit a parse tree produced by JSONParser#elements.
    def exitElements(self, ctx:JSONParser.ElementsContext):
        pass


    # Enter a parse tree produced by JSONParser#simplevalue.
    def enterSimplevalue(self, ctx:JSONParser.SimplevalueContext):
        pass

    # Exit a parse tree produced by JSONParser#simplevalue.
    def exitSimplevalue(self, ctx:JSONParser.SimplevalueContext):
        pass


    # Enter a parse tree produced by JSONParser#compoundvalue.
    def enterCompoundvalue(self, ctx:JSONParser.CompoundvalueContext):
        pass

    # Exit a parse tree produced by JSONParser#compoundvalue.
    def exitCompoundvalue(self, ctx:JSONParser.CompoundvalueContext):
        pass


    # Enter a parse tree produced by JSONParser#value.
    def enterValue(self, ctx:JSONParser.ValueContext):
        pass

    # Exit a parse tree produced by JSONParser#value.
    def exitValue(self, ctx:JSONParser.ValueContext):
        pass


