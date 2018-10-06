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
        buf.write(u"(\u0110\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\3\2\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write(u"\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write(u"\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write(u"\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\5")
        buf.write(u"\20\u0095\n\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\22\3\22\3\22\3\22\5\22\u00a4\n\22\3\23\3\23\3")
        buf.write(u"\23\5\23\u00a9\n\23\3\24\3\24\6\24\u00ad\n\24\r\24\16")
        buf.write(u"\24\u00ae\3\25\3\25\6\25\u00b3\n\25\r\25\16\25\u00b4")
        buf.write(u"\3\25\3\25\7\25\u00b9\n\25\f\25\16\25\u00bc\13\25\3\26")
        buf.write(u"\3\26\3\26\3\26\7\26\u00c2\n\26\f\26\16\26\u00c5\13\26")
        buf.write(u"\3\26\3\26\3\26\3\26\7\26\u00cb\n\26\f\26\16\26\u00ce")
        buf.write(u"\13\26\3\26\5\26\u00d1\n\26\3\27\3\27\3\27\3\30\3\30")
        buf.write(u"\3\30\3\30\3\31\3\31\3\31\3\32\3\32\6\32\u00df\n\32\r")
        buf.write(u"\32\16\32\u00e0\3\32\3\32\3\33\3\33\6\33\u00e7\n\33\r")
        buf.write(u"\33\16\33\u00e8\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3")
        buf.write(u"\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"")
        buf.write(u"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3")
        buf.write(u"(\2\2)\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write(u"\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27")
        buf.write(u"-\2/\30\61\31\63\32\65\33\67\349\35;\36=\37? A!C\"E#")
        buf.write(u"G$I%K&M\'O(\3\2\6\6\2\f\f\16\17))^^\6\2\f\f\16\17$$^")
        buf.write(u"^\5\2\13\f\16\17\"\"\6\2//C\\aac|\2\u011c\2\3\3\2\2\2")
        buf.write(u"\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write(u"\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write(u"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write(u"\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2")
        buf.write(u"\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write(u"\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3")
        buf.write(u"\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write(u"C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write(u"\2M\3\2\2\2\2O\3\2\2\2\3Q\3\2\2\2\5W\3\2\2\2\7]\3\2\2")
        buf.write(u"\2\td\3\2\2\2\13j\3\2\2\2\rm\3\2\2\2\17p\3\2\2\2\21u")
        buf.write(u"\3\2\2\2\23z\3\2\2\2\25}\3\2\2\2\27\u0080\3\2\2\2\31")
        buf.write(u"\u0085\3\2\2\2\33\u008a\3\2\2\2\35\u008d\3\2\2\2\37\u0090")
        buf.write(u"\3\2\2\2!\u0096\3\2\2\2#\u00a3\3\2\2\2%\u00a8\3\2\2\2")
        buf.write(u"\'\u00aa\3\2\2\2)\u00b0\3\2\2\2+\u00bd\3\2\2\2-\u00d2")
        buf.write(u"\3\2\2\2/\u00d5\3\2\2\2\61\u00d9\3\2\2\2\63\u00dc\3\2")
        buf.write(u"\2\2\65\u00e4\3\2\2\2\67\u00ea\3\2\2\29\u00ed\3\2\2\2")
        buf.write(u";\u00f0\3\2\2\2=\u00f3\3\2\2\2?\u00f6\3\2\2\2A\u00f9")
        buf.write(u"\3\2\2\2C\u00fc\3\2\2\2E\u00ff\3\2\2\2G\u0102\3\2\2\2")
        buf.write(u"I\u0105\3\2\2\2K\u0108\3\2\2\2M\u010b\3\2\2\2O\u010e")
        buf.write(u"\3\2\2\2QR\6\2\2\2RS\7]\2\2ST\7]\2\2TU\3\2\2\2UV\b\2")
        buf.write(u"\2\2V\4\3\2\2\2WX\6\3\3\2XY\7_\2\2YZ\7_\2\2Z[\3\2\2\2")
        buf.write(u"[\\\b\3\3\2\\\6\3\2\2\2]^\6\4\4\2^_\7]\2\2_`\7]\2\2`")
        buf.write(u"a\7%\2\2ab\3\2\2\2bc\b\4\4\2c\b\3\2\2\2de\6\5\5\2ef\7")
        buf.write(u"_\2\2fg\7_\2\2gh\3\2\2\2hi\b\5\5\2i\n\3\2\2\2jk\7]\2")
        buf.write(u"\2kl\b\6\6\2l\f\3\2\2\2mn\7_\2\2no\b\7\7\2o\16\3\2\2")
        buf.write(u"\2pq\7*\2\2qr\7*\2\2rs\3\2\2\2st\b\b\b\2t\20\3\2\2\2")
        buf.write(u"uv\7+\2\2vw\7+\2\2wx\3\2\2\2xy\b\t\t\2y\22\3\2\2\2z{")
        buf.write(u"\7*\2\2{|\b\n\n\2|\24\3\2\2\2}~\7+\2\2~\177\b\13\13\2")
        buf.write(u"\177\26\3\2\2\2\u0080\u0081\7}\2\2\u0081\u0082\7}\2\2")
        buf.write(u"\u0082\u0083\3\2\2\2\u0083\u0084\b\f\f\2\u0084\30\3\2")
        buf.write(u"\2\2\u0085\u0086\7\177\2\2\u0086\u0087\7\177\2\2\u0087")
        buf.write(u"\u0088\3\2\2\2\u0088\u0089\b\r\r\2\u0089\32\3\2\2\2\u008a")
        buf.write(u"\u008b\7}\2\2\u008b\u008c\b\16\16\2\u008c\34\3\2\2\2")
        buf.write(u"\u008d\u008e\7\177\2\2\u008e\u008f\b\17\17\2\u008f\36")
        buf.write(u"\3\2\2\2\u0090\u0094\6\20\6\2\u0091\u0095\5I%\2\u0092")
        buf.write(u"\u0095\5K&\2\u0093\u0095\5M\'\2\u0094\u0091\3\2\2\2\u0094")
        buf.write(u"\u0092\3\2\2\2\u0094\u0093\3\2\2\2\u0095 \3\2\2\2\u0096")
        buf.write(u"\u0097\6\21\7\2\u0097\u0098\13\2\2\2\u0098\"\3\2\2\2")
        buf.write(u"\u0099\u009a\6\22\b\2\u009a\u009b\7V\2\2\u009b\u009c")
        buf.write(u"\7t\2\2\u009c\u009d\7w\2\2\u009d\u00a4\7g\2\2\u009e\u009f")
        buf.write(u"\7H\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2")
        buf.write(u"\7u\2\2\u00a2\u00a4\7g\2\2\u00a3\u0099\3\2\2\2\u00a3")
        buf.write(u"\u009e\3\2\2\2\u00a4$\3\2\2\2\u00a5\u00a6\6\23\t\2\u00a6")
        buf.write(u"\u00a9\5\'\24\2\u00a7\u00a9\5)\25\2\u00a8\u00a5\3\2\2")
        buf.write(u"\2\u00a8\u00a7\3\2\2\2\u00a9&\3\2\2\2\u00aa\u00ac\6\24")
        buf.write(u"\n\2\u00ab\u00ad\4\62;\2\u00ac\u00ab\3\2\2\2\u00ad\u00ae")
        buf.write(u"\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write(u"(\3\2\2\2\u00b0\u00b2\6\25\13\2\u00b1\u00b3\5\'\24\2")
        buf.write(u"\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2")
        buf.write(u"\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write(u"\u00ba\5E#\2\u00b7\u00b9\5\'\24\2\u00b8\u00b7\3\2\2\2")
        buf.write(u"\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write(u"\3\2\2\2\u00bb*\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00d0")
        buf.write(u"\6\26\f\2\u00be\u00c3\7)\2\2\u00bf\u00c2\5-\27\2\u00c0")
        buf.write(u"\u00c2\n\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3\2\2")
        buf.write(u"\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4")
        buf.write(u"\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6")
        buf.write(u"\u00d1\7)\2\2\u00c7\u00cc\7$\2\2\u00c8\u00cb\5-\27\2")
        buf.write(u"\u00c9\u00cb\n\3\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00c9")
        buf.write(u"\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc")
        buf.write(u"\u00cd\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3\2\2")
        buf.write(u"\2\u00cf\u00d1\7$\2\2\u00d0\u00be\3\2\2\2\u00d0\u00c7")
        buf.write(u"\3\2\2\2\u00d1,\3\2\2\2\u00d2\u00d3\7^\2\2\u00d3\u00d4")
        buf.write(u"\13\2\2\2\u00d4.\3\2\2\2\u00d5\u00d6\6\30\r\2\u00d6\u00d7")
        buf.write(u"\7~\2\2\u00d7\u00d8\7~\2\2\u00d8\60\3\2\2\2\u00d9\u00da")
        buf.write(u"\6\31\16\2\u00da\u00db\7~\2\2\u00db\62\3\2\2\2\u00dc")
        buf.write(u"\u00de\6\32\17\2\u00dd\u00df\t\4\2\2\u00de\u00dd\3\2")
        buf.write(u"\2\2\u00df\u00e0\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1")
        buf.write(u"\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\b\32\20\2\u00e3")
        buf.write(u"\64\3\2\2\2\u00e4\u00e6\6\33\20\2\u00e5\u00e7\t\5\2\2")
        buf.write(u"\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e6")
        buf.write(u"\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\66\3\2\2\2\u00ea\u00eb")
        buf.write(u"\6\34\21\2\u00eb\u00ec\13\2\2\2\u00ec8\3\2\2\2\u00ed")
        buf.write(u"\u00ee\6\35\22\2\u00ee\u00ef\7\61\2\2\u00ef:\3\2\2\2")
        buf.write(u"\u00f0\u00f1\6\36\23\2\u00f1\u00f2\7(\2\2\u00f2<\3\2")
        buf.write(u"\2\2\u00f3\u00f4\6\37\24\2\u00f4\u00f5\7@\2\2\u00f5>")
        buf.write(u"\3\2\2\2\u00f6\u00f7\6 \25\2\u00f7\u00f8\7`\2\2\u00f8")
        buf.write(u"@\3\2\2\2\u00f9\u00fa\6!\26\2\u00fa\u00fb\7?\2\2\u00fb")
        buf.write(u"B\3\2\2\2\u00fc\u00fd\6\"\27\2\u00fd\u00fe\7#\2\2\u00fe")
        buf.write(u"D\3\2\2\2\u00ff\u0100\6#\30\2\u0100\u0101\7\60\2\2\u0101")
        buf.write(u"F\3\2\2\2\u0102\u0103\6$\31\2\u0103\u0104\7.\2\2\u0104")
        buf.write(u"H\3\2\2\2\u0105\u0106\6%\32\2\u0106\u0107\7\'\2\2\u0107")
        buf.write(u"J\3\2\2\2\u0108\u0109\6&\33\2\u0109\u010a\7\u0080\2\2")
        buf.write(u"\u010aL\3\2\2\2\u010b\u010c\6\'\34\2\u010c\u010d\7B\2")
        buf.write(u"\2\u010dN\3\2\2\2\u010e\u010f\13\2\2\2\u010fP\3\2\2\2")
        buf.write(u"\20\2\u0094\u00a3\u00a8\u00ae\u00b4\u00ba\u00c1\u00c3")
        buf.write(u"\u00ca\u00cc\u00d0\u00e0\u00e8\21\3\2\2\3\3\3\3\4\4\3")
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
    UNKNOWN = 38

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
            u"UNKNOWN" ]

    ruleNames = [ u"LL_BRACK", u"RR_BRACK", u"LL_COMMENT_BRACK", u"RR_COMMENT_BRACK", 
                  u"L_BRACK", u"R_BRACK", u"LL_PAREN", u"RR_PAREN", u"L_PAREN", 
                  u"R_PAREN", u"LL_BRACE", u"RR_BRACE", u"L_BRACE", u"R_BRACE", 
                  u"ENTITY_TYPE", u"COMMENT_DATA", u"BOOL", u"NUMBER", u"INT_NUMBER", 
                  u"FLOAT_NUMBER", u"STRING", u"STRING_ESC_SEQ", u"DOUBLE_PIPE", 
                  u"PIPE", u"WS", u"NAME", u"DATA", u"SLASH", u"AMP", u"GREATER", 
                  u"HAT", u"EQUAL", u"BANG", u"DOT", u"COMMA", u"PERCENT", 
                  u"TILDA", u"COMMAT", u"UNKNOWN" ]

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
         


