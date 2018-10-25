from boltun.engine.grammar.antlr4.node.fork import ContentNode, RootNode
from boltun.engine.grammar.antlr4.node.leaf import DataNode
from tests.engine.grammar.antlr4.base import BaseAntlr4GrammarTestCase


class DataTestCase(BaseAntlr4GrammarTestCase):

    def test_data_empty(self):
        self.assert_grammar_tree(
            self.parse(""),
            (RootNode, {'children': []})
        )

    def test_data_whitespace(self):
        self.assert_grammar_tree(
            self.parse(" "),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (DataNode, {'content': ' '})
                ]}),
            ]})
        )

    def test_data_multiple_whitespaces(self):
        self.assert_grammar_tree(
            self.parse("     "),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (DataNode, {'content': '     '})
                ]}),
            ]})
        )

    def test_data_text(self):
        self.assert_grammar_tree(
            self.parse("Hello"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (DataNode, {'content': 'Hello'})
                ]}),
            ]})
        )

    def test_data_text_with_spaces(self):
        self.assert_grammar_tree(
            self.parse("Hello, world!"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (DataNode, {'content': 'Hello, world!'})
                ]}),
            ]})
        )

    def test_data_text_with_spaces_surrounded(self):
        self.assert_grammar_tree(
            self.parse("   Hello, world!  "),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (DataNode, {'content': '   Hello, world!  '})
                ]}),
            ]})
        )