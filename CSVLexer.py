# Generated from CSV.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,38,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        1,4,1,15,8,1,11,1,12,1,16,1,2,1,2,1,2,1,2,3,2,23,8,2,1,2,1,2,1,3,
        3,3,28,8,3,1,3,1,3,1,4,4,4,33,8,4,11,4,12,4,34,1,4,1,4,0,0,5,1,1,
        3,2,5,3,7,4,9,5,1,0,3,3,0,10,10,34,34,44,44,1,0,34,34,2,0,9,9,32,
        32,41,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,1,11,1,0,0,0,3,14,1,0,0,0,5,18,1,0,0,0,7,27,1,0,0,0,9,32,1,0,0,
        0,11,12,5,44,0,0,12,2,1,0,0,0,13,15,8,0,0,0,14,13,1,0,0,0,15,16,
        1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,4,1,0,0,0,18,22,5,34,0,0,
        19,20,5,34,0,0,20,23,5,34,0,0,21,23,8,1,0,0,22,19,1,0,0,0,22,21,
        1,0,0,0,23,24,1,0,0,0,24,25,5,34,0,0,25,6,1,0,0,0,26,28,5,13,0,0,
        27,26,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,5,10,0,0,30,8,1,
        0,0,0,31,33,7,2,0,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,
        35,1,0,0,0,35,36,1,0,0,0,36,37,6,4,0,0,37,10,1,0,0,0,5,0,16,22,27,
        34,1,6,0,0
    ]

class CSVLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    TEXT = 2
    QUOTED_TEXT = 3
    CRLF = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','" ]

    symbolicNames = [ "<INVALID>",
            "TEXT", "QUOTED_TEXT", "CRLF", "WS" ]

    ruleNames = [ "T__0", "TEXT", "QUOTED_TEXT", "CRLF", "WS" ]

    grammarFileName = "CSV.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


