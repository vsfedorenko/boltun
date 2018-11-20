from __future__ import absolute_import, division, print_function

import unittest

from parameterized import parameterized

from boltun.engine.grammar.antlr4.node.fork import ChoiceNode, ContentNode, \
    RootNode
from boltun.engine.grammar.antlr4.node.leaf import DataNode
from ._base import BaseAntlr4GrammarTestCase


class TestChoiceTag(BaseAntlr4GrammarTestCase):

    @parameterized.expand([
        (
                "{{ Hello || Hi }}",
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
        ),
        (
                "{{ Hello ||{  Hi   }}}",
                (RootNode, {'children': [
                    (ChoiceNode, {'children': [
                        (ContentNode, {'children': [
                            (DataNode, {'content': "Hello"})
                        ]}),
                        (ContentNode, {'children': [
                            (DataNode, {'content': "  Hi   "})
                        ]}),
                    ]})
                ]})
        ),
        (
                "{{{ Hello }||{  Hi   }}}",
                (RootNode, {'children': [
                    (ChoiceNode, {'children': [
                        (ContentNode, {'children': [
                            (DataNode, {'content': " Hello "})
                        ]}),
                        (ContentNode, {'children': [
                            (DataNode, {'content': "  Hi   "})
                        ]}),
                    ]})
                ]})
        ),
        (
                "{{{ Hello }||{ Aloha  }||  Hi   }}",
                (RootNode, {'children': [
                    (ChoiceNode, {'children': [
                        (ContentNode, {'children': [
                            (DataNode, {'content': " Hello "})
                        ]}),
                        (ContentNode, {'children': [
                            (DataNode, {'content': " Aloha  "})
                        ]}),
                        (ContentNode, {'children': [
                            (DataNode, {'content': "Hi"})
                        ]}),
                    ]})
                ]})
        ),
        (
                "{{ Hello ||{ Aloha  }||  Hi   }}",
                (RootNode, {'children': [
                    (ChoiceNode, {'children': [
                        (ContentNode, {'children': [
                            (DataNode, {'content': "Hello"})
                        ]}),
                        (ContentNode, {'children': [
                            (DataNode, {'content': " Aloha  "})
                        ]}),
                        (ContentNode, {'children': [
                            (DataNode, {'content': "Hi"})
                        ]}),
                    ]})
                ]})
        ),
        (
                "{{{ Hello }||{ Aloha  }||{  Hi   }}}",
                (RootNode, {'children': [
                    (ChoiceNode, {'children': [
                        (ContentNode, {'children': [
                            (DataNode, {'content': " Hello "})
                        ]}),
                        (ContentNode, {'children': [
                            (DataNode, {'content': " Aloha  "})
                        ]}),
                        (ContentNode, {'children': [
                            (DataNode, {'content': "  Hi   "})
                        ]}),
                    ]})
                ]})
        ),
        (
                "{{ Hello || {{ Hi || Aloha }} }}",
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

        ),
        (
                "{{ {{ Hi || Salaam }} "
                "|| Bonjour "
                "|| {{ {{ Hola || Hallo }} || Aloha }} "
                "}}",
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
        ),
    ])
    def test_choice_tag(self, text, expected_tree):
        self.assert_grammar_tree(self.parse(text), expected_tree)


if __name__ == '__main__':
    unittest.main()
