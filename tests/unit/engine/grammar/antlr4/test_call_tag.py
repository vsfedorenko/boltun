from __future__ import absolute_import, division, print_function

import unittest

from parameterized import parameterized

from boltun.engine.grammar.antlr4.node import NodeFilter
from boltun.engine.grammar.antlr4.node.fork import ContentNode, \
    RootNode
from boltun.engine.grammar.antlr4.node.leaf import CallNode, DataNode
from ._base import BaseAntlr4GrammarTestCase


class TestCallTag(BaseAntlr4GrammarTestCase):

    @parameterized.expand([
        (
                "[% env('JAVA_HOME') %]",

                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (
                                CallNode,
                                {'name': "env", 'arg_params': ['JAVA_HOME']}
                        )
                    ]}),
                ]})
        ),
        (
                "[% env.get('JAVA_HOME') %]",

                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (
                                CallNode,
                                {
                                    'name': "env",
                                    'ref_names': ['get'],
                                    'arg_params': ['JAVA_HOME']
                                }
                        )
                    ]}),
                ]})
        ),
        (
                "[% namespace1.namespace2.get('ARG') %]",

                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (
                                CallNode,
                                {
                                    'name': "namespace1",
                                    'ref_names': ['namespace2', 'get'],
                                    'arg_params': ['ARG']
                                }
                        )
                    ]}),
                ]})
        ),
        (
                "[% env('PATH') %] [% print('Hello') %]",

                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (CallNode, {'name': "env", 'arg_params': ['PATH']}),
                        (DataNode, {'content': ' '}),
                        (CallNode, {'name': "print", 'arg_params': ['Hello']})
                    ]}),
                ]})
        ),
        (
                "[% env('JAVA_HOME', print=False) %]",

                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (
                                CallNode,
                                {
                                    'name': "env",
                                    'arg_params': ['JAVA_HOME'],
                                    'kwarg_params': {'print': False}
                                }
                        )
                    ]}),
                ]})
        ),
        (
                "[% env('JAVA_HOME') | filter('a') | filter2(kwarg='b') %]",

                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (CallNode, {
                            'name': "env",
                            'arg_params': ['JAVA_HOME'],
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
                "[% env('JAVA_HOME') | namespace1.namespace2.filter('a') %]",

                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (CallNode, {
                            'name': "env",
                            'arg_params': ['JAVA_HOME'],
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
        ),
        (
                "[% some_func('1', 2, 3., 0.4, True, [1, 2, '3']) %]",

                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (CallNode, {
                            'name': "some_func",
                            'arg_params': ['1', 2, 3.0, 0.4, True, [1, 2, '3']]
                        })
                    ]}),
                ]})

        ),
        (
                "[% some_func(0, [[1], 2, [3, 4, [5, 6]], 7], 8) %]",

                (RootNode, {'children': [
                    (ContentNode, {'children': [
                        (CallNode, {
                            'name': "some_func",
                            'arg_params': [0, [[1], 2, [3, 4, [5, 6]], 7], 8]
                        })
                    ]}),
                ]})

        )

    ])
    def test_call_tag(self, text, expected_tree):
        self.assert_grammar_tree(self.parse(text), expected_tree)


if __name__ == '__main__':
    unittest.main()
