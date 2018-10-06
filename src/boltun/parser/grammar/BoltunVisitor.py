# Generated from /Users/vfedorenko/Developer/Business/Projects/NeuralNetworks/nlu_data_generator/src/boltun/parser/grammar/Boltun.g4 by ANTLR 4.7
from antlr4 import *

import ast
import logging

from antlr4 import *

from .node import AliasNode, CallNode, ChoiceNode, CommentNode, ContentNode, \
    DataNode, Filter, IntentNode, RootNode, SlotNode
from ...util.collections import Stack

logger = logging.getLogger(__name__)


# This class defines a complete generic visitor for a parse tree produced by BoltunParser.

class BoltunVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BoltunParser#document.
    def visitDocument(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#content.
    def visitContent(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#data.
    def visitData(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#polyadic_tag.
    def visitPolyadic_tag(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#unary_tag.
    def visitUnary_tag(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#choice_tag.
    def visitChoice_tag(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#entity_tag.
    def visitEntity_tag(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#entity_type.
    def visitEntity_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#call_tag.
    def visitCall_tag(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#fltr.
    def visitFltr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#attr.
    def visitAttr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#attr_arg_def.
    def visitAttr_arg_def(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#attr_kw_arg_def.
    def visitAttr_kw_arg_def(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#attr_value.
    def visitAttr_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BoltunParser#comment_tag.
    def visitComment_tag(self, ctx):
        return self.visitChildren(ctx)


