from __future__ import absolute_import

import attr

from .base import LeafNode


@attr.s
class DataNode(LeafNode):
    content = attr.ib(type=str)

    def __compile__(self, compiler):
        return compiler.text(self.content)


__all__ = ['DataNode']
