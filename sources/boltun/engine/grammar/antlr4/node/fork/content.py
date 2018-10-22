from __future__ import absolute_import

import attr

from boltun.engine.grammar.antlr4.node.leaf import DataNode
from .base import ForkNode


@attr.s
class ContentNode(ForkNode):

    def __compile__(self, compiler, environment):
        compiled_content = \
            super(ContentNode, self).__compile__(compiler, environment)

        return compiled_content

    def strip(self):
        if len(self.children) == 1:
            child = self.children[0]
            if isinstance(child, DataNode):
                node = ContentNode()
                node.add_child(child.strip())
                return node
        else:
            return self.lstrip().rstrip()

    def lstrip(self):
        node = ContentNode()

        index = 0
        while True:
            if index == len(self.children):
                break

            child_node = self.children[index]
            if isinstance(child_node, DataNode):
                if not child_node.is_space():
                    break
            else:
                break

            index += 1

        children = self.children
        if index > 0:
            children = children[index:]

        if children:
            node.add_children(children)

        return node

    def rstrip(self):
        node = ContentNode()

        index = 0
        while True:
            if index == len(self.children):
                break

            child_node = self.children[len(self.children) - index - 1]
            if isinstance(child_node, DataNode):
                if not child_node.is_space():
                    break
            else:
                break

            index += 1

        children = self.children
        if index > 0:
            children = children[:index]

        if children:
            node.add_children(children)

        return node
