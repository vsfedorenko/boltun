from __future__ import absolute_import, division, print_function

from abc import ABCMeta

import attr
from six import with_metaclass

from boltun.engine.grammar.antlr4.node import Node


@attr.s
class LeafNode(with_metaclass(ABCMeta, Node)):

    def __compile__(self, compiler, environment):
        pass
