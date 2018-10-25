import unittest

from parameterized import parameterized

from boltun.engine.grammar.antlr4.node.fork import ContentNode, RootNode
from boltun.engine.grammar.antlr4.node.leaf import DataNode
from .base import BaseAntlr4GrammarTestCase


class TestData(BaseAntlr4GrammarTestCase):

    @parameterized.expand([
        (
                "",
                (RootNode, {'children': []})
        ),
        (
                " ",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {'content': ' '})
                    ]}),
                ]})

        ),
        (
                "     ",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {'content': '     '})
                    ]}),
                ]})
        ),
        (
                "Hello",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {'content': 'Hello'})
                    ]}),
                ]})
        ),
        (
                "Hello, world!",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {'content': 'Hello, world!'})
                    ]}),
                ]})
        ),
        (
                "   Hello, world!  ",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {'content': '   Hello, world!  '})
                    ]}),
                ]})
        )

    ])
    def test_data_tag(self, text, expected_tree):
        self.assert_grammar_tree(self.parse(text), expected_tree)


if __name__ == '__main__':
    unittest.main()
