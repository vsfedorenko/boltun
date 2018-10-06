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
        buf.write(u",\u0139\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write(u"\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00ad\n\22")
        buf.write(u"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5")
        buf.write(u"\23\u00b9\n\23\3\24\3\24\3\24\5\24\u00be\n\24\3\25\3")
        buf.write(u"\25\6\25\u00c2\n\25\r\25\16\25\u00c3\3\26\3\26\6\26\u00c8")
        buf.write(u"\n\26\r\26\16\26\u00c9\3\26\3\26\7\26\u00ce\n\26\f\26")
        buf.write(u"\16\26\u00d1\13\26\3\27\3\27\3\27\3\27\7\27\u00d7\n\27")
        buf.write(u"\f\27\16\27\u00da\13\27\3\27\3\27\3\27\3\27\7\27\u00e0")
        buf.write(u"\n\27\f\27\16\27\u00e3\13\27\3\27\5\27\u00e6\n\27\3\30")
        buf.write(u"\3\30\3\30\3\31\3\31\6\31\u00ed\n\31\r\31\16\31\u00ee")
        buf.write(u"\3\31\3\31\3\32\3\32\6\32\u00f5\n\32\r\32\16\32\u00f6")
        buf.write(u"\3\32\3\32\7\32\u00fb\n\32\f\32\16\32\u00fe\13\32\3\33")
        buf.write(u"\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3")
        buf.write(u"\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#")
        buf.write(u"\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3")
        buf.write(u")\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\2\2/\3")
        buf.write(u"\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write(u"\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\2")
        buf.write(u"\61\31\63\32\65\2\67\29\33;\34=\35?\36A\37C E!G\"I#K")
        buf.write(u"$M%O&Q\'S(U)W*Y+[,\3\2\6\6\2\f\f\16\17))^^\6\2\f\f\16")
        buf.write(u"\17$$^^\5\2\13\f\16\17\"\"\6\2//C\\aac|\2\u0145\2\3\3")
        buf.write(u"\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write(u"\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write(u"\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write(u"\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write(u"\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write(u"\61\3\2\2\2\2\63\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write(u"\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write(u"\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write(u"Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write(u"\2[\3\2\2\2\3]\3\2\2\2\5c\3\2\2\2\7i\3\2\2\2\tp\3\2\2")
        buf.write(u"\2\13v\3\2\2\2\ry\3\2\2\2\17|\3\2\2\2\21\u0081\3\2\2")
        buf.write(u"\2\23\u0086\3\2\2\2\25\u0089\3\2\2\2\27\u008c\3\2\2\2")
        buf.write(u"\31\u0092\3\2\2\2\33\u0098\3\2\2\2\35\u009d\3\2\2\2\37")
        buf.write(u"\u00a2\3\2\2\2!\u00a5\3\2\2\2#\u00a8\3\2\2\2%\u00b8\3")
        buf.write(u"\2\2\2\'\u00bd\3\2\2\2)\u00bf\3\2\2\2+\u00c5\3\2\2\2")
        buf.write(u"-\u00d2\3\2\2\2/\u00e7\3\2\2\2\61\u00ea\3\2\2\2\63\u00f2")
        buf.write(u"\3\2\2\2\65\u00ff\3\2\2\2\67\u0101\3\2\2\29\u0103\3\2")
        buf.write(u"\2\2;\u0106\3\2\2\2=\u0109\3\2\2\2?\u010d\3\2\2\2A\u0110")
        buf.write(u"\3\2\2\2C\u0113\3\2\2\2E\u0116\3\2\2\2G\u0119\3\2\2\2")
        buf.write(u"I\u011c\3\2\2\2K\u011f\3\2\2\2M\u0122\3\2\2\2O\u0125")
        buf.write(u"\3\2\2\2Q\u0128\3\2\2\2S\u012b\3\2\2\2U\u012e\3\2\2\2")
        buf.write(u"W\u0131\3\2\2\2Y\u0134\3\2\2\2[\u0137\3\2\2\2]^\6\2\2")
        buf.write(u"\2^_\7]\2\2_`\7]\2\2`a\3\2\2\2ab\b\2\2\2b\4\3\2\2\2c")
        buf.write(u"d\6\3\3\2de\7_\2\2ef\7_\2\2fg\3\2\2\2gh\b\3\3\2h\6\3")
        buf.write(u"\2\2\2ij\6\4\4\2jk\7]\2\2kl\7]\2\2lm\7%\2\2mn\3\2\2\2")
        buf.write(u"no\b\4\4\2o\b\3\2\2\2pq\6\5\5\2qr\7_\2\2rs\7_\2\2st\3")
        buf.write(u"\2\2\2tu\b\5\5\2u\n\3\2\2\2vw\7]\2\2wx\b\6\6\2x\f\3\2")
        buf.write(u"\2\2yz\7_\2\2z{\b\7\7\2{\16\3\2\2\2|}\7*\2\2}~\7*\2\2")
        buf.write(u"~\177\3\2\2\2\177\u0080\b\b\b\2\u0080\20\3\2\2\2\u0081")
        buf.write(u"\u0082\7+\2\2\u0082\u0083\7+\2\2\u0083\u0084\3\2\2\2")
        buf.write(u"\u0084\u0085\b\t\t\2\u0085\22\3\2\2\2\u0086\u0087\7*")
        buf.write(u"\2\2\u0087\u0088\b\n\n\2\u0088\24\3\2\2\2\u0089\u008a")
        buf.write(u"\7+\2\2\u008a\u008b\b\13\13\2\u008b\26\3\2\2\2\u008c")
        buf.write(u"\u008d\7}\2\2\u008d\u008e\7}\2\2\u008e\u008f\7}\2\2\u008f")
        buf.write(u"\u0090\3\2\2\2\u0090\u0091\b\f\f\2\u0091\30\3\2\2\2\u0092")
        buf.write(u"\u0093\7\177\2\2\u0093\u0094\7\177\2\2\u0094\u0095\7")
        buf.write(u"\177\2\2\u0095\u0096\3\2\2\2\u0096\u0097\b\r\r\2\u0097")
        buf.write(u"\32\3\2\2\2\u0098\u0099\7}\2\2\u0099\u009a\7}\2\2\u009a")
        buf.write(u"\u009b\3\2\2\2\u009b\u009c\b\16\16\2\u009c\34\3\2\2\2")
        buf.write(u"\u009d\u009e\7\177\2\2\u009e\u009f\7\177\2\2\u009f\u00a0")
        buf.write(u"\3\2\2\2\u00a0\u00a1\b\17\17\2\u00a1\36\3\2\2\2\u00a2")
        buf.write(u"\u00a3\7}\2\2\u00a3\u00a4\b\20\20\2\u00a4 \3\2\2\2\u00a5")
        buf.write(u"\u00a6\7\177\2\2\u00a6\u00a7\b\21\21\2\u00a7\"\3\2\2")
        buf.write(u"\2\u00a8\u00ac\6\22\6\2\u00a9\u00ad\5S*\2\u00aa\u00ad")
        buf.write(u"\5U+\2\u00ab\u00ad\5W,\2\u00ac\u00a9\3\2\2\2\u00ac\u00aa")
        buf.write(u"\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad$\3\2\2\2\u00ae\u00af")
        buf.write(u"\6\23\7\2\u00af\u00b0\7V\2\2\u00b0\u00b1\7t\2\2\u00b1")
        buf.write(u"\u00b2\7w\2\2\u00b2\u00b9\7g\2\2\u00b3\u00b4\7H\2\2\u00b4")
        buf.write(u"\u00b5\7c\2\2\u00b5\u00b6\7n\2\2\u00b6\u00b7\7u\2\2\u00b7")
        buf.write(u"\u00b9\7g\2\2\u00b8\u00ae\3\2\2\2\u00b8\u00b3\3\2\2\2")
        buf.write(u"\u00b9&\3\2\2\2\u00ba\u00bb\6\24\b\2\u00bb\u00be\5)\25")
        buf.write(u"\2\u00bc\u00be\5+\26\2\u00bd\u00ba\3\2\2\2\u00bd\u00bc")
        buf.write(u"\3\2\2\2\u00be(\3\2\2\2\u00bf\u00c1\6\25\t\2\u00c0\u00c2")
        buf.write(u"\4\62;\2\u00c1\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write(u"\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4*\3\2\2\2\u00c5")
        buf.write(u"\u00c7\6\26\n\2\u00c6\u00c8\5)\25\2\u00c7\u00c6\3\2\2")
        buf.write(u"\2\u00c8\u00c9\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca")
        buf.write(u"\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cf\5O(\2\u00cc")
        buf.write(u"\u00ce\5)\25\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1\3\2\2")
        buf.write(u"\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0,\3\2")
        buf.write(u"\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00e5\6\27\13\2\u00d3")
        buf.write(u"\u00d8\7)\2\2\u00d4\u00d7\5/\30\2\u00d5\u00d7\n\2\2\2")
        buf.write(u"\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00da")
        buf.write(u"\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write(u"\u00db\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00e6\7)\2\2")
        buf.write(u"\u00dc\u00e1\7$\2\2\u00dd\u00e0\5/\30\2\u00de\u00e0\n")
        buf.write(u"\3\2\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2\u00e0")
        buf.write(u"\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2")
        buf.write(u"\2\u00e2\u00e4\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e6")
        buf.write(u"\7$\2\2\u00e5\u00d3\3\2\2\2\u00e5\u00dc\3\2\2\2\u00e6")
        buf.write(u".\3\2\2\2\u00e7\u00e8\7^\2\2\u00e8\u00e9\13\2\2\2\u00e9")
        buf.write(u"\60\3\2\2\2\u00ea\u00ec\6\31\f\2\u00eb\u00ed\t\4\2\2")
        buf.write(u"\u00ec\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ec")
        buf.write(u"\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write(u"\u00f1\b\31\22\2\u00f1\62\3\2\2\2\u00f2\u00f4\6\32\r")
        buf.write(u"\2\u00f3\u00f5\5\65\33\2\u00f4\u00f3\3\2\2\2\u00f5\u00f6")
        buf.write(u"\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write(u"\u00fc\3\2\2\2\u00f8\u00fb\5\65\33\2\u00f9\u00fb\5\67")
        buf.write(u"\34\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fe")
        buf.write(u"\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd")
        buf.write(u"\64\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0100\t\5\2\2\u0100")
        buf.write(u"\66\3\2\2\2\u0101\u0102\4\62;\2\u01028\3\2\2\2\u0103")
        buf.write(u"\u0104\6\35\16\2\u0104\u0105\13\2\2\2\u0105:\3\2\2\2")
        buf.write(u"\u0106\u0107\6\36\17\2\u0107\u0108\13\2\2\2\u0108<\3")
        buf.write(u"\2\2\2\u0109\u010a\6\37\20\2\u010a\u010b\7~\2\2\u010b")
        buf.write(u"\u010c\7~\2\2\u010c>\3\2\2\2\u010d\u010e\6 \21\2\u010e")
        buf.write(u"\u010f\7~\2\2\u010f@\3\2\2\2\u0110\u0111\6!\22\2\u0111")
        buf.write(u"\u0112\7\61\2\2\u0112B\3\2\2\2\u0113\u0114\6\"\23\2\u0114")
        buf.write(u"\u0115\7(\2\2\u0115D\3\2\2\2\u0116\u0117\6#\24\2\u0117")
        buf.write(u"\u0118\7%\2\2\u0118F\3\2\2\2\u0119\u011a\6$\25\2\u011a")
        buf.write(u"\u011b\7@\2\2\u011bH\3\2\2\2\u011c\u011d\6%\26\2\u011d")
        buf.write(u"\u011e\7`\2\2\u011eJ\3\2\2\2\u011f\u0120\6&\27\2\u0120")
        buf.write(u"\u0121\7?\2\2\u0121L\3\2\2\2\u0122\u0123\6\'\30\2\u0123")
        buf.write(u"\u0124\7#\2\2\u0124N\3\2\2\2\u0125\u0126\6(\31\2\u0126")
        buf.write(u"\u0127\7\60\2\2\u0127P\3\2\2\2\u0128\u0129\6)\32\2\u0129")
        buf.write(u"\u012a\7.\2\2\u012aR\3\2\2\2\u012b\u012c\6*\33\2\u012c")
        buf.write(u"\u012d\7\'\2\2\u012dT\3\2\2\2\u012e\u012f\6+\34\2\u012f")
        buf.write(u"\u0130\7\u0080\2\2\u0130V\3\2\2\2\u0131\u0132\6,\35\2")
        buf.write(u"\u0132\u0133\7B\2\2\u0133X\3\2\2\2\u0134\u0135\6-\36")
        buf.write(u"\2\u0135\u0136\7A\2\2\u0136Z\3\2\2\2\u0137\u0138\13\2")
        buf.write(u"\2\2\u0138\\\3\2\2\2\22\2\u00ac\u00b8\u00bd\u00c3\u00c9")
        buf.write(u"\u00cf\u00d6\u00d8\u00df\u00e1\u00e5\u00ee\u00f6\u00fa")
        buf.write(u"\u00fc\23\3\2\2\3\3\3\3\4\4\3\5\5\3\6\6\3\7\7\3\b\b\3")
        buf.write(u"\t\t\3\n\n\3\13\13\3\f\f\3\r\r\3\16\16\3\17\17\3\20\20")
        buf.write(u"\3\21\21\2\3\2")
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
    LLL_BRACE = 11
    RRR_BRACE = 12
    LL_BRACE = 13
    RR_BRACE = 14
    L_BRACE = 15
    R_BRACE = 16
    ENTITY_TYPE = 17
    BOOL = 18
    NUMBER = 19
    INT_NUMBER = 20
    FLOAT_NUMBER = 21
    STRING = 22
    WS = 23
    NAME = 24
    COMMENT_DATA = 25
    DATA = 26
    DOUBLE_PIPE = 27
    PIPE = 28
    SLASH = 29
    AMP = 30
    HASH = 31
    GREATER = 32
    HAT = 33
    EQUAL = 34
    BANG = 35
    DOT = 36
    COMMA = 37
    PERCENT = 38
    TILDA = 39
    COMMAT = 40
    QUESTION = 41
    UNKNOWN = 42

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'['", u"']'", u"'(('", u"'))'", u"'('", u"')'", u"'{{{'", 
            u"'}}}'", u"'{{'", u"'}}'", u"'{'", u"'}'" ]

    symbolicNames = [ u"<INVALID>",
            u"LL_BRACK", u"RR_BRACK", u"LL_COMMENT_BRACK", u"RR_COMMENT_BRACK", 
            u"L_BRACK", u"R_BRACK", u"LL_PAREN", u"RR_PAREN", u"L_PAREN", 
            u"R_PAREN", u"LLL_BRACE", u"RRR_BRACE", u"LL_BRACE", u"RR_BRACE", 
            u"L_BRACE", u"R_BRACE", u"ENTITY_TYPE", u"BOOL", u"NUMBER", 
            u"INT_NUMBER", u"FLOAT_NUMBER", u"STRING", u"WS", u"NAME", u"COMMENT_DATA", 
            u"DATA", u"DOUBLE_PIPE", u"PIPE", u"SLASH", u"AMP", u"HASH", 
            u"GREATER", u"HAT", u"EQUAL", u"BANG", u"DOT", u"COMMA", u"PERCENT", 
            u"TILDA", u"COMMAT", u"QUESTION", u"UNKNOWN" ]

    ruleNames = [ u"LL_BRACK", u"RR_BRACK", u"LL_COMMENT_BRACK", u"RR_COMMENT_BRACK", 
                  u"L_BRACK", u"R_BRACK", u"LL_PAREN", u"RR_PAREN", u"L_PAREN", 
                  u"R_PAREN", u"LLL_BRACE", u"RRR_BRACE", u"LL_BRACE", u"RR_BRACE", 
                  u"L_BRACE", u"R_BRACE", u"ENTITY_TYPE", u"BOOL", u"NUMBER", 
                  u"INT_NUMBER", u"FLOAT_NUMBER", u"STRING", u"STRING_ESC_SEQ", 
                  u"WS", u"NAME", u"NAME_LETTERS", u"NAME_NUMBERS", u"COMMENT_DATA", 
                  u"DATA", u"DOUBLE_PIPE", u"PIPE", u"SLASH", u"AMP", u"HASH", 
                  u"GREATER", u"HAT", u"EQUAL", u"BANG", u"DOT", u"COMMA", 
                  u"PERCENT", u"TILDA", u"COMMAT", u"QUESTION", u"UNKNOWN" ]

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
    		actions[10] = self.LLL_BRACE_action 
    		actions[11] = self.RRR_BRACE_action 
    		actions[12] = self.LL_BRACE_action 
    		actions[13] = self.RR_BRACE_action 
    		actions[14] = self.L_BRACE_action 
    		actions[15] = self.R_BRACE_action 
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

     

    def LLL_BRACE_action(self, localctx , actionIndex):
        if actionIndex == 10:

            self.open_bracket(current='{{{')
            self.state['choice_short'] = True

     

    def RRR_BRACE_action(self, localctx , actionIndex):
        if actionIndex == 11:

            self.close_bracket(expected='{{{')
            self.state['choice_short'] = False

     

    def LL_BRACE_action(self, localctx , actionIndex):
        if actionIndex == 12:

            self.open_bracket(current='{{')
            self.state['choice'] = True

     

    def RR_BRACE_action(self, localctx , actionIndex):
        if actionIndex == 13:

            self.close_bracket(expected='{{')
            self.state['choice'] = False

     

    def L_BRACE_action(self, localctx , actionIndex):
        if actionIndex == 14:

            self.open_bracket(current='{')

     

    def R_BRACE_action(self, localctx , actionIndex):
        if actionIndex == 15:

            self.close_bracket(expected='{')

     

    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates is None:
            preds = dict()
            preds[0] = self.LL_BRACK_sempred
            preds[1] = self.RR_BRACK_sempred
            preds[2] = self.LL_COMMENT_BRACK_sempred
            preds[3] = self.RR_COMMENT_BRACK_sempred
            preds[16] = self.ENTITY_TYPE_sempred
            preds[17] = self.BOOL_sempred
            preds[18] = self.NUMBER_sempred
            preds[19] = self.INT_NUMBER_sempred
            preds[20] = self.FLOAT_NUMBER_sempred
            preds[21] = self.STRING_sempred
            preds[23] = self.WS_sempred
            preds[24] = self.NAME_sempred
            preds[27] = self.COMMENT_DATA_sempred
            preds[28] = self.DATA_sempred
            preds[29] = self.DOUBLE_PIPE_sempred
            preds[30] = self.PIPE_sempred
            preds[31] = self.SLASH_sempred
            preds[32] = self.AMP_sempred
            preds[33] = self.HASH_sempred
            preds[34] = self.GREATER_sempred
            preds[35] = self.HAT_sempred
            preds[36] = self.EQUAL_sempred
            preds[37] = self.BANG_sempred
            preds[38] = self.DOT_sempred
            preds[39] = self.COMMA_sempred
            preds[40] = self.PERCENT_sempred
            preds[41] = self.TILDA_sempred
            preds[42] = self.COMMAT_sempred
            preds[43] = self.QUESTION_sempred
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
         

    def BOOL_sempred(self, localctx, predIndex):
            if predIndex == 5:
                return self.state['tag'] and not self.state['comment']
         

    def NUMBER_sempred(self, localctx, predIndex):
            if predIndex == 6:
                return self.state['tag'] and not self.state['comment']
         

    def INT_NUMBER_sempred(self, localctx, predIndex):
            if predIndex == 7:
                return self.state['tag'] and not self.state['comment']
         

    def FLOAT_NUMBER_sempred(self, localctx, predIndex):
            if predIndex == 8:
                return self.state['tag'] and not self.state['comment']
         

    def STRING_sempred(self, localctx, predIndex):
            if predIndex == 9:
                return self.state['tag'] and not self.state['comment']
         

    def WS_sempred(self, localctx, predIndex):
            if predIndex == 10:
                return self.state['tag'] and not self.state['comment']
         

    def NAME_sempred(self, localctx, predIndex):
            if predIndex == 11:
                return self.state['tag'] and not self.state['comment']
         

    def COMMENT_DATA_sempred(self, localctx, predIndex):
            if predIndex == 12:
                return self.state['tag'] and self.state['comment']
         

    def DATA_sempred(self, localctx, predIndex):
            if predIndex == 13:
                return not self.state['tag']
         

    def DOUBLE_PIPE_sempred(self, localctx, predIndex):
            if predIndex == 14:
                return self.state['choice'] and not self.state['tag']
         

    def PIPE_sempred(self, localctx, predIndex):
            if predIndex == 15:
                return self.state['tag']
         

    def SLASH_sempred(self, localctx, predIndex):
            if predIndex == 16:
                return self.state['tag']
         

    def AMP_sempred(self, localctx, predIndex):
            if predIndex == 17:
                return self.state['tag']
         

    def HASH_sempred(self, localctx, predIndex):
            if predIndex == 18:
                return self.state['tag']
         

    def GREATER_sempred(self, localctx, predIndex):
            if predIndex == 19:
                return self.state['tag']
         

    def HAT_sempred(self, localctx, predIndex):
            if predIndex == 20:
                return self.state['tag']
         

    def EQUAL_sempred(self, localctx, predIndex):
            if predIndex == 21:
                return self.state['tag']
         

    def BANG_sempred(self, localctx, predIndex):
            if predIndex == 22:
                return self.state['tag']
         

    def DOT_sempred(self, localctx, predIndex):
            if predIndex == 23:
                return self.state['tag']
         

    def COMMA_sempred(self, localctx, predIndex):
            if predIndex == 24:
                return self.state['tag']
         

    def PERCENT_sempred(self, localctx, predIndex):
            if predIndex == 25:
                return self.state['tag']
         

    def TILDA_sempred(self, localctx, predIndex):
            if predIndex == 26:
                return self.state['tag']
         

    def COMMAT_sempred(self, localctx, predIndex):
            if predIndex == 27:
                return self.state['tag']
         

    def QUESTION_sempred(self, localctx, predIndex):
            if predIndex == 28:
                return self.state['tag']
         


