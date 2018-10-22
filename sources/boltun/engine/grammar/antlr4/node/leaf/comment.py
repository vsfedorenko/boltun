from __future__ import absolute_import

import attr

from .base import LeafNode


@attr.s
class CommentNode(LeafNode):
    content = attr.ib(type=str)

    def __compile__(self, compiler, environment):
        return compiler.nothing(environment)
