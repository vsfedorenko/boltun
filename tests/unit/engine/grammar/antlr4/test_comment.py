import unittest

from parameterized import parameterized

from boltun.engine.grammar.antlr4.node.fork import ContentNode, RootNode
from boltun.engine.grammar.antlr4.node.leaf import CommentNode
from .base import BaseAntlr4GrammarTestCase


class TestDataTag(BaseAntlr4GrammarTestCase):

    @parameterized.expand([
        (
                "[##]",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (CommentNode, {'content': None})
                    ]})
                ]})
        ),
        (
                "[# #]",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (CommentNode, {'content': None})
                    ]})
                ]})

        ),
        (
                "[#     #]",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (CommentNode, {'content': None})
                    ]})
                ]})
        ),
        (
                "[# Hello #]",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (CommentNode, {'content': 'Hello'})
                    ]})
                ]})
        ),
        (
                "[#    Hello, World !      #]",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (CommentNode, {'content': 'Hello, World !'})
                    ]})
                ]})
        ),
        (
                '[# @##$@#$###%^**&(()1 #]',
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (CommentNode, {'content': '@##$@#$###%^**&(()1'})
                    ]})
                ]})
        )
    ])
    def test_comment_tag(self, text, expected_tree):
        self.assert_grammar_tree(self.parse(text), expected_tree)


if __name__ == '__main__':
    unittest.main()
