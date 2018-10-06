import json
import logging.config
import unittest

import yaml
from antlr4 import *
from antlr4.tree.Trees import Trees

from boltun.parser.grammar import BoltunLexer, BoltunParser, \
    BoltunVisitor

logging.config.dictConfig(yaml.load(open('logging.dev.yaml', 'r')))
logger = logging.getLogger(__name__)


class MyTestCase(unittest.TestCase):

    def setUp(self):
        super(MyTestCase, self).setUp()

    def test_something(self):
        # input_str = "first"
        # input_str = "{{ first || second }}"
        # input_str = "{{ first || second || third }}"
        # input_str = "{{ first || [[% intent ]] [[# comment ]] || third }}"
        input_str = \
            "hello [[%? some_intent # another # ref1 | join(1, 15, 1., 'Hello', left=True) | append ]], " \
            "and call env func here [[> env('JAVA_HOME') | lower ]]" \
            "then call eval func here [[>? eval?('1 + 2')? | lower ]] " \
            "and comment here [[# comment hello commentworld!! My name is comment ]] " \
            "and here [[# comment2 ___#@!@#!#$324~ ]] " \
            "{{ then select [[> env('THIS_VAR') ]] || or select [[> env('THAT_VAR') ]] }} " \
            "my dear, [[~ some_alias | validate(all=True) ]] " \
            "[[@ slot_here ]] {{{!,?}}}"

        lexer = self.get_lexer(input_str)
        stream = self.get_stream(lexer)
        parser = self.get_parser(stream)

        self.assertIsNotNone(parser)
        tree = self.get_tree(parser)
        self.assertIsNotNone(tree)

        visitor = BoltunVisitor()
        visitor.visit(tree)

        print(Trees.toStringTree(tree, None, parser))

        root_node = parser.node_stack.peek()
        print(root_node)
        json_dump = json.dumps(
            root_node,
            default=lambda obj: obj.__dict__,
            sort_keys=True,
            indent=2
        )
        print(json_dump)

    def get_tree(self, parser):
        parser_result = parser.document()
        return parser_result

    def get_parser(self, stream):
        parser = BoltunParser(stream)
        return parser

    def get_lexer(self, input):
        return BoltunLexer(InputStream(input))

    def get_stream(self, lexer):
        return CommonTokenStream(lexer)


if __name__ == '__main__':
    unittest.main()
