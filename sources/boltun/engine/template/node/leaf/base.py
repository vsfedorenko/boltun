from __future__ import absolute_import

from abc import ABCMeta

import attr
from six import with_metaclass

from ..__base__ import Node


@attr.s
class LeafNode(with_metaclass(ABCMeta, Node)):

    def __compile__(self, compiler):
        pass


__all__ = ['LeafNode']
