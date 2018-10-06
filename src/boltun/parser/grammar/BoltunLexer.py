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
        buf.write(u"*\u0129\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write(u"\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write(u"\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write(u"\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write(u"\3\20\3\20\3\20\3\20\5\20\u009d\n\20\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00a9\n\21\3\22")
        buf.write(u"\3\22\3\22\5\22\u00ae\n\22\3\23\3\23\6\23\u00b2\n\23")
        buf.write(u"\r\23\16\23\u00b3\3\24\3\24\6\24\u00b8\n\24\r\24\16\24")
        buf.write(u"\u00b9\3\24\3\24\7\24\u00be\n\24\f\24\16\24\u00c1\13")
        buf.write(u"\24\3\25\3\25\3\25\3\25\7\25\u00c7\n\25\f\25\16\25\u00ca")
        buf.write(u"\13\25\3\25\3\25\3\25\3\25\7\25\u00d0\n\25\f\25\16\25")
        buf.write(u"\u00d3\13\25\3\25\5\25\u00d6\n\25\3\26\3\26\3\26\3\27")
        buf.write(u"\3\27\6\27\u00dd\n\27\r\27\16\27\u00de\3\27\3\27\3\30")
        buf.write(u"\3\30\6\30\u00e5\n\30\r\30\16\30\u00e6\3\30\3\30\7\30")
        buf.write(u"\u00eb\n\30\f\30\16\30\u00ee\13\30\3\31\3\31\3\32\3\32")
        buf.write(u"\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3")
        buf.write(u"\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write(u"\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3")
        buf.write(u"\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\2\2-\3\3")
        buf.write(u"\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write(u"\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\2-\27/\30\61")
        buf.write(u"\2\63\2\65\31\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%")
        buf.write(u"O&Q\'S(U)W*\3\2\6\6\2\f\f\16\17))^^\6\2\f\f\16\17$$^")
        buf.write(u"^\5\2\13\f\16\17\"\"\6\2//C\\aac|\2\u0135\2\3\3\2\2\2")
        buf.write(u"\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write(u"\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write(u"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write(u"\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2")
        buf.write(u"\2\2\'\3\2\2\2\2)\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\65")
        buf.write(u"\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2")
        buf.write(u"\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2")
        buf.write(u"\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3")
        buf.write(u"\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\3Y\3\2\2\2\5")
        buf.write(u"_\3\2\2\2\7e\3\2\2\2\tl\3\2\2\2\13r\3\2\2\2\ru\3\2\2")
        buf.write(u"\2\17x\3\2\2\2\21}\3\2\2\2\23\u0082\3\2\2\2\25\u0085")
        buf.write(u"\3\2\2\2\27\u0088\3\2\2\2\31\u008d\3\2\2\2\33\u0092\3")
        buf.write(u"\2\2\2\35\u0095\3\2\2\2\37\u0098\3\2\2\2!\u00a8\3\2\2")
        buf.write(u"\2#\u00ad\3\2\2\2%\u00af\3\2\2\2\'\u00b5\3\2\2\2)\u00c2")
        buf.write(u"\3\2\2\2+\u00d7\3\2\2\2-\u00da\3\2\2\2/\u00e2\3\2\2\2")
        buf.write(u"\61\u00ef\3\2\2\2\63\u00f1\3\2\2\2\65\u00f3\3\2\2\2\67")
        buf.write(u"\u00f6\3\2\2\29\u00f9\3\2\2\2;\u00fd\3\2\2\2=\u0100\3")
        buf.write(u"\2\2\2?\u0103\3\2\2\2A\u0106\3\2\2\2C\u0109\3\2\2\2E")
        buf.write(u"\u010c\3\2\2\2G\u010f\3\2\2\2I\u0112\3\2\2\2K\u0115\3")
        buf.write(u"\2\2\2M\u0118\3\2\2\2O\u011b\3\2\2\2Q\u011e\3\2\2\2S")
        buf.write(u"\u0121\3\2\2\2U\u0124\3\2\2\2W\u0127\3\2\2\2YZ\6\2\2")
        buf.write(u"\2Z[\7]\2\2[\\\7]\2\2\\]\3\2\2\2]^\b\2\2\2^\4\3\2\2\2")
        buf.write(u"_`\6\3\3\2`a\7_\2\2ab\7_\2\2bc\3\2\2\2cd\b\3\3\2d\6\3")
        buf.write(u"\2\2\2ef\6\4\4\2fg\7]\2\2gh\7]\2\2hi\7%\2\2ij\3\2\2\2")
        buf.write(u"jk\b\4\4\2k\b\3\2\2\2lm\6\5\5\2mn\7_\2\2no\7_\2\2op\3")
        buf.write(u"\2\2\2pq\b\5\5\2q\n\3\2\2\2rs\7]\2\2st\b\6\6\2t\f\3\2")
        buf.write(u"\2\2uv\7_\2\2vw\b\7\7\2w\16\3\2\2\2xy\7*\2\2yz\7*\2\2")
        buf.write(u"z{\3\2\2\2{|\b\b\b\2|\20\3\2\2\2}~\7+\2\2~\177\7+\2\2")
        buf.write(u"\177\u0080\3\2\2\2\u0080\u0081\b\t\t\2\u0081\22\3\2\2")
        buf.write(u"\2\u0082\u0083\7*\2\2\u0083\u0084\b\n\n\2\u0084\24\3")
        buf.write(u"\2\2\2\u0085\u0086\7+\2\2\u0086\u0087\b\13\13\2\u0087")
        buf.write(u"\26\3\2\2\2\u0088\u0089\7}\2\2\u0089\u008a\7}\2\2\u008a")
        buf.write(u"\u008b\3\2\2\2\u008b\u008c\b\f\f\2\u008c\30\3\2\2\2\u008d")
        buf.write(u"\u008e\7\177\2\2\u008e\u008f\7\177\2\2\u008f\u0090\3")
        buf.write(u"\2\2\2\u0090\u0091\b\r\r\2\u0091\32\3\2\2\2\u0092\u0093")
        buf.write(u"\7}\2\2\u0093\u0094\b\16\16\2\u0094\34\3\2\2\2\u0095")
        buf.write(u"\u0096\7\177\2\2\u0096\u0097\b\17\17\2\u0097\36\3\2\2")
        buf.write(u"\2\u0098\u009c\6\20\6\2\u0099\u009d\5O(\2\u009a\u009d")
        buf.write(u"\5Q)\2\u009b\u009d\5S*\2\u009c\u0099\3\2\2\2\u009c\u009a")
        buf.write(u"\3\2\2\2\u009c\u009b\3\2\2\2\u009d \3\2\2\2\u009e\u009f")
        buf.write(u"\6\21\7\2\u009f\u00a0\7V\2\2\u00a0\u00a1\7t\2\2\u00a1")
        buf.write(u"\u00a2\7w\2\2\u00a2\u00a9\7g\2\2\u00a3\u00a4\7H\2\2\u00a4")
        buf.write(u"\u00a5\7c\2\2\u00a5\u00a6\7n\2\2\u00a6\u00a7\7u\2\2\u00a7")
        buf.write(u"\u00a9\7g\2\2\u00a8\u009e\3\2\2\2\u00a8\u00a3\3\2\2\2")
        buf.write(u"\u00a9\"\3\2\2\2\u00aa\u00ab\6\22\b\2\u00ab\u00ae\5%")
        buf.write(u"\23\2\u00ac\u00ae\5\'\24\2\u00ad\u00aa\3\2\2\2\u00ad")
        buf.write(u"\u00ac\3\2\2\2\u00ae$\3\2\2\2\u00af\u00b1\6\23\t\2\u00b0")
        buf.write(u"\u00b2\4\62;\2\u00b1\u00b0\3\2\2\2\u00b2\u00b3\3\2\2")
        buf.write(u"\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4&\3\2")
        buf.write(u"\2\2\u00b5\u00b7\6\24\n\2\u00b6\u00b8\5%\23\2\u00b7\u00b6")
        buf.write(u"\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9")
        buf.write(u"\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bf\5K&\2")
        buf.write(u"\u00bc\u00be\5%\23\2\u00bd\u00bc\3\2\2\2\u00be\u00c1")
        buf.write(u"\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0")
        buf.write(u"(\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00d5\6\25\13\2\u00c3")
        buf.write(u"\u00c8\7)\2\2\u00c4\u00c7\5+\26\2\u00c5\u00c7\n\2\2\2")
        buf.write(u"\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00ca")
        buf.write(u"\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write(u"\u00cb\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00d6\7)\2\2")
        buf.write(u"\u00cc\u00d1\7$\2\2\u00cd\u00d0\5+\26\2\u00ce\u00d0\n")
        buf.write(u"\3\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0")
        buf.write(u"\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2")
        buf.write(u"\2\u00d2\u00d4\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d6")
        buf.write(u"\7$\2\2\u00d5\u00c3\3\2\2\2\u00d5\u00cc\3\2\2\2\u00d6")
        buf.write(u"*\3\2\2\2\u00d7\u00d8\7^\2\2\u00d8\u00d9\13\2\2\2\u00d9")
        buf.write(u",\3\2\2\2\u00da\u00dc\6\27\f\2\u00db\u00dd\t\4\2\2\u00dc")
        buf.write(u"\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00dc\3\2\2")
        buf.write(u"\2\u00de\u00df\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1")
        buf.write(u"\b\27\20\2\u00e1.\3\2\2\2\u00e2\u00e4\6\30\r\2\u00e3")
        buf.write(u"\u00e5\5\61\31\2\u00e4\u00e3\3\2\2\2\u00e5\u00e6\3\2")
        buf.write(u"\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00ec")
        buf.write(u"\3\2\2\2\u00e8\u00eb\5\61\31\2\u00e9\u00eb\5\63\32\2")
        buf.write(u"\u00ea\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb\u00ee")
        buf.write(u"\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed")
        buf.write(u"\60\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0\t\5\2\2\u00f0")
        buf.write(u"\62\3\2\2\2\u00f1\u00f2\4\62;\2\u00f2\64\3\2\2\2\u00f3")
        buf.write(u"\u00f4\6\33\16\2\u00f4\u00f5\13\2\2\2\u00f5\66\3\2\2")
        buf.write(u"\2\u00f6\u00f7\6\34\17\2\u00f7\u00f8\13\2\2\2\u00f88")
        buf.write(u"\3\2\2\2\u00f9\u00fa\6\35\20\2\u00fa\u00fb\7~\2\2\u00fb")
        buf.write(u"\u00fc\7~\2\2\u00fc:\3\2\2\2\u00fd\u00fe\6\36\21\2\u00fe")
        buf.write(u"\u00ff\7~\2\2\u00ff<\3\2\2\2\u0100\u0101\6\37\22\2\u0101")
        buf.write(u"\u0102\7\61\2\2\u0102>\3\2\2\2\u0103\u0104\6 \23\2\u0104")
        buf.write(u"\u0105\7(\2\2\u0105@\3\2\2\2\u0106\u0107\6!\24\2\u0107")
        buf.write(u"\u0108\7%\2\2\u0108B\3\2\2\2\u0109\u010a\6\"\25\2\u010a")
        buf.write(u"\u010b\7@\2\2\u010bD\3\2\2\2\u010c\u010d\6#\26\2\u010d")
        buf.write(u"\u010e\7`\2\2\u010eF\3\2\2\2\u010f\u0110\6$\27\2\u0110")
        buf.write(u"\u0111\7?\2\2\u0111H\3\2\2\2\u0112\u0113\6%\30\2\u0113")
        buf.write(u"\u0114\7#\2\2\u0114J\3\2\2\2\u0115\u0116\6&\31\2\u0116")
        buf.write(u"\u0117\7\60\2\2\u0117L\3\2\2\2\u0118\u0119\6\'\32\2\u0119")
        buf.write(u"\u011a\7.\2\2\u011aN\3\2\2\2\u011b\u011c\6(\33\2\u011c")
        buf.write(u"\u011d\7\'\2\2\u011dP\3\2\2\2\u011e\u011f\6)\34\2\u011f")
        buf.write(u"\u0120\7\u0080\2\2\u0120R\3\2\2\2\u0121\u0122\6*\35\2")
        buf.write(u"\u0122\u0123\7B\2\2\u0123T\3\2\2\2\u0124\u0125\6+\36")
        buf.write(u"\2\u0125\u0126\7A\2\2\u0126V\3\2\2\2\u0127\u0128\13\2")
        buf.write(u"\2\2\u0128X\3\2\2\2\22\2\u009c\u00a8\u00ad\u00b3\u00b9")
        buf.write(u"\u00bf\u00c6\u00c8\u00cf\u00d1\u00d5\u00de\u00e6\u00ea")
        buf.write(u"\u00ec\21\3\2\2\3\3\3\3\4\4\3\5\5\3\6\6\3\7\7\3\b\b\3")
        buf.write(u"\t\t\3\n\n\3\13\13\3\f\f\3\r\r\3\16\16\3\17\17\2\3\2")
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
    BOOL = 16
    NUMBER = 17
    INT_NUMBER = 18
    FLOAT_NUMBER = 19
    STRING = 20
    WS = 21
    NAME = 22
    COMMENT_DATA = 23
    DATA = 24
    DOUBLE_PIPE = 25
    PIPE = 26
    SLASH = 27
    AMP = 28
    HASH = 29
    GREATER = 30
    HAT = 31
    EQUAL = 32
    BANG = 33
    DOT = 34
    COMMA = 35
    PERCENT = 36
    TILDA = 37
    COMMAT = 38
    QUESTION = 39
    UNKNOWN = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'['", u"']'", u"'(('", u"'))'", u"'('", u"')'", u"'{{'", u"'}}'", 
            u"'{'", u"'}'" ]

    symbolicNames = [ u"<INVALID>",
            u"LL_BRACK", u"RR_BRACK", u"LL_COMMENT_BRACK", u"RR_COMMENT_BRACK", 
            u"L_BRACK", u"R_BRACK", u"LL_PAREN", u"RR_PAREN", u"L_PAREN", 
            u"R_PAREN", u"LL_BRACE", u"RR_BRACE", u"L_BRACE", u"R_BRACE", 
            u"ENTITY_TYPE", u"BOOL", u"NUMBER", u"INT_NUMBER", u"FLOAT_NUMBER", 
            u"STRING", u"WS", u"NAME", u"COMMENT_DATA", u"DATA", u"DOUBLE_PIPE", 
            u"PIPE", u"SLASH", u"AMP", u"HASH", u"GREATER", u"HAT", u"EQUAL", 
            u"BANG", u"DOT", u"COMMA", u"PERCENT", u"TILDA", u"COMMAT", 
            u"QUESTION", u"UNKNOWN" ]

    ruleNames = [ u"LL_BRACK", u"RR_BRACK", u"LL_COMMENT_BRACK", u"RR_COMMENT_BRACK", 
                  u"L_BRACK", u"R_BRACK", u"LL_PAREN", u"RR_PAREN", u"L_PAREN", 
                  u"R_PAREN", u"LL_BRACE", u"RR_BRACE", u"L_BRACE", u"R_BRACE", 
                  u"ENTITY_TYPE", u"BOOL", u"NUMBER", u"INT_NUMBER", u"FLOAT_NUMBER", 
                  u"STRING", u"STRING_ESC_SEQ", u"WS", u"NAME", u"NAME_LETTERS", 
                  u"NAME_NUMBERS", u"COMMENT_DATA", u"DATA", u"DOUBLE_PIPE", 
                  u"PIPE", u"SLASH", u"AMP", u"HASH", u"GREATER", u"HAT", 
                  u"EQUAL", u"BANG", u"DOT", u"COMMA", u"PERCENT", u"TILDA", 
                  u"COMMAT", u"QUESTION", u"UNKNOWN" ]

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
            preds[15] = self.BOOL_sempred
            preds[16] = self.NUMBER_sempred
            preds[17] = self.INT_NUMBER_sempred
            preds[18] = self.FLOAT_NUMBER_sempred
            preds[19] = self.STRING_sempred
            preds[21] = self.WS_sempred
            preds[22] = self.NAME_sempred
            preds[25] = self.COMMENT_DATA_sempred
            preds[26] = self.DATA_sempred
            preds[27] = self.DOUBLE_PIPE_sempred
            preds[28] = self.PIPE_sempred
            preds[29] = self.SLASH_sempred
            preds[30] = self.AMP_sempred
            preds[31] = self.HASH_sempred
            preds[32] = self.GREATER_sempred
            preds[33] = self.HAT_sempred
            preds[34] = self.EQUAL_sempred
            preds[35] = self.BANG_sempred
            preds[36] = self.DOT_sempred
            preds[37] = self.COMMA_sempred
            preds[38] = self.PERCENT_sempred
            preds[39] = self.TILDA_sempred
            preds[40] = self.COMMAT_sempred
            preds[41] = self.QUESTION_sempred
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
         


