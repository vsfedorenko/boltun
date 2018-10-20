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


@attr.s
class Entity(Node):
    type = attr.ib()
    name = attr.ib(type=six.string_types)
    ref_names = attr.ib(type=list, default=attr.Factory(list))


@attr.s
class Call(Node):
    function = attr.ib(type=callable)
    method = attr.ib(type=six.string_types, default=None)
    args = attr.ib(type=list, default=attr.Factory(list))
    kwargs = attr.ib(type=dict, default=attr.Factory(dict))
