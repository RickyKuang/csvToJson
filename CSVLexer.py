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
        4,0,5,54,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,13,
        8,0,10,0,12,0,16,9,0,1,0,1,0,5,0,20,8,0,10,0,12,0,23,9,0,5,0,25,
        8,0,10,0,12,0,28,9,0,1,1,1,1,1,1,1,1,5,1,34,8,1,10,1,12,1,37,9,1,
        1,1,1,1,1,2,1,2,1,3,3,3,44,8,3,1,3,1,3,1,4,4,4,49,8,4,11,4,12,4,
        50,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,5,6,0,9,10,13,13,32,32,
        44,44,59,59,124,124,3,0,10,10,13,13,44,44,3,0,10,10,13,13,34,34,
        5,0,9,9,32,32,44,44,59,59,124,124,2,0,9,9,32,32,60,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,14,1,0,0,0,3,29,
        1,0,0,0,5,40,1,0,0,0,7,43,1,0,0,0,9,48,1,0,0,0,11,13,8,0,0,0,12,
        11,1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,26,1,0,0,
        0,16,14,1,0,0,0,17,21,8,1,0,0,18,20,8,0,0,0,19,18,1,0,0,0,20,23,
        1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,
        24,17,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,2,1,0,
        0,0,28,26,1,0,0,0,29,35,5,34,0,0,30,34,8,2,0,0,31,32,5,34,0,0,32,
        34,5,34,0,0,33,30,1,0,0,0,33,31,1,0,0,0,34,37,1,0,0,0,35,33,1,0,
        0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,34,0,0,39,
        4,1,0,0,0,40,41,7,3,0,0,41,6,1,0,0,0,42,44,5,13,0,0,43,42,1,0,0,
        0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,10,0,0,46,8,1,0,0,0,47,49,
        7,4,0,0,48,47,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,
        51,52,1,0,0,0,52,53,6,4,0,0,53,10,1,0,0,0,8,0,14,21,26,33,35,43,
        50,1,6,0,0
    ]

class CSVLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TEXT = 1
    QUOTED_TEXT = 2
    DELIMITER = 3
    END_ROW = 4
    WHITESPACE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "TEXT", "QUOTED_TEXT", "DELIMITER", "END_ROW", "WHITESPACE" ]

    ruleNames = [ "TEXT", "QUOTED_TEXT", "DELIMITER", "END_ROW", "WHITESPACE" ]

    grammarFileName = "CSV.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


