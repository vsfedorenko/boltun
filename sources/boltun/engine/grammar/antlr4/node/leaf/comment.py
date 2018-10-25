from __future__ import absolute_import, division, print_function

import attr

from .base import LeafNode


@attr.s
class CommentNode(LeafNode):
    content = attr.ib(type=str)

    def __attrs_post_init__(self):
        if not self.content:
            return

        self.content = self.content.strip()

        if len(self.content) == 0:
            self.content = None

    def __compile__(self, compiler, environment):
        return compiler.nothing(environment)
