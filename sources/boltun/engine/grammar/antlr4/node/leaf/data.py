from __future__ import absolute_import

import attr
import six

from boltun.engine.grammar.nodes import FilteredNode, NodeFilter
from .base import LeafNode


@attr.s
class DataNode(LeafNode, FilteredNode):
    content = attr.ib(type=six.string_types)
    optional = attr.ib(type=bool, default=False)

    def __compile__(self, compiler, environment):
        text = compiler.text(environment, self.content)

        filtered_text = \
            NodeFilter.compile_sequence(
                compiler, environment, self.filters, text)

        return filtered_text

    def is_space(self):
        return self.content.isspace()

    def strip(self):
        return self.lstrip().rstrip()

    def lstrip(self):
        content = self.content.lstrip()

        node = DataNode(content, self.optional)
        node.filters = self.filters

        return node

    def rstrip(self):
        content = self.content.rstrip()

        node = DataNode(content, self.optional)
        node.filters = self.filters

        return node
