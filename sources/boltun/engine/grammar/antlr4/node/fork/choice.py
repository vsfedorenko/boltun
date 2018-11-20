from __future__ import absolute_import, division, print_function

import attr

from ._base import ForkNode


@attr.s
class ChoiceNode(ForkNode):

    def add_child(self, node, keep_ws=False):
        if isinstance(node, ChoiceNode.Wrapper):
            self.add_children(node.children, node.keep_ws)
        else:
            if not keep_ws:
                node = node.strip()
            super(ChoiceNode, self).add_child(node)

    def add_children(self, nodes, keep_ws=False):
        for node in nodes:
            self.add_child(node, keep_ws)

    def __compile__(self, compiler, environment):
        return compiler.any(
            *super(ChoiceNode, self).__compile__(compiler, environment))

    @attr.s
    class Wrapper(ForkNode):
        keep_ws = attr.ib(type=bool, factory=bool, init=False)
