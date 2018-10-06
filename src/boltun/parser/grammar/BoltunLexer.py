# Generated from /Users/vfedorenko/Developer/Business/Projects/NeuralNetworks/nlu_data_generator/src/boltun/parser/grammar/Boltun.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys



import re
import importlib
import logging

from antlr4 import *

from Queue import Empty, LifoQueue
from collections import defaultdict

logger = logging.getLogger(__name__)


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u")\u0115\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7")
        buf.write(u"\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write(u"\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write(u"\20\5\20\u0097\n\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00a6\n\22\3\23\3")
        buf.write(u"\23\3\23\5\23\u00ab\n\23\3\24\3\24\6\24\u00af\n\24\r")
        buf.write(u"\24\16\24\u00b0\3\25\3\25\6\25\u00b5\n\25\r\25\16\25")
        buf.write(u"\u00b6\3\25\3\25\7\25\u00bb\n\25\f\25\16\25\u00be\13")
        buf.write(u"\25\3\26\3\26\3\26\3\26\7\26\u00c4\n\26\f\26\16\26\u00c7")
        buf.write(u"\13\26\3\26\3\26\3\26\3\26\7\26\u00cd\n\26\f\26\16\26")
        buf.write(u"\u00d0\13\26\3\26\5\26\u00d3\n\26\3\27\3\27\3\27\3\30")
        buf.write(u"\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\6\32\u00e1\n")
        buf.write(u"\32\r\32\16\32\u00e2\3\32\3\32\3\33\3\33\6\33\u00e9\n")
        buf.write(u"\33\r\33\16\33\u00ea\3\34\3\34\3\34\3\35\3\35\3\35\3")
        buf.write(u"\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write(u"\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3")
        buf.write(u"\'\3(\3(\3(\3)\3)\2\2*\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write(u"\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write(u"%\24\'\25)\26+\27-\2/\30\61\31\63\32\65\33\67\349\35")
        buf.write(u";\36=\37? A!C\"E#G$I%K&M\'O(Q)\3\2\6\6\2\f\f\16\17))")
        buf.write(u"^^\6\2\f\f\16\17$$^^\5\2\13\f\16\17\"\"\6\2//C\\aac|")
        buf.write(u"\2\u0121\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write(u"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write(u"\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write(u"\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write(u"\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write(u"\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2")
        buf.write(u"\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3")
        buf.write(u"\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2")
        buf.write(u"I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2")
        buf.write(u"\3S\3\2\2\2\5Y\3\2\2\2\7_\3\2\2\2\tf\3\2\2\2\13l\3\2")
        buf.write(u"\2\2\ro\3\2\2\2\17r\3\2\2\2\21w\3\2\2\2\23|\3\2\2\2\25")
        buf.write(u"\177\3\2\2\2\27\u0082\3\2\2\2\31\u0087\3\2\2\2\33\u008c")
        buf.write(u"\3\2\2\2\35\u008f\3\2\2\2\37\u0092\3\2\2\2!\u0098\3\2")
        buf.write(u"\2\2#\u00a5\3\2\2\2%\u00aa\3\2\2\2\'\u00ac\3\2\2\2)\u00b2")
        buf.write(u"\3\2\2\2+\u00bf\3\2\2\2-\u00d4\3\2\2\2/\u00d7\3\2\2\2")
        buf.write(u"\61\u00db\3\2\2\2\63\u00de\3\2\2\2\65\u00e6\3\2\2\2\67")
        buf.write(u"\u00ec\3\2\2\29\u00ef\3\2\2\2;\u00f2\3\2\2\2=\u00f5\3")
        buf.write(u"\2\2\2?\u00f8\3\2\2\2A\u00fb\3\2\2\2C\u00fe\3\2\2\2E")
        buf.write(u"\u0101\3\2\2\2G\u0104\3\2\2\2I\u0107\3\2\2\2K\u010a\3")
        buf.write(u"\2\2\2M\u010d\3\2\2\2O\u0110\3\2\2\2Q\u0113\3\2\2\2S")
        buf.write(u"T\6\2\2\2TU\7]\2\2UV\7]\2\2VW\3\2\2\2WX\b\2\2\2X\4\3")
        buf.write(u"\2\2\2YZ\6\3\3\2Z[\7_\2\2[\\\7_\2\2\\]\3\2\2\2]^\b\3")
        buf.write(u"\3\2^\6\3\2\2\2_`\6\4\4\2`a\7]\2\2ab\7]\2\2bc\7%\2\2")
        buf.write(u"cd\3\2\2\2de\b\4\4\2e\b\3\2\2\2fg\6\5\5\2gh\7_\2\2hi")
        buf.write(u"\7_\2\2ij\3\2\2\2jk\b\5\5\2k\n\3\2\2\2lm\7]\2\2mn\b\6")
        buf.write(u"\6\2n\f\3\2\2\2op\7_\2\2pq\b\7\7\2q\16\3\2\2\2rs\7*\2")
        buf.write(u"\2st\7*\2\2tu\3\2\2\2uv\b\b\b\2v\20\3\2\2\2wx\7+\2\2")
        buf.write(u"xy\7+\2\2yz\3\2\2\2z{\b\t\t\2{\22\3\2\2\2|}\7*\2\2}~")
        buf.write(u"\b\n\n\2~\24\3\2\2\2\177\u0080\7+\2\2\u0080\u0081\b\13")
        buf.write(u"\13\2\u0081\26\3\2\2\2\u0082\u0083\7}\2\2\u0083\u0084")
        buf.write(u"\7}\2\2\u0084\u0085\3\2\2\2\u0085\u0086\b\f\f\2\u0086")
        buf.write(u"\30\3\2\2\2\u0087\u0088\7\177\2\2\u0088\u0089\7\177\2")
        buf.write(u"\2\u0089\u008a\3\2\2\2\u008a\u008b\b\r\r\2\u008b\32\3")
        buf.write(u"\2\2\2\u008c\u008d\7}\2\2\u008d\u008e\b\16\16\2\u008e")
        buf.write(u"\34\3\2\2\2\u008f\u0090\7\177\2\2\u0090\u0091\b\17\17")
        buf.write(u"\2\u0091\36\3\2\2\2\u0092\u0096\6\20\6\2\u0093\u0097")
        buf.write(u"\5I%\2\u0094\u0097\5K&\2\u0095\u0097\5M\'\2\u0096\u0093")
        buf.write(u"\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write(u" \3\2\2\2\u0098\u0099\6\21\7\2\u0099\u009a\13\2\2\2\u009a")
        buf.write(u"\"\3\2\2\2\u009b\u009c\6\22\b\2\u009c\u009d\7V\2\2\u009d")
        buf.write(u"\u009e\7t\2\2\u009e\u009f\7w\2\2\u009f\u00a6\7g\2\2\u00a0")
        buf.write(u"\u00a1\7H\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3\7n\2\2\u00a3")
        buf.write(u"\u00a4\7u\2\2\u00a4\u00a6\7g\2\2\u00a5\u009b\3\2\2\2")
        buf.write(u"\u00a5\u00a0\3\2\2\2\u00a6$\3\2\2\2\u00a7\u00a8\6\23")
        buf.write(u"\t\2\u00a8\u00ab\5\'\24\2\u00a9\u00ab\5)\25\2\u00aa\u00a7")
        buf.write(u"\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab&\3\2\2\2\u00ac\u00ae")
        buf.write(u"\6\24\n\2\u00ad\u00af\4\62;\2\u00ae\u00ad\3\2\2\2\u00af")
        buf.write(u"\u00b0\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2")
        buf.write(u"\2\u00b1(\3\2\2\2\u00b2\u00b4\6\25\13\2\u00b3\u00b5\5")
        buf.write(u"\'\24\2\u00b4\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write(u"\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\3\2\2")
        buf.write(u"\2\u00b8\u00bc\5E#\2\u00b9\u00bb\5\'\24\2\u00ba\u00b9")
        buf.write(u"\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc")
        buf.write(u"\u00bd\3\2\2\2\u00bd*\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf")
        buf.write(u"\u00d2\6\26\f\2\u00c0\u00c5\7)\2\2\u00c1\u00c4\5-\27")
        buf.write(u"\2\u00c2\u00c4\n\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2")
        buf.write(u"\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5")
        buf.write(u"\u00c6\3\2\2\2\u00c6\u00c8\3\2\2\2\u00c7\u00c5\3\2\2")
        buf.write(u"\2\u00c8\u00d3\7)\2\2\u00c9\u00ce\7$\2\2\u00ca\u00cd")
        buf.write(u"\5-\27\2\u00cb\u00cd\n\3\2\2\u00cc\u00ca\3\2\2\2\u00cc")
        buf.write(u"\u00cb\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2")
        buf.write(u"\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00ce")
        buf.write(u"\3\2\2\2\u00d1\u00d3\7$\2\2\u00d2\u00c0\3\2\2\2\u00d2")
        buf.write(u"\u00c9\3\2\2\2\u00d3,\3\2\2\2\u00d4\u00d5\7^\2\2\u00d5")
        buf.write(u"\u00d6\13\2\2\2\u00d6.\3\2\2\2\u00d7\u00d8\6\30\r\2\u00d8")
        buf.write(u"\u00d9\7~\2\2\u00d9\u00da\7~\2\2\u00da\60\3\2\2\2\u00db")
        buf.write(u"\u00dc\6\31\16\2\u00dc\u00dd\7~\2\2\u00dd\62\3\2\2\2")
        buf.write(u"\u00de\u00e0\6\32\17\2\u00df\u00e1\t\4\2\2\u00e0\u00df")
        buf.write(u"\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2")
        buf.write(u"\u00e3\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\b\32\20")
        buf.write(u"\2\u00e5\64\3\2\2\2\u00e6\u00e8\6\33\20\2\u00e7\u00e9")
        buf.write(u"\t\5\2\2\u00e8\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write(u"\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\66\3\2\2\2\u00ec")
        buf.write(u"\u00ed\6\34\21\2\u00ed\u00ee\13\2\2\2\u00ee8\3\2\2\2")
        buf.write(u"\u00ef\u00f0\6\35\22\2\u00f0\u00f1\7\61\2\2\u00f1:\3")
        buf.write(u"\2\2\2\u00f2\u00f3\6\36\23\2\u00f3\u00f4\7(\2\2\u00f4")
        buf.write(u"<\3\2\2\2\u00f5\u00f6\6\37\24\2\u00f6\u00f7\7@\2\2\u00f7")
        buf.write(u">\3\2\2\2\u00f8\u00f9\6 \25\2\u00f9\u00fa\7`\2\2\u00fa")
        buf.write(u"@\3\2\2\2\u00fb\u00fc\6!\26\2\u00fc\u00fd\7?\2\2\u00fd")
        buf.write(u"B\3\2\2\2\u00fe\u00ff\6\"\27\2\u00ff\u0100\7#\2\2\u0100")
        buf.write(u"D\3\2\2\2\u0101\u0102\6#\30\2\u0102\u0103\7\60\2\2\u0103")
        buf.write(u"F\3\2\2\2\u0104\u0105\6$\31\2\u0105\u0106\7.\2\2\u0106")
        buf.write(u"H\3\2\2\2\u0107\u0108\6%\32\2\u0108\u0109\7\'\2\2\u0109")
        buf.write(u"J\3\2\2\2\u010a\u010b\6&\33\2\u010b\u010c\7\u0080\2\2")
        buf.write(u"\u010cL\3\2\2\2\u010d\u010e\6\'\34\2\u010e\u010f\7B\2")
        buf.write(u"\2\u010fN\3\2\2\2\u0110\u0111\6(\35\2\u0111\u0112\7A")
        buf.write(u"\2\2\u0112P\3\2\2\2\u0113\u0114\13\2\2\2\u0114R\3\2\2")
        buf.write(u"\2\20\2\u0096\u00a5\u00aa\u00b0\u00b6\u00bc\u00c3\u00c5")
        buf.write(u"\u00cc\u00ce\u00d2\u00e2\u00ea\21\3\2\2\3\3\3\3\4\4\3")
        buf.write(u"\5\5\3\6\6\3\7\7\3\b\b\3\t\t\3\n\n\3\13\13\3\f\f\3\r")
        buf.write(u"\r\3\16\16\3\17\17\2\3\2")
        return buf.getvalue()


class BoltunLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LL_BRACK = 1
    RR_BRACK = 2
    LL_COMMENT_BRACK = 3
    RR_COMMENT_BRACK = 4
    L_BRACK = 5
    R_BRACK = 6
    LL_PAREN = 7
    RR_PAREN = 8
    L_PAREN = 9
    R_PAREN = 10
    LL_BRACE = 11
    RR_BRACE = 12
    L_BRACE = 13
    R_BRACE = 14
    ENTITY_TYPE = 15
    COMMENT_DATA = 16
    BOOL = 17
    NUMBER = 18
    INT_NUMBER = 19
    FLOAT_NUMBER = 20
    STRING = 21
    DOUBLE_PIPE = 22
    PIPE = 23
    WS = 24
    NAME = 25
    DATA = 26
    SLASH = 27
    AMP = 28
    GREATER = 29
    HAT = 30
    EQUAL = 31
    BANG = 32
    DOT = 33
    COMMA = 34
    PERCENT = 35
    TILDA = 36
    COMMAT = 37
    QUESTION = 38
    UNKNOWN = 39

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'['", u"']'", u"'(('", u"'))'", u"'('", u"')'", u"'{{'", u"'}}'", 
            u"'{'", u"'}'" ]

    symbolicNames = [ u"<INVALID>",
            u"LL_BRACK", u"RR_BRACK", u"LL_COMMENT_BRACK", u"RR_COMMENT_BRACK", 
            u"L_BRACK", u"R_BRACK", u"LL_PAREN", u"RR_PAREN", u"L_PAREN", 
            u"R_PAREN", u"LL_BRACE", u"RR_BRACE", u"L_BRACE", u"R_BRACE", 
            u"ENTITY_TYPE", u"COMMENT_DATA", u"BOOL", u"NUMBER", u"INT_NUMBER", 
            u"FLOAT_NUMBER", u"STRING", u"DOUBLE_PIPE", u"PIPE", u"WS", 
            u"NAME", u"DATA", u"SLASH", u"AMP", u"GREATER", u"HAT", u"EQUAL", 
            u"BANG", u"DOT", u"COMMA", u"PERCENT", u"TILDA", u"COMMAT", 
            u"QUESTION", u"UNKNOWN" ]

    ruleNames = [ u"LL_BRACK", u"RR_BRACK", u"LL_COMMENT_BRACK", u"RR_COMMENT_BRACK", 
                  u"L_BRACK", u"R_BRACK", u"LL_PAREN", u"RR_PAREN", u"L_PAREN", 
                  u"R_PAREN", u"LL_BRACE", u"RR_BRACE", u"L_BRACE", u"R_BRACE", 
                  u"ENTITY_TYPE", u"COMMENT_DATA", u"BOOL", u"NUMBER", u"INT_NUMBER", 
                  u"FLOAT_NUMBER", u"STRING", u"STRING_ESC_SEQ", u"DOUBLE_PIPE", 
                  u"PIPE", u"WS", u"NAME", u"DATA", u"SLASH", u"AMP", u"GREATER", 
                  u"HAT", u"EQUAL", u"BANG", u"DOT", u"COMMA", u"PERCENT", 
                  u"TILDA", u"COMMAT", u"QUESTION", u"UNKNOWN" ]

    grammarFileName = u"Boltun.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(BoltunLexer, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



    @property
    def state(self):
        try:
            return self._state
        except AttributeError:
            self._state = defaultdict(bool)
            return self._state

    @property
    def bracket_queue(self):
        try:
            return self._bracket_queue
        except AttributeError:
            self._bracket_queue = LifoQueue()
            return self._bracket_queue

    def open_bracket(self, current):
        self.bracket_queue.put(current)

    def close_bracket(self, expected):
        if self.bracket_queue.get() == expected:
            return True
        return None


    def reset(self):
        super(BoltunLexer, self).reset()
        self.state['tag'] = False
        self.state['choice'] = False
        self.state['comment'] = False
        while not self.bracket_queue.empty():
            try:
                self.bracket_queue.get(False)
            except Empty:
                continue
        self.bracket_queue.task_done()


    def action(self, localctx, ruleIndex, actionIndex):
    	if self._actions is None:
    		actions = dict()
    		actions[0] = self.LL_BRACK_action 
    		actions[1] = self.RR_BRACK_action 
    		actions[2] = self.LL_COMMENT_BRACK_action 
    		actions[3] = self.RR_COMMENT_BRACK_action 
    		actions[4] = self.L_BRACK_action 
    		actions[5] = self.R_BRACK_action 
    		actions[6] = self.LL_PAREN_action 
    		actions[7] = self.RR_PAREN_action 
    		actions[8] = self.L_PAREN_action 
    		actions[9] = self.R_PAREN_action 
    		actions[10] = self.LL_BRACE_action 
    		actions[11] = self.RR_BRACE_action 
    		actions[12] = self.L_BRACE_action 
    		actions[13] = self.R_BRACE_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def LL_BRACK_action(self, localctx , actionIndex):
        if actionIndex == 0:

            self.open_bracket(current='[[')
            self.state['tag'] = True

     

    def RR_BRACK_action(self, localctx , actionIndex):
        if actionIndex == 1:

            self.close_bracket(expected='[[')
            self.state['tag'] = False

     

    def LL_COMMENT_BRACK_action(self, localctx , actionIndex):
        if actionIndex == 2:

            self.open_bracket(current='[[')
            self.state['tag'] = True
            self.state['comment'] = True

     

    def RR_COMMENT_BRACK_action(self, localctx , actionIndex):
        if actionIndex == 3:

            self.close_bracket(expected='[[')
            self.state['tag'] = False
            self.state['comment'] = False

     

    def L_BRACK_action(self, localctx , actionIndex):
        if actionIndex == 4:

            self.open_bracket(current='[')

     

    def R_BRACK_action(self, localctx , actionIndex):
        if actionIndex == 5:

            self.close_bracket(expected='[')

     

    def LL_PAREN_action(self, localctx , actionIndex):
        if actionIndex == 6:

            self.open_bracket(current='((')

     

    def RR_PAREN_action(self, localctx , actionIndex):
        if actionIndex == 7:

            self.close_bracket(expected='((')

     

    def L_PAREN_action(self, localctx , actionIndex):
        if actionIndex == 8:

            self.open_bracket(current='(')

     

    def R_PAREN_action(self, localctx , actionIndex):
        if actionIndex == 9:

            self.close_bracket(expected='(')

     

    def LL_BRACE_action(self, localctx , actionIndex):
        if actionIndex == 10:

            self.open_bracket(current='{{')
            self.state['choice'] = True

     

    def RR_BRACE_action(self, localctx , actionIndex):
        if actionIndex == 11:

            self.close_bracket(expected='{{')
            self.state['choice'] = False

     

    def L_BRACE_action(self, localctx , actionIndex):
        if actionIndex == 12:

            self.open_bracket(current='{')

     

    def R_BRACE_action(self, localctx , actionIndex):
        if actionIndex == 13:

            self.close_bracket(expected='{')

     

    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates is None:
            preds = dict()
            preds[0] = self.LL_BRACK_sempred
            preds[1] = self.RR_BRACK_sempred
            preds[2] = self.LL_COMMENT_BRACK_sempred
            preds[3] = self.RR_COMMENT_BRACK_sempred
            preds[14] = self.ENTITY_TYPE_sempred
            preds[15] = self.COMMENT_DATA_sempred
            preds[16] = self.BOOL_sempred
            preds[17] = self.NUMBER_sempred
            preds[18] = self.INT_NUMBER_sempred
            preds[19] = self.FLOAT_NUMBER_sempred
            preds[20] = self.STRING_sempred
            preds[22] = self.DOUBLE_PIPE_sempred
            preds[23] = self.PIPE_sempred
            preds[24] = self.WS_sempred
            preds[25] = self.NAME_sempred
            preds[26] = self.DATA_sempred
            preds[27] = self.SLASH_sempred
            preds[28] = self.AMP_sempred
            preds[29] = self.GREATER_sempred
            preds[30] = self.HAT_sempred
            preds[31] = self.EQUAL_sempred
            preds[32] = self.BANG_sempred
            preds[33] = self.DOT_sempred
            preds[34] = self.COMMA_sempred
            preds[35] = self.PERCENT_sempred
            preds[36] = self.TILDA_sempred
            preds[37] = self.COMMAT_sempred
            preds[38] = self.QUESTION_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def LL_BRACK_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return not self.state['tag'] and not self.state['comment']
         

    def RR_BRACK_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.state['tag'] and not self.state['comment']
         

    def LL_COMMENT_BRACK_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return not self.state['tag'] and not self.state['comment']
         

    def RR_COMMENT_BRACK_sempred(self, localctx, predIndex):
            if predIndex == 3:
                return self.state['tag'] and self.state['comment']
         

    def ENTITY_TYPE_sempred(self, localctx, predIndex):
            if predIndex == 4:
                return self.state['tag'] and not self.state['comment']
         

    def COMMENT_DATA_sempred(self, localctx, predIndex):
            if predIndex == 5:
                return self.state['tag'] and self.state['comment']
         

    def BOOL_sempred(self, localctx, predIndex):
            if predIndex == 6:
                return self.state['tag'] and not self.state['comment']
         

    def NUMBER_sempred(self, localctx, predIndex):
            if predIndex == 7:
                return self.state['tag'] and not self.state['comment']
         

    def INT_NUMBER_sempred(self, localctx, predIndex):
            if predIndex == 8:
                return self.state['tag'] and not self.state['comment']
         

    def FLOAT_NUMBER_sempred(self, localctx, predIndex):
            if predIndex == 9:
                return self.state['tag'] and not self.state['comment']
         

    def STRING_sempred(self, localctx, predIndex):
            if predIndex == 10:
                return self.state['tag'] and not self.state['comment']
         

    def DOUBLE_PIPE_sempred(self, localctx, predIndex):
            if predIndex == 11:
                return self.state['choice'] and not self.state['tag']
         

    def PIPE_sempred(self, localctx, predIndex):
            if predIndex == 12:
                return self.state['tag']
         

    def WS_sempred(self, localctx, predIndex):
            if predIndex == 13:
                return self.state['tag'] and not self.state['comment']
         

    def NAME_sempred(self, localctx, predIndex):
            if predIndex == 14:
                return self.state['tag'] and not self.state['comment']
         

    def DATA_sempred(self, localctx, predIndex):
            if predIndex == 15:
                return not self.state['tag']
         

    def SLASH_sempred(self, localctx, predIndex):
            if predIndex == 16:
                return self.state['tag']
         

    def AMP_sempred(self, localctx, predIndex):
            if predIndex == 17:
                return self.state['tag']
         

    def GREATER_sempred(self, localctx, predIndex):
            if predIndex == 18:
                return self.state['tag']
         

    def HAT_sempred(self, localctx, predIndex):
            if predIndex == 19:
                return self.state['tag']
         

    def EQUAL_sempred(self, localctx, predIndex):
            if predIndex == 20:
                return self.state['tag']
         

    def BANG_sempred(self, localctx, predIndex):
            if predIndex == 21:
                return self.state['tag']
         

    def DOT_sempred(self, localctx, predIndex):
            if predIndex == 22:
                return self.state['tag']
         

    def COMMA_sempred(self, localctx, predIndex):
            if predIndex == 23:
                return self.state['tag']
         

    def PERCENT_sempred(self, localctx, predIndex):
            if predIndex == 24:
                return self.state['tag']
         

    def TILDA_sempred(self, localctx, predIndex):
            if predIndex == 25:
                return self.state['tag']
         

    def COMMAT_sempred(self, localctx, predIndex):
            if predIndex == 26:
                return self.state['tag']
         

    def QUESTION_sempred(self, localctx, predIndex):
            if predIndex == 27:
                return self.state['tag']
         


