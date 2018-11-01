from __future__ import absolute_import, division, print_function

from abc import ABCMeta

import attr
from six import with_metaclass

from boltun.engine.grammar.antlr4.node import Node


@attr.s
class ForkNode(with_metaclass(ABCMeta, Node)):
    children = attr.ib(type=list, factory=list)

    def __compile__(self, compiler, environment):
        return [
            child.__compile__(compiler, environment)
            for child in
            self.children
        ]

    def add_child(self, node):
        self.children.append(node)

    def add_children(self, nodes):
        self.children.extend(nodes)
