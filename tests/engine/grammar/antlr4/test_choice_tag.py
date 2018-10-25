from __future__ import absolute_import, division, print_function

import unittest

from boltun.engine.grammar.antlr4.node.fork import ChoiceNode, ContentNode, \
    RootNode
from boltun.engine.grammar.antlr4.node.leaf import DataNode
from .base import BaseAntlr4GrammarTestCase


class ChoiceTagTestCase(BaseAntlr4GrammarTestCase):

    def test_choice_single_tag(self):
        self.assert_grammar_tree(
            self.parse("{{ Hello || Hi }}"),
            (RootNode, {'children': [
                (ChoiceNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {'content': "Hello"})
                    ]}),
                    (ContentNode, {'children': [
                        (DataNode, {'content': "Hi"})
                    ]}),
                ]})
            ]})
        )

    def test_choice_inner_tag(self):
        self.assert_grammar_tree(
            self.parse("{{ Hello || {{ Hi || Aloha }} }}"),
            (RootNode, {'children': [
                (ChoiceNode, {'children': [
                    (ContentNode, {'children': [
                        (DataNode, {'content': "Hello"})
                    ]}),
                    (ContentNode, {'children': [
                        (ChoiceNode, {'children': [
                            (ContentNode, {'children': [
                                (DataNode, {'content': "Hi"})
                            ]}),
                            (ContentNode, {'children': [
                                (DataNode, {'content': "Aloha"})
                            ]}),
                        ]})
                    ]}),
                ]})
            ]})
        )

    def test_choice_multiple_inner_tag(self):
        self.assert_grammar_tree(
            self.parse(
                "{{ "
                "{{ Hi || Salaam }} "
                "|| Bonjour "
                "|| {{ {{ Hola || Hallo }} || Aloha }} "
                "}}"
            ),
            (RootNode, {'children': [
                (ChoiceNode, {'children': [
                    (ContentNode, {'children': [
                        (ChoiceNode, {'children': [
                            (ContentNode, {'children': [
                                (DataNode, {'content': "Hi"})
                            ]}),
                            (ContentNode, {'children': [
                                (DataNode, {'content': "Salaam"})
                            ]}),
                        ]})
                    ]}),
                    (ContentNode, {'children': [
                        (DataNode, {'content': "Bonjour"})
                    ]}),
                    (ContentNode, {'children': [
                        (ChoiceNode, {'children': [
                            (ContentNode, {'children': [
                                (ChoiceNode, {'children': [
                                    (ContentNode, {'children': [
                                        (DataNode, {'content': "Hola"})
                                    ]}),
                                    (ContentNode, {'children': [
                                        (DataNode, {'content': "Hallo"})
                                    ]}),
                                ]})
                            ]}),
                            (ContentNode, {'children': [
                                (DataNode, {'content': "Aloha"})
                            ]}),
                        ]})
                    ]}),
                ]})
            ]})
        )


if __name__ == '__main__':
    unittest.main()
