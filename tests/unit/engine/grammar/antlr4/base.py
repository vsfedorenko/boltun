from __future__ import absolute_import, division, print_function

import unittest
from abc import ABCMeta

import six
from six import with_metaclass

from boltun.engine.grammar import Node
from boltun.engine.grammar.antlr4 import Antlr4Grammar
from boltun.engine.grammar.antlr4.node.fork import RootNode


class BaseAntlr4GrammarTestCase(with_metaclass(ABCMeta, unittest.TestCase)):

    def parse(self, input_str):
        # type: (str) -> RootNode
        grammar = Antlr4Grammar()
        parse_result = grammar.parse(input_str)
        assert parse_result is not None

        node_tree = parse_result.node_tree
        return node_tree

    def assert_grammar_tree(self, node_or_tree, expected):
        if not issubclass(type(node_or_tree), Node):
            assert node_or_tree == expected
            return

        node_type, params = expected

        assert node_or_tree is not None
        assert isinstance(node_or_tree, node_type)
        for k, expected_v in six.iteritems(params):
            param_v = getattr(node_or_tree, k)

            if isinstance(param_v, list):

                param_expected_values_tuples = zip(param_v, expected_v)
                assert len(param_expected_values_tuples) == len(param_v)
                assert len(param_expected_values_tuples) == len(expected_v)

                for p, e in param_expected_values_tuples:
                    self.assert_grammar_tree(p, e)
            else:
                self.assert_grammar_tree(param_v, expected_v)
