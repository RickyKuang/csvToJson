# Generated from CSV.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,30,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,3,0,16,8,0,1,0,1,0,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,
        26,9,1,1,2,1,2,1,2,0,0,3,0,2,4,0,1,1,0,2,3,29,0,6,1,0,0,0,2,19,1,
        0,0,0,4,27,1,0,0,0,6,11,3,2,1,0,7,8,5,4,0,0,8,10,3,2,1,0,9,7,1,0,
        0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,15,1,0,0,0,13,11,
        1,0,0,0,14,16,5,4,0,0,15,14,1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,0,
        17,18,5,0,0,1,18,1,1,0,0,0,19,24,3,4,2,0,20,21,5,1,0,0,21,23,3,4,
        2,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,
        1,0,0,0,26,24,1,0,0,0,27,28,7,0,0,0,28,5,1,0,0,0,3,11,15,24
    ]

class CSVParser ( Parser ):

    grammarFileName = "CSV.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "TEXT", "QUOTED_TEXT", "CRLF", 
                      "WS" ]

    RULE_file = 0
    RULE_row = 1
    RULE_field = 2

    ruleNames =  [ "file", "row", "field" ]

    EOF = Token.EOF
    T__0=1
    TEXT=2
    QUOTED_TEXT=3
    CRLF=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.RowContext)
            else:
                return self.getTypedRuleContext(CSVParser.RowContext,i)


        def EOF(self):
            return self.getToken(CSVParser.EOF, 0)

        def CRLF(self, i:int=None):
            if i is None:
                return self.getTokens(CSVParser.CRLF)
            else:
                return self.getToken(CSVParser.CRLF, i)

        def getRuleIndex(self):
            return CSVParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile" ):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = CSVParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.row()
            self.state = 11
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 7
                    self.match(CSVParser.CRLF)
                    self.state = 8
                    self.row() 
                self.state = 13
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 14
                self.match(CSVParser.CRLF)


            self.state = 17
            self.match(CSVParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.FieldContext)
            else:
                return self.getTypedRuleContext(CSVParser.FieldContext,i)


        def getRuleIndex(self):
            return CSVParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRow" ):
                return visitor.visitRow(self)
            else:
                return visitor.visitChildren(self)




    def row(self):

        localctx = CSVParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.field()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 20
                self.match(CSVParser.T__0)
                self.state = 21
                self.field()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(CSVParser.TEXT, 0)

        def QUOTED_TEXT(self):
            return self.getToken(CSVParser.QUOTED_TEXT, 0)

        def getRuleIndex(self):
            return CSVParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = CSVParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





