from __future__ import absolute_import, division, print_function

from boltun.engine.grammar.antlr4.node import NodeFilter
from boltun.engine.grammar.antlr4.node.fork import ContentNode, \
    RootNode
from boltun.engine.grammar.antlr4.node.leaf import CallNode, DataNode
from .base import BaseAntlr4GrammarTestCase


class CallTagTestCase(BaseAntlr4GrammarTestCase):

    def test_call_single_tag(self):
        self.assert_grammar_tree(
            self.parse("[% env('JAVA_HOME') %]"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (CallNode, {'name': "env", 'arg_params': ['JAVA_HOME']})
                ]}),
            ]})
        )

    def test_call_multiple_tag(self):
        self.assert_grammar_tree(
            self.parse("[% env('PATH') %] [% print('Hello') %]"),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (CallNode, {'name': "env", 'arg_params': ['PATH']}),
                    (DataNode, {'content': ' '}),
                    (CallNode, {'name': "print", 'arg_params': ['Hello']})
                ]}),
            ]})
        )

    def test_call_single_tag_with_kwargs(self):
        self.assert_grammar_tree(
            self.parse("[% env('JAVA_HOME', print=False) %]"),
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
        )

    def test_call_single_tag_with_filters(self):
        self.assert_grammar_tree(
            self.parse(
                "[% env('JAVA_HOME') | filter('a') | filter2(kwarg='b') %]"
            ),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (CallNode, {
                        'name': "env",
                        'arg_params': ['JAVA_HOME'],
                        'filters': [
                            NodeFilter('filter', arg_params=['a']),
                            NodeFilter('filter2', kwarg_params={'kwarg': 'b'})
                        ]
                    })
                ]}),
            ]})
        )

    def test_call_different_types_of_args(self):
        self.assert_grammar_tree(
            self.parse(
                "[% some_func('1', 2, 3., 0.4, True, [1, 2, '3']) %]"
            ),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (CallNode, {
                        'name': "some_func",
                        'arg_params': ['1', 2, 3.0, 0.4, True, [1, 2, '3']]
                    })
                ]}),
            ]})
        )

    def test_call_inner_lists(self):
        self.assert_grammar_tree(
            self.parse(
                "[% some_func(0, [[1], 2, [3, 4, [5, 6]], 7], 8) %]"
            ),
            (RootNode, {'children': [
                (ContentNode, {'children': [
                    (CallNode, {
                        'name': "some_func",
                        'arg_params': [0, [[1], 2, [3, 4, [5, 6]], 7], 8]
                    })
                ]}),
            ]})
        )
