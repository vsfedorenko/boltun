from __future__ import absolute_import, division, print_function

import unittest

from parameterized import parameterized

from boltun.engine.grammar.antlr4.node import NodeFilter
from boltun.engine.grammar.antlr4.node.fork import ContentNode, \
    RootNode
from boltun.engine.grammar.antlr4.node.leaf import DataNode
from ._base import BaseAntlr4GrammarTestCase


class TestDataTag(BaseAntlr4GrammarTestCase):

    @parameterized.expand([
        (
                "[[ ]]",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {'content': None})
                    ]}),
                ]})
        ),
        (
                "[[ ' ' ]]",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {'content': ' '})
                    ]}),
                ]})
        ),
        (
                "[[ 'Hello, World !' ]]",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {'content': "Hello, World !"})
                    ]}),
                ]})
        ),
        (
                "[[ 'Hello, World !' ]] [[ 'Welcome !' ]]",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {'content': "Hello, World !"}),
                        (DataNode, {'content': ' '}),
                        (DataNode, {'content': "Welcome !"})
                    ]}),
                ]})
        ),
        (
                "[[ 'Hello, friend !' | filter('a') | filter2(kwarg='b') ]]",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {
                            'content': "Hello, friend !",
                            'filters': [
                                NodeFilter('filter', arg_params=['a']),
                                NodeFilter(
                                    'filter2',
                                    kwarg_params={'kwarg': 'b'}
                                )
                            ]
                        })
                    ]}),
                ]})
        ),
        (
                "[[ 'Hello, friend !' | namespace1.namespace2.filter('a') ]]",
                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {
                            'content': "Hello, friend !",
                            'filters': [
                                NodeFilter(
                                    'namespace1',
                                    ref_names=['namespace2', 'filter'],
                                    arg_params=['a']
                                ),
                            ]
                        })
                    ]}),
                ]})
        )
    ])
    def test_data_tag(self, text, expected_tree):
        self.assert_grammar_tree(self.parse(text), expected_tree)


if __name__ == '__main__':
    unittest.main()
