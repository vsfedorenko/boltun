import json
import logging.config
import unittest

import yaml

from boltun.engine.grammar.antlr4 import Antlr4Grammar

logging.config.dictConfig(yaml.load(open('logging.dev.yaml', 'r')))
logger = logging.getLogger(__name__)


class MyTestCase(unittest.TestCase):

    def setUp(self):
        super(MyTestCase, self).setUp()

    def test_something(self):
        # input_str = "hello [asfsfsdf"
        # input_str = "first"
        # input_str = "{{ first || second }}"
        # input_str = "{{ first || second || third }}"
        # input_str = "{{ first || [[% intent ]] [[# comment ]] || third }}"
        input_str = \
            "hello [[%? some_intent # another # ref1 | join(1, 15, 1., 'Hello', left=True) | append ]], " \
            "and call env func here [[> env('JAVA_HOME') | lower ]]" \
            "then call eval func here [[>? eval?('1 + 2')? | lower? | apper ]] " \
            "and comment here [[# comment hello commentworld!! My name is comment ]] " \
            "and here [[# comment2 ___#@!@#!#$324~ ]] " \
            "{{ then select [[>? env('THIS_VAR') ]] || or select [[>? env('THAT_VAR') ]] }} " \
            "my dear, [[~ some_alias | validate(all=True) ]] " \
            "[[@ slot_here ]] {{{!,?}}}"

        grammar = Antlr4Grammar()
        process_result = grammar.parse(input_str)

        node_tree = process_result.node_tree

        print(process_result)
        json_dump = json.dumps(
            node_tree,
            default=lambda obj: obj.__dict__,
            sort_keys=True,
            indent=2
        )
        print(json_dump)


if __name__ == '__main__':
    unittest.main()
