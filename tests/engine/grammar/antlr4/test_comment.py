from boltun.engine.grammar.antlr4.node.fork import ContentNode, RootNode
from boltun.engine.grammar.antlr4.node.leaf import CommentNode
from tests.engine.grammar.antlr4.base import BaseAntlr4GrammarTestCase


class DataTestCase(BaseAntlr4GrammarTestCase):

    def test_comment_empty(self):
        self.assert_grammar_tree(
            self.parse("[##]"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (CommentNode, {'content': None})
                ]})
            ]})
        )

    def test_comment_whitespace(self):
        self.assert_grammar_tree(
            self.parse("[# #]"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (CommentNode, {'content': None})
                ]})
            ]})
        )

    def test_comment_multiple_whitespaces(self):
        self.assert_grammar_tree(
            self.parse("[#     #]"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (CommentNode, {'content': None})
                ]})
            ]})
        )

    def test_comment_text(self):
        self.assert_grammar_tree(
            self.parse("[# Hello #]"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (CommentNode, {'content': 'Hello'})
                ]})
            ]})
        )

    def test_comment_text_with_whitespace_surrounded(self):
        self.assert_grammar_tree(
            self.parse("[#    Hello, World !      #]"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (CommentNode, {'content': 'Hello, World !'})
                ]})
            ]})
        )

    def test_comment_text_with_special_symbols(self):
        text = '#@##$@#$###%^**&(()1'
        self.assert_grammar_tree(
            self.parse("[# " + text + " #]"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (CommentNode, {'content': text})
                ]})
            ]})
        )
