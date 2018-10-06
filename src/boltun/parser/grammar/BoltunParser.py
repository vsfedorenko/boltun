# Generated from /Users/vfedorenko/Developer/Business/Projects/NeuralNetworks/nlu_data_generator/src/boltun/parser/grammar/Boltun.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


import ast
import logging

from antlr4 import *

from .nodes import AliasNode, CallNode, ChoiceNode, CommentNode, ContentNode, \
    DataNode, Filter, IntentNode, RootNode, SlotNode
from ...util.collections import Stack

logger = logging.getLogger(__name__)

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"*\u00c3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\7\2#\n\2\f\2\16")
        buf.write(u"\2&\13\2\3\2\5\2)\n\2\3\3\3\3\6\3-\n\3\r\3\16\3.\3\4")
        buf.write(u"\6\4\62\n\4\r\4\16\4\63\3\4\3\4\3\5\3\5\3\6\3\6\3\6\5")
        buf.write(u"\6=\n\6\3\7\3\7\5\7A\n\7\3\7\3\7\5\7E\n\7\7\7G\n\7\f")
        buf.write(u"\7\16\7J\13\7\3\7\3\7\3\7\3\b\3\b\3\b\5\bR\n\b\3\b\3")
        buf.write(u"\b\3\b\3\b\3\b\7\bY\n\b\f\b\16\b\\\13\b\5\b^\n\b\3\b")
        buf.write(u"\5\ba\n\b\3\b\7\bd\n\b\f\b\16\bg\13\b\3\b\3\b\3\b\3\t")
        buf.write(u"\3\t\3\n\3\n\3\n\5\nq\n\n\3\n\3\n\5\nu\n\n\3\n\3\n\5")
        buf.write(u"\ny\n\n\3\n\7\n|\n\n\f\n\16\n\177\13\n\3\n\3\n\3\n\3")
        buf.write(u"\13\3\13\3\13\5\13\u0087\n\13\3\13\5\13\u008a\n\13\3")
        buf.write(u"\13\5\13\u008d\n\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u0095")
        buf.write(u"\n\f\f\f\16\f\u0098\13\f\3\f\3\f\3\f\7\f\u009d\n\f\f")
        buf.write(u"\f\16\f\u00a0\13\f\3\f\3\f\7\f\u00a4\n\f\f\f\16\f\u00a7")
        buf.write(u"\13\f\5\f\u00a9\n\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\7\20\u00bb\n")
        buf.write(u"\20\f\20\16\20\u00be\13\20\3\20\3\20\3\20\3\20\5He\u00bc")
        buf.write(u"\2\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2\3\4\2")
        buf.write(u"\22\23\26\26\2\u00cf\2$\3\2\2\2\4,\3\2\2\2\6\61\3\2\2")
        buf.write(u"\2\b\67\3\2\2\2\n<\3\2\2\2\f>\3\2\2\2\16N\3\2\2\2\20")
        buf.write(u"k\3\2\2\2\22m\3\2\2\2\24\u0083\3\2\2\2\26\u0090\3\2\2")
        buf.write(u"\2\30\u00ad\3\2\2\2\32\u00b0\3\2\2\2\34\u00b5\3\2\2\2")
        buf.write(u"\36\u00b8\3\2\2\2 #\5\b\5\2!#\5\4\3\2\" \3\2\2\2\"!\3")
        buf.write(u"\2\2\2#&\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%(\3\2\2\2&$\3\2")
        buf.write(u"\2\2\')\7\2\2\3(\'\3\2\2\2()\3\2\2\2)\3\3\2\2\2*-\5\n")
        buf.write(u"\6\2+-\5\6\4\2,*\3\2\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2")
        buf.write(u"\2./\3\2\2\2/\5\3\2\2\2\60\62\7\32\2\2\61\60\3\2\2\2")
        buf.write(u"\62\63\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\65\3\2")
        buf.write(u"\2\2\65\66\b\4\1\2\66\7\3\2\2\2\678\5\f\7\28\t\3\2\2")
        buf.write(u"\29=\5\16\b\2:=\5\22\n\2;=\5\36\20\2<9\3\2\2\2<:\3\2")
        buf.write(u"\2\2<;\3\2\2\2=\13\3\2\2\2>@\7\r\2\2?A\5\4\3\2@?\3\2")
        buf.write(u"\2\2@A\3\2\2\2AH\3\2\2\2BD\7\33\2\2CE\5\4\3\2DC\3\2\2")
        buf.write(u"\2DE\3\2\2\2EG\3\2\2\2FB\3\2\2\2GJ\3\2\2\2HI\3\2\2\2")
        buf.write(u"HF\3\2\2\2IK\3\2\2\2JH\3\2\2\2KL\7\16\2\2LM\b\7\1\2M")
        buf.write(u"\r\3\2\2\2NO\7\3\2\2OQ\5\20\t\2PR\7)\2\2QP\3\2\2\2QR")
        buf.write(u"\3\2\2\2RS\3\2\2\2S]\7\30\2\2TU\7\37\2\2UZ\7\30\2\2V")
        buf.write(u"W\7\37\2\2WY\7\30\2\2XV\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2")
        buf.write(u"Z[\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2]T\3\2\2\2]^\3\2\2\2^")
        buf.write(u"`\3\2\2\2_a\7)\2\2`_\3\2\2\2`a\3\2\2\2ae\3\2\2\2bd\5")
        buf.write(u"\24\13\2cb\3\2\2\2dg\3\2\2\2ef\3\2\2\2ec\3\2\2\2fh\3")
        buf.write(u"\2\2\2ge\3\2\2\2hi\7\4\2\2ij\b\b\1\2j\17\3\2\2\2kl\7")
        buf.write(u"\21\2\2l\21\3\2\2\2mn\7\3\2\2np\7 \2\2oq\7)\2\2po\3\2")
        buf.write(u"\2\2pq\3\2\2\2qr\3\2\2\2rt\7\30\2\2su\7)\2\2ts\3\2\2")
        buf.write(u"\2tu\3\2\2\2uv\3\2\2\2vx\5\26\f\2wy\7)\2\2xw\3\2\2\2")
        buf.write(u"xy\3\2\2\2y}\3\2\2\2z|\5\24\13\2{z\3\2\2\2|\177\3\2\2")
        buf.write(u"\2}{\3\2\2\2}~\3\2\2\2~\u0080\3\2\2\2\177}\3\2\2\2\u0080")
        buf.write(u"\u0081\7\4\2\2\u0081\u0082\b\n\1\2\u0082\23\3\2\2\2\u0083")
        buf.write(u"\u0084\7\34\2\2\u0084\u0086\7\30\2\2\u0085\u0087\7)\2")
        buf.write(u"\2\u0086\u0085\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0089")
        buf.write(u"\3\2\2\2\u0088\u008a\5\26\f\2\u0089\u0088\3\2\2\2\u0089")
        buf.write(u"\u008a\3\2\2\2\u008a\u008c\3\2\2\2\u008b\u008d\7)\2\2")
        buf.write(u"\u008c\u008b\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e")
        buf.write(u"\3\2\2\2\u008e\u008f\b\13\1\2\u008f\25\3\2\2\2\u0090")
        buf.write(u"\u00a8\7\13\2\2\u0091\u0096\5\32\16\2\u0092\u0093\7%")
        buf.write(u"\2\2\u0093\u0095\5\32\16\2\u0094\u0092\3\2\2\2\u0095")
        buf.write(u"\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2")
        buf.write(u"\2\u0097\u00a9\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009e")
        buf.write(u"\5\30\r\2\u009a\u009b\7%\2\2\u009b\u009d\5\30\r\2\u009c")
        buf.write(u"\u009a\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2")
        buf.write(u"\2\u009e\u009f\3\2\2\2\u009f\u00a5\3\2\2\2\u00a0\u009e")
        buf.write(u"\3\2\2\2\u00a1\u00a2\7%\2\2\u00a2\u00a4\5\32\16\2\u00a3")
        buf.write(u"\u00a1\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2")
        buf.write(u"\2\u00a5\u00a6\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5")
        buf.write(u"\3\2\2\2\u00a8\u0091\3\2\2\2\u00a8\u0099\3\2\2\2\u00a9")
        buf.write(u"\u00aa\3\2\2\2\u00aa\u00ab\7\f\2\2\u00ab\u00ac\b\f\1")
        buf.write(u"\2\u00ac\27\3\2\2\2\u00ad\u00ae\5\34\17\2\u00ae\u00af")
        buf.write(u"\b\r\1\2\u00af\31\3\2\2\2\u00b0\u00b1\7\30\2\2\u00b1")
        buf.write(u"\u00b2\7\"\2\2\u00b2\u00b3\5\34\17\2\u00b3\u00b4\b\16")
        buf.write(u"\1\2\u00b4\33\3\2\2\2\u00b5\u00b6\t\2\2\2\u00b6\u00b7")
        buf.write(u"\b\17\1\2\u00b7\35\3\2\2\2\u00b8\u00bc\7\5\2\2\u00b9")
        buf.write(u"\u00bb\7\31\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2")
        buf.write(u"\2\u00bc\u00bd\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00bf")
        buf.write(u"\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\7\6\2\2\u00c0")
        buf.write(u"\u00c1\b\20\1\2\u00c1\37\3\2\2\2\35\"$(,.\63<@DHQZ]`")
        buf.write(u"eptx}\u0086\u0089\u008c\u0096\u009e\u00a5\u00a8\u00bc")
        return buf.getvalue()


class BoltunParser ( Parser ):

    grammarFileName = "Boltun.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'['", u"']'", u"'(('", u"'))'", u"'('", 
                     u"')'", u"'{{'", u"'}}'", u"'{'", u"'}'" ]

    symbolicNames = [ u"<INVALID>", u"LL_BRACK", u"RR_BRACK", u"LL_COMMENT_BRACK", 
                      u"RR_COMMENT_BRACK", u"L_BRACK", u"R_BRACK", u"LL_PAREN", 
                      u"RR_PAREN", u"L_PAREN", u"R_PAREN", u"LL_BRACE", 
                      u"RR_BRACE", u"L_BRACE", u"R_BRACE", u"ENTITY_TYPE", 
                      u"BOOL", u"NUMBER", u"INT_NUMBER", u"FLOAT_NUMBER", 
                      u"STRING", u"WS", u"NAME", u"COMMENT_DATA", u"DATA", 
                      u"DOUBLE_PIPE", u"PIPE", u"SLASH", u"AMP", u"HASH", 
                      u"GREATER", u"HAT", u"EQUAL", u"BANG", u"DOT", u"COMMA", 
                      u"PERCENT", u"TILDA", u"COMMAT", u"QUESTION", u"UNKNOWN" ]

    RULE_document = 0
    RULE_content = 1
    RULE_data = 2
    RULE_polyadic_tag = 3
    RULE_unary_tag = 4
    RULE_choice_tag = 5
    RULE_entity_tag = 6
    RULE_entity_type = 7
    RULE_call_tag = 8
    RULE_fltr = 9
    RULE_attr = 10
    RULE_attr_arg_def = 11
    RULE_attr_kw_arg_def = 12
    RULE_attr_value = 13
    RULE_comment_tag = 14

    ruleNames =  [ u"document", u"content", u"data", u"polyadic_tag", u"unary_tag", 
                   u"choice_tag", u"entity_tag", u"entity_type", u"call_tag", 
                   u"fltr", u"attr", u"attr_arg_def", u"attr_kw_arg_def", 
                   u"attr_value", u"comment_tag" ]

    EOF = Token.EOF
    LL_BRACK=1
    RR_BRACK=2
    LL_COMMENT_BRACK=3
    RR_COMMENT_BRACK=4
    L_BRACK=5
    R_BRACK=6
    LL_PAREN=7
    RR_PAREN=8
    L_PAREN=9
    R_PAREN=10
    LL_BRACE=11
    RR_BRACE=12
    L_BRACE=13
    R_BRACE=14
    ENTITY_TYPE=15
    BOOL=16
    NUMBER=17
    INT_NUMBER=18
    FLOAT_NUMBER=19
    STRING=20
    WS=21
    NAME=22
    COMMENT_DATA=23
    DATA=24
    DOUBLE_PIPE=25
    PIPE=26
    SLASH=27
    AMP=28
    HASH=29
    GREATER=30
    HAT=31
    EQUAL=32
    BANG=33
    DOT=34
    COMMA=35
    PERCENT=36
    TILDA=37
    COMMAT=38
    QUESTION=39
    UNKNOWN=40

    def __init__(self, input, output=sys.stdout):
        super(BoltunParser, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    @property
    def node_stack(self):
        try:
            return self._node_stack
        except AttributeError:
            self._node_stack = Stack()
            self._node_stack.push(RootNode())
            return self._node_stack

    def get_start_pos(self, ctx):
        if not ctx:
            return None
        return ctx.start.start if ctx.start else None

    def get_stop_pos(self, ctx):
        if not ctx:
            return None
        return ctx.stop.stop if ctx.stop else None



    class DocumentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.DocumentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def polyadic_tag(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BoltunParser.Polyadic_tagContext)
            else:
                return self.getTypedRuleContext(BoltunParser.Polyadic_tagContext,i)


        def content(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BoltunParser.ContentContext)
            else:
                return self.getTypedRuleContext(BoltunParser.ContentContext,i)


        def EOF(self):
            return self.getToken(BoltunParser.EOF, 0)

        def getRuleIndex(self):
            return BoltunParser.RULE_document

        def enterRule(self, listener):
            if hasattr(listener, "enterDocument"):
                listener.enterDocument(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDocument"):
                listener.exitDocument(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitDocument"):
                return visitor.visitDocument(self)
            else:
                return visitor.visitChildren(self)




    def document(self):

        localctx = BoltunParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)


        content_node = ContentNode()
        self.node_stack.push(content_node)


        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BoltunParser.LL_BRACK) | (1 << BoltunParser.LL_COMMENT_BRACK) | (1 << BoltunParser.LL_BRACE) | (1 << BoltunParser.DATA))) != 0):
                self.state = 32
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BoltunParser.LL_BRACE]:
                    self.state = 30
                    self.polyadic_tag()
                    pass
                elif token in [BoltunParser.LL_BRACK, BoltunParser.LL_COMMENT_BRACK, BoltunParser.DATA]:
                    self.state = 31
                    self.content()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 37
                self.match(BoltunParser.EOF)


            self._ctx.stop = self._input.LT(-1)


            root_node = self.node_stack.peek()
            root_node.start = self.get_start_pos(localctx)
            root_node.stop = self.get_stop_pos(localctx)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.ContentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unary_tag(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BoltunParser.Unary_tagContext)
            else:
                return self.getTypedRuleContext(BoltunParser.Unary_tagContext,i)


        def data(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BoltunParser.DataContext)
            else:
                return self.getTypedRuleContext(BoltunParser.DataContext,i)


        def getRuleIndex(self):
            return BoltunParser.RULE_content

        def enterRule(self, listener):
            if hasattr(listener, "enterContent"):
                listener.enterContent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitContent"):
                listener.exitContent(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitContent"):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = BoltunParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_content)


        content_node = ContentNode()
        self.node_stack.push(content_node)


        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 42
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [BoltunParser.LL_BRACK, BoltunParser.LL_COMMENT_BRACK]:
                        self.state = 40
                        self.unary_tag()
                        pass
                    elif token in [BoltunParser.DATA]:
                        self.state = 41
                        self.data()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 44 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self._ctx.stop = self._input.LT(-1)


            content_node = self.node_stack.pop()
            content_node.start = self.get_start_pos(localctx)
            content_node.stop = self.get_stop_pos(localctx)

            self.node_stack.peek().add_child(content_node)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DataContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.DataContext, self).__init__(parent, invokingState)
            self.parser = parser
            self._DATA = None # Token
            self.var_chars = list() # of Tokens

        def DATA(self, i=None):
            if i is None:
                return self.getTokens(BoltunParser.DATA)
            else:
                return self.getToken(BoltunParser.DATA, i)

        def getRuleIndex(self):
            return BoltunParser.RULE_data

        def enterRule(self, listener):
            if hasattr(listener, "enterData"):
                listener.enterData(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitData"):
                listener.exitData(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitData"):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = BoltunParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_data)



        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 46
                    localctx._DATA = self.match(BoltunParser.DATA)
                    localctx.var_chars.append(localctx._DATA)

                else:
                    raise NoViableAltException(self)
                self.state = 49 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)



            data_str = ''.join([c.text for c in localctx.var_chars])

            node = DataNode(data_str)


            self._ctx.stop = self._input.LT(-1)


            node.start = self.get_start_pos(localctx)
            node.stop = self.get_stop_pos(localctx)
            self.node_stack.peek().add_child(node)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Polyadic_tagContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.Polyadic_tagContext, self).__init__(parent, invokingState)
            self.parser = parser

        def choice_tag(self):
            return self.getTypedRuleContext(BoltunParser.Choice_tagContext,0)


        def getRuleIndex(self):
            return BoltunParser.RULE_polyadic_tag

        def enterRule(self, listener):
            if hasattr(listener, "enterPolyadic_tag"):
                listener.enterPolyadic_tag(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPolyadic_tag"):
                listener.exitPolyadic_tag(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitPolyadic_tag"):
                return visitor.visitPolyadic_tag(self)
            else:
                return visitor.visitChildren(self)




    def polyadic_tag(self):

        localctx = BoltunParser.Polyadic_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_polyadic_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.choice_tag()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Unary_tagContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.Unary_tagContext, self).__init__(parent, invokingState)
            self.parser = parser

        def entity_tag(self):
            return self.getTypedRuleContext(BoltunParser.Entity_tagContext,0)


        def call_tag(self):
            return self.getTypedRuleContext(BoltunParser.Call_tagContext,0)


        def comment_tag(self):
            return self.getTypedRuleContext(BoltunParser.Comment_tagContext,0)


        def getRuleIndex(self):
            return BoltunParser.RULE_unary_tag

        def enterRule(self, listener):
            if hasattr(listener, "enterUnary_tag"):
                listener.enterUnary_tag(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUnary_tag"):
                listener.exitUnary_tag(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitUnary_tag"):
                return visitor.visitUnary_tag(self)
            else:
                return visitor.visitChildren(self)




    def unary_tag(self):

        localctx = BoltunParser.Unary_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_unary_tag)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.entity_tag()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.call_tag()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.comment_tag()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Choice_tagContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.Choice_tagContext, self).__init__(parent, invokingState)
            self.parser = parser
            self._content = None # ContentContext
            self.var_content_choises = list() # of ContentContexts

        def LL_BRACE(self):
            return self.getToken(BoltunParser.LL_BRACE, 0)

        def RR_BRACE(self):
            return self.getToken(BoltunParser.RR_BRACE, 0)

        def DOUBLE_PIPE(self, i=None):
            if i is None:
                return self.getTokens(BoltunParser.DOUBLE_PIPE)
            else:
                return self.getToken(BoltunParser.DOUBLE_PIPE, i)

        def content(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BoltunParser.ContentContext)
            else:
                return self.getTypedRuleContext(BoltunParser.ContentContext,i)


        def getRuleIndex(self):
            return BoltunParser.RULE_choice_tag

        def enterRule(self, listener):
            if hasattr(listener, "enterChoice_tag"):
                listener.enterChoice_tag(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitChoice_tag"):
                listener.exitChoice_tag(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitChoice_tag"):
                return visitor.visitChoice_tag(self)
            else:
                return visitor.visitChildren(self)




    def choice_tag(self):

        localctx = BoltunParser.Choice_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_choice_tag)


        choice_node = ChoiceNode()
        self.node_stack.push(choice_node)


        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(BoltunParser.LL_BRACE)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BoltunParser.LL_BRACK) | (1 << BoltunParser.LL_COMMENT_BRACK) | (1 << BoltunParser.DATA))) != 0):
                self.state = 61
                localctx._content = self.content()
                localctx.var_content_choises.append(localctx._content)


            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 64
                    self.match(BoltunParser.DOUBLE_PIPE)
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BoltunParser.LL_BRACK) | (1 << BoltunParser.LL_COMMENT_BRACK) | (1 << BoltunParser.DATA))) != 0):
                        self.state = 65
                        localctx._content = self.content()
                        localctx.var_content_choises.append(localctx._content)

             
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 73
            self.match(BoltunParser.RR_BRACE)



            self._ctx.stop = self._input.LT(-1)


            choice_node = self.node_stack.pop()
            choice_node.start = self.get_start_pos(localctx)
            choice_node.stop = self.get_stop_pos(localctx)

            self.node_stack.peek().add_child(choice_node)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Entity_tagContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.Entity_tagContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.var_type = None # Entity_typeContext
            self.var_optional = None # Token
            self.name = None # Token
            self._NAME = None # Token
            self.var_ref_names = list() # of Tokens
            self._fltr = None # FltrContext
            self.var_fltrs = list() # of FltrContexts

        def LL_BRACK(self):
            return self.getToken(BoltunParser.LL_BRACK, 0)

        def RR_BRACK(self):
            return self.getToken(BoltunParser.RR_BRACK, 0)

        def entity_type(self):
            return self.getTypedRuleContext(BoltunParser.Entity_typeContext,0)


        def NAME(self, i=None):
            if i is None:
                return self.getTokens(BoltunParser.NAME)
            else:
                return self.getToken(BoltunParser.NAME, i)

        def HASH(self, i=None):
            if i is None:
                return self.getTokens(BoltunParser.HASH)
            else:
                return self.getToken(BoltunParser.HASH, i)

        def QUESTION(self, i=None):
            if i is None:
                return self.getTokens(BoltunParser.QUESTION)
            else:
                return self.getToken(BoltunParser.QUESTION, i)

        def fltr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BoltunParser.FltrContext)
            else:
                return self.getTypedRuleContext(BoltunParser.FltrContext,i)


        def getRuleIndex(self):
            return BoltunParser.RULE_entity_tag

        def enterRule(self, listener):
            if hasattr(listener, "enterEntity_tag"):
                listener.enterEntity_tag(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEntity_tag"):
                listener.exitEntity_tag(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitEntity_tag"):
                return visitor.visitEntity_tag(self)
            else:
                return visitor.visitChildren(self)




    def entity_tag(self):

        localctx = BoltunParser.Entity_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_entity_tag)



        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(BoltunParser.LL_BRACK)
            self.state = 77
            localctx.var_type = self.entity_type()
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BoltunParser.QUESTION:
                self.state = 78
                localctx.var_optional = self.match(BoltunParser.QUESTION)


            self.state = 81
            localctx.name = self.match(BoltunParser.NAME)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BoltunParser.HASH:
                self.state = 82
                self.match(BoltunParser.HASH)
                self.state = 83
                localctx._NAME = self.match(BoltunParser.NAME)
                localctx.var_ref_names.append(localctx._NAME)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BoltunParser.HASH:
                    self.state = 84
                    self.match(BoltunParser.HASH)
                    self.state = 85
                    localctx._NAME = self.match(BoltunParser.NAME)
                    localctx.var_ref_names.append(localctx._NAME)
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BoltunParser.QUESTION:
                self.state = 93
                localctx.var_optional = self.match(BoltunParser.QUESTION)


            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 96
                    localctx._fltr = self.fltr()
                    localctx.var_fltrs.append(localctx._fltr) 
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 102
            self.match(BoltunParser.RR_BRACK)


            node_class = None

            entity_type = (None if localctx.var_type is None else self._input.getText((localctx.var_type.start,localctx.var_type.stop)))
            if entity_type == '%':
                node_class = IntentNode
            elif entity_type == '~':
                node_class = AliasNode
            elif entity_type == '@':
                node_class = SlotNode

            name=(None if localctx.name is None else localctx.name.text)
            optional=localctx.var_optional is not None
            ref_names=[v.text for v in localctx.var_ref_names]

            node = node_class(name, ref_names, optional)


            for fltr in localctx.var_fltrs:
                name = fltr.__data__.get('name')
                optional = fltr.__data__.get('optional')
                args = fltr.__data__.get('args')
                kwargs = fltr.__data__.get('kwargs')
                node.add_filter(Filter(name, optional, args, kwargs))


            self._ctx.stop = self._input.LT(-1)


            node.start = self.get_start_pos(localctx)
            node.stop = self.get_stop_pos(localctx)
            self.node_stack.peek().add_child(node)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Entity_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.Entity_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ENTITY_TYPE(self):
            return self.getToken(BoltunParser.ENTITY_TYPE, 0)

        def getRuleIndex(self):
            return BoltunParser.RULE_entity_type

        def enterRule(self, listener):
            if hasattr(listener, "enterEntity_type"):
                listener.enterEntity_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEntity_type"):
                listener.exitEntity_type(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitEntity_type"):
                return visitor.visitEntity_type(self)
            else:
                return visitor.visitChildren(self)




    def entity_type(self):

        localctx = BoltunParser.Entity_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_entity_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(BoltunParser.ENTITY_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Call_tagContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.Call_tagContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.var_optional = None # Token
            self.name = None # Token
            self.var_attr = None # AttrContext
            self._fltr = None # FltrContext
            self.var_fltrs = list() # of FltrContexts

        def LL_BRACK(self):
            return self.getToken(BoltunParser.LL_BRACK, 0)

        def GREATER(self):
            return self.getToken(BoltunParser.GREATER, 0)

        def RR_BRACK(self):
            return self.getToken(BoltunParser.RR_BRACK, 0)

        def NAME(self):
            return self.getToken(BoltunParser.NAME, 0)

        def attr(self):
            return self.getTypedRuleContext(BoltunParser.AttrContext,0)


        def QUESTION(self, i=None):
            if i is None:
                return self.getTokens(BoltunParser.QUESTION)
            else:
                return self.getToken(BoltunParser.QUESTION, i)

        def fltr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BoltunParser.FltrContext)
            else:
                return self.getTypedRuleContext(BoltunParser.FltrContext,i)


        def getRuleIndex(self):
            return BoltunParser.RULE_call_tag

        def enterRule(self, listener):
            if hasattr(listener, "enterCall_tag"):
                listener.enterCall_tag(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCall_tag"):
                listener.exitCall_tag(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitCall_tag"):
                return visitor.visitCall_tag(self)
            else:
                return visitor.visitChildren(self)




    def call_tag(self):

        localctx = BoltunParser.Call_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_call_tag)



        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(BoltunParser.LL_BRACK)
            self.state = 108
            self.match(BoltunParser.GREATER)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BoltunParser.QUESTION:
                self.state = 109
                localctx.var_optional = self.match(BoltunParser.QUESTION)


            self.state = 112
            localctx.name = self.match(BoltunParser.NAME)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BoltunParser.QUESTION:
                self.state = 113
                localctx.var_optional = self.match(BoltunParser.QUESTION)


            self.state = 116
            localctx.var_attr = self.attr()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BoltunParser.QUESTION:
                self.state = 117
                localctx.var_optional = self.match(BoltunParser.QUESTION)


            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BoltunParser.PIPE:
                self.state = 120
                localctx._fltr = self.fltr()
                localctx.var_fltrs.append(localctx._fltr)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(BoltunParser.RR_BRACK)


            name=(None if localctx.name is None else localctx.name.text)
            optional=localctx.var_optional is not None
            args = localctx.var_attr.__data__.get('args', None)
            kwargs = localctx.var_attr.__data__.get('kwargs', None)

            node = CallNode(name, optional, args, kwargs)

            for fltr in localctx.var_fltrs:
                name = fltr.__data__.get('name')
                args = fltr.__data__.get('args')
                kwargs = fltr.__data__.get('kwargs')

                node.add_filter(Filter(name, args, kwargs))


            self._ctx.stop = self._input.LT(-1)


            node.start = self.get_start_pos(localctx)
            node.stop = self.get_stop_pos(localctx)
            self.node_stack.peek().add_child(node)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FltrContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.FltrContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.var_name = None # Token
            self.var_optional = None # Token
            self.var_attr = None # AttrContext

        def PIPE(self):
            return self.getToken(BoltunParser.PIPE, 0)

        def NAME(self):
            return self.getToken(BoltunParser.NAME, 0)

        def QUESTION(self, i=None):
            if i is None:
                return self.getTokens(BoltunParser.QUESTION)
            else:
                return self.getToken(BoltunParser.QUESTION, i)

        def attr(self):
            return self.getTypedRuleContext(BoltunParser.AttrContext,0)


        def getRuleIndex(self):
            return BoltunParser.RULE_fltr

        def enterRule(self, listener):
            if hasattr(listener, "enterFltr"):
                listener.enterFltr(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFltr"):
                listener.exitFltr(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitFltr"):
                return visitor.visitFltr(self)
            else:
                return visitor.visitChildren(self)




    def fltr(self):

        localctx = BoltunParser.FltrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_fltr)



        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(BoltunParser.PIPE)
            self.state = 130
            localctx.var_name = self.match(BoltunParser.NAME)
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 131
                localctx.var_optional = self.match(BoltunParser.QUESTION)


            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BoltunParser.L_PAREN:
                self.state = 134
                localctx.var_attr = self.attr()


            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BoltunParser.QUESTION:
                self.state = 137
                localctx.var_optional = self.match(BoltunParser.QUESTION)




            localctx.__data__ = {
                'name' : localctx.var_name.text,
                'optional': localctx.var_optional is not None,
                'args' : localctx.var_attr.__data__.get('args') if localctx.var_attr else [],
                'kwargs' : localctx.var_attr.__data__.get('kwargs') if localctx.var_attr else {}
            }


            self._ctx.stop = self._input.LT(-1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttrContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.AttrContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.__data__ = dict()
            self._attr_kw_arg_def = None # Attr_kw_arg_defContext
            self.var_attr_kw_arg_defs = list() # of Attr_kw_arg_defContexts
            self._attr_arg_def = None # Attr_arg_defContext
            self.var_attr_arg_defs = list() # of Attr_arg_defContexts

        def L_PAREN(self):
            return self.getToken(BoltunParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(BoltunParser.R_PAREN, 0)

        def attr_kw_arg_def(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BoltunParser.Attr_kw_arg_defContext)
            else:
                return self.getTypedRuleContext(BoltunParser.Attr_kw_arg_defContext,i)


        def attr_arg_def(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(BoltunParser.Attr_arg_defContext)
            else:
                return self.getTypedRuleContext(BoltunParser.Attr_arg_defContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(BoltunParser.COMMA)
            else:
                return self.getToken(BoltunParser.COMMA, i)

        def getRuleIndex(self):
            return BoltunParser.RULE_attr

        def enterRule(self, listener):
            if hasattr(listener, "enterAttr"):
                listener.enterAttr(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttr"):
                listener.exitAttr(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAttr"):
                return visitor.visitAttr(self)
            else:
                return visitor.visitChildren(self)




    def attr(self):

        localctx = BoltunParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attr)



        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(BoltunParser.L_PAREN)
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BoltunParser.NAME]:
                self.state = 143
                localctx._attr_kw_arg_def = self.attr_kw_arg_def()
                localctx.var_attr_kw_arg_defs.append(localctx._attr_kw_arg_def)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BoltunParser.COMMA:
                    self.state = 144
                    self.match(BoltunParser.COMMA)
                    self.state = 145
                    localctx._attr_kw_arg_def = self.attr_kw_arg_def()
                    localctx.var_attr_kw_arg_defs.append(localctx._attr_kw_arg_def)
                    self.state = 150
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [BoltunParser.BOOL, BoltunParser.NUMBER, BoltunParser.STRING]:
                self.state = 151
                localctx._attr_arg_def = self.attr_arg_def()
                localctx.var_attr_arg_defs.append(localctx._attr_arg_def)
                self.state = 156
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 152
                        self.match(BoltunParser.COMMA)
                        self.state = 153
                        localctx._attr_arg_def = self.attr_arg_def()
                        localctx.var_attr_arg_defs.append(localctx._attr_arg_def) 
                    self.state = 158
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BoltunParser.COMMA:
                    self.state = 159
                    self.match(BoltunParser.COMMA)
                    self.state = 160
                    localctx._attr_kw_arg_def = self.attr_kw_arg_def()
                    localctx.var_attr_kw_arg_defs.append(localctx._attr_kw_arg_def)
                    self.state = 165
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 168
            self.match(BoltunParser.R_PAREN)


            localctx.__data__ = {
                'args' : [
                    v.__data__.get('value') for v in localctx.var_attr_arg_defs
                ],
                'kwargs' : {
                    v.__data__.get('name'): v.__data__.get('value')
                    for v in localctx.var_attr_kw_arg_defs
                }
            }


            self._ctx.stop = self._input.LT(-1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attr_arg_defContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.Attr_arg_defContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.__data__ = dict()
            self.var_value = None # Attr_valueContext

        def attr_value(self):
            return self.getTypedRuleContext(BoltunParser.Attr_valueContext,0)


        def getRuleIndex(self):
            return BoltunParser.RULE_attr_arg_def

        def enterRule(self, listener):
            if hasattr(listener, "enterAttr_arg_def"):
                listener.enterAttr_arg_def(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttr_arg_def"):
                listener.exitAttr_arg_def(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAttr_arg_def"):
                return visitor.visitAttr_arg_def(self)
            else:
                return visitor.visitChildren(self)




    def attr_arg_def(self):

        localctx = BoltunParser.Attr_arg_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attr_arg_def)



        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            localctx.var_value = self.attr_value()


            localctx.__data__ = {
                'value': localctx.var_value.__data__.get('content')
            }


            self._ctx.stop = self._input.LT(-1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attr_kw_arg_defContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.Attr_kw_arg_defContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.__data__ = dict()
            self.var_name = None # Token
            self.var_value = None # Attr_valueContext

        def EQUAL(self):
            return self.getToken(BoltunParser.EQUAL, 0)

        def NAME(self):
            return self.getToken(BoltunParser.NAME, 0)

        def attr_value(self):
            return self.getTypedRuleContext(BoltunParser.Attr_valueContext,0)


        def getRuleIndex(self):
            return BoltunParser.RULE_attr_kw_arg_def

        def enterRule(self, listener):
            if hasattr(listener, "enterAttr_kw_arg_def"):
                listener.enterAttr_kw_arg_def(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttr_kw_arg_def"):
                listener.exitAttr_kw_arg_def(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAttr_kw_arg_def"):
                return visitor.visitAttr_kw_arg_def(self)
            else:
                return visitor.visitChildren(self)




    def attr_kw_arg_def(self):

        localctx = BoltunParser.Attr_kw_arg_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_attr_kw_arg_def)



        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            localctx.var_name = self.match(BoltunParser.NAME)
            self.state = 175
            self.match(BoltunParser.EQUAL)
            self.state = 176
            localctx.var_value = self.attr_value()


            localctx.__data__ = {
                'name': localctx.var_name.text,
                'value': localctx.var_value.__data__.get('content')
            }


            self._ctx.stop = self._input.LT(-1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attr_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.Attr_valueContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.__data__ = dict()
            self.var_content = None # Token

        def BOOL(self):
            return self.getToken(BoltunParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(BoltunParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(BoltunParser.STRING, 0)

        def getRuleIndex(self):
            return BoltunParser.RULE_attr_value

        def enterRule(self, listener):
            if hasattr(listener, "enterAttr_value"):
                listener.enterAttr_value(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAttr_value"):
                listener.exitAttr_value(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAttr_value"):
                return visitor.visitAttr_value(self)
            else:
                return visitor.visitChildren(self)




    def attr_value(self):

        localctx = BoltunParser.Attr_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_attr_value)



        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            localctx.var_content = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BoltunParser.BOOL) | (1 << BoltunParser.NUMBER) | (1 << BoltunParser.STRING))) != 0)):
                localctx.var_content = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()


            localctx.__data__ = {
                'content': ast.literal_eval(localctx.var_content.text)
            }


            self._ctx.stop = self._input.LT(-1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comment_tagContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(BoltunParser.Comment_tagContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.__data__ = dict()
            self._COMMENT_DATA = None # Token
            self.var_chars = list() # of Tokens

        def LL_COMMENT_BRACK(self):
            return self.getToken(BoltunParser.LL_COMMENT_BRACK, 0)

        def RR_COMMENT_BRACK(self):
            return self.getToken(BoltunParser.RR_COMMENT_BRACK, 0)

        def COMMENT_DATA(self, i=None):
            if i is None:
                return self.getTokens(BoltunParser.COMMENT_DATA)
            else:
                return self.getToken(BoltunParser.COMMENT_DATA, i)

        def getRuleIndex(self):
            return BoltunParser.RULE_comment_tag

        def enterRule(self, listener):
            if hasattr(listener, "enterComment_tag"):
                listener.enterComment_tag(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitComment_tag"):
                listener.exitComment_tag(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitComment_tag"):
                return visitor.visitComment_tag(self)
            else:
                return visitor.visitChildren(self)




    def comment_tag(self):

        localctx = BoltunParser.Comment_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comment_tag)



        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(BoltunParser.LL_COMMENT_BRACK)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 183
                    localctx._COMMENT_DATA = self.match(BoltunParser.COMMENT_DATA)
                    localctx.var_chars.append(localctx._COMMENT_DATA) 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 189
            self.match(BoltunParser.RR_COMMENT_BRACK)


            content = data_str = ''.join([c.text for c in localctx.var_chars])
            localctx.__data__ = {
                'content' : content
            }

            node = CommentNode(content)
            node.start = self.get_start_pos(localctx)
            node.stop = self.get_stop_pos(localctx)


            self._ctx.stop = self._input.LT(-1)


            node.start = self.get_start_pos(localctx)
            node.stop = self.get_stop_pos(localctx)
            self.node_stack.peek().add_child(node)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





