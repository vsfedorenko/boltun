from __future__ import absolute_import

from abc import ABCMeta, abstractmethod as abstract_method

import attr
from enum import IntEnum
from six import with_metaclass

from boltun.engine.template.node import Node


@attr.s
class GrammarParseResult(object):
    grammar_tree = attr.ib()
    node_tree = attr.ib(type=Node)


@attr.s
class GrammarMode(IntEnum):
    DATA = 1
    CALL = 2
    NLP = 3


@attr.s
class Grammar(with_metaclass(ABCMeta, object)):

    @abstract_method
    def parse(self, input_str, mode=GrammarMode.NLP):
        """
        :param str input_str: input str
        :param mode: GrammarMode: parser mode

        :rtype: GrammarParseResult
        """
        raise NotImplementedError()


__all__ = ['Grammar', 'GrammarMode', 'GrammarParseResult']
