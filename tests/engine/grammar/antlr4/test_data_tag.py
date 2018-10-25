from __future__ import absolute_import, division, print_function

from boltun.engine.grammar.antlr4.node import NodeFilter
from boltun.engine.grammar.antlr4.node.fork import ContentNode, \
    RootNode
from boltun.engine.grammar.antlr4.node.leaf import DataNode
from .base import BaseAntlr4GrammarTestCase


class DataTagTestCase(BaseAntlr4GrammarTestCase):

    def test_data_single_empty_tag(self):
        self.assert_grammar_tree(
            self.parse("[[ ]]"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (DataNode, {'content': None})
                ]}),
            ]})
        )

    def test_data_single_whitespace_tag(self):
        self.assert_grammar_tree(
            self.parse("[[ ' ' ]]"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (DataNode, {'content': ' '})
                ]}),
            ]})
        )

    def test_data_single_text_tag(self):
        self.assert_grammar_tree(
            self.parse("[[ 'Hello, World !' ]]"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (DataNode, {'content': "Hello, World !"})
                ]}),
            ]})
        )

    def test_data_multiple_tag(self):
        self.assert_grammar_tree(
            self.parse("[[ 'Hello, World !' ]] [[ 'Welcome !' ]]"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (DataNode, {'content': "Hello, World !"}),
                    (DataNode, {'content': ' '}),
                    (DataNode, {'content': "Welcome !"})
                ]}),
            ]})
        )

    def test_data_single_tag_with_filters(self):
        self.assert_grammar_tree(
            self.parse(
                "[[ 'Hello, friend !' | filter('a') | filter2(kwarg='b') ]]"
            ),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (DataNode, {
                        'content': "Hello, friend !",
                        'filters': [
                            NodeFilter('filter', arg_params=['a']),
                            NodeFilter('filter2', kwarg_params={'kwarg': 'b'})
                        ]
                    })
                ]}),
            ]})
        )
