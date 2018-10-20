from __future__ import absolute_import

from abc import ABCMeta

import attr
from six import with_metaclass

from boltun.engine.grammar.antlr4.node import Node


@attr.s
class ForkNode(with_metaclass(ABCMeta, Node)):
    children = attr.ib(type=list, default=attr.Factory(list))

    def add_child(self, node):
        self.children.append(node)

    def __compile__(self, compiler):
        return [compiler.process(child) for child in self.children]


__all__ = ['ForkNode']
