from __future__ import absolute_import, division, print_function

import attr

from ._base import ForkNode
from .content import ContentNode


@attr.s
class ChoiceNode(ForkNode):

    def add_child(self, node):
        if isinstance(node, ContentNode):
            node = node.strip()

        super(ChoiceNode, self).add_child(node)

    def __compile__(self, compiler, environment):
        return compiler.any(
            *super(ChoiceNode, self).__compile__(compiler, environment))
