from __future__ import absolute_import

import attr

from .base import ForkNode


@attr.s
class ContentNode(ForkNode):
    pass


__all__ = ['ContentNode']
