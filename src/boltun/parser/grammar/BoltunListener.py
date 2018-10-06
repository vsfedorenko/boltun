# Generated from /Users/vfedorenko/Developer/Business/Projects/NeuralNetworks/nlu_data_generator/src/boltun/parser/grammar/Boltun.g4 by ANTLR 4.7
from antlr4 import *

import ast
import logging

from antlr4 import *

from .node import AliasNode, CallNode, ChoiceNode, CommentNode, ContentNode, \
    DataNode, Filter, IntentNode, RootNode, SlotNode
from ...util.collections import Stack

logger = logging.getLogger(__name__)


# This class defines a complete listener for a parse tree produced by BoltunParser.
class BoltunListener(ParseTreeListener):

    # Enter a parse tree produced by BoltunParser#document.
    def enterDocument(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#document.
    def exitDocument(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#content.
    def enterContent(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#content.
    def exitContent(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#data.
    def enterData(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#data.
    def exitData(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#polyadic_tag.
    def enterPolyadic_tag(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#polyadic_tag.
    def exitPolyadic_tag(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#unary_tag.
    def enterUnary_tag(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#unary_tag.
    def exitUnary_tag(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#choice_tag.
    def enterChoice_tag(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#choice_tag.
    def exitChoice_tag(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#choice_short_tag.
    def enterChoice_short_tag(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#choice_short_tag.
    def exitChoice_short_tag(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#entity_tag.
    def enterEntity_tag(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#entity_tag.
    def exitEntity_tag(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#entity_type.
    def enterEntity_type(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#entity_type.
    def exitEntity_type(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#call_tag.
    def enterCall_tag(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#call_tag.
    def exitCall_tag(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#fltr.
    def enterFltr(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#fltr.
    def exitFltr(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#attr.
    def enterAttr(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#attr.
    def exitAttr(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#attr_arg_def.
    def enterAttr_arg_def(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#attr_arg_def.
    def exitAttr_arg_def(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#attr_kw_arg_def.
    def enterAttr_kw_arg_def(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#attr_kw_arg_def.
    def exitAttr_kw_arg_def(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#attr_value.
    def enterAttr_value(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#attr_value.
    def exitAttr_value(self, ctx):
        pass


    # Enter a parse tree produced by BoltunParser#comment_tag.
    def enterComment_tag(self, ctx):
        pass

    # Exit a parse tree produced by BoltunParser#comment_tag.
    def exitComment_tag(self, ctx):
        pass


