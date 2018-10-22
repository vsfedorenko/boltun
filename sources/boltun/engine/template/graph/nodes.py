from __future__ import absolute_import

from abc import ABCMeta

import attr
import six
from six import with_metaclass


@attr.s
class Node(with_metaclass(ABCMeta, object)):
    pass


@attr.s
class Const(Node):
    value = attr.ib()

    def __call__(self, *args, **kwargs):
        return self.value


@attr.s
class Call(Node):
    callable = attr.ib(type=callable)

    def __call__(self, *args, **kwargs):
        return self.callable(*args, **kwargs)


@attr.s
class Entity(Node):
    type = attr.ib()
    name = attr.ib(type=six.string_types)
    ref_names = attr.ib(type=list, default=attr.Factory(list))
