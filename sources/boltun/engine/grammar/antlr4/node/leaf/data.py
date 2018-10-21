from __future__ import absolute_import

import attr
import six

from .base import LeafNode


@attr.s
class DataNode(LeafNode):
    content = attr.ib(type=six.string_types)

    def __compile__(self, compiler, environment):
        return compiler.text(environment, self.content)


__all__ = ['DataNode']
