from __future__ import absolute_import

import attr
import six


@attr.s
class Const(object):
    value = attr.ib()


@attr.s
class Entity(object):
    type = attr.ib()
    name = attr.ib(type=six.string_types)
    ref_names = attr.ib(type=list, default=attr.Factory(list))


@attr.s
class Call(object):
    function = attr.ib(type=callable)
    method = attr.ib(type=six.string_types, default=None)
    args = attr.ib(type=list, default=attr.Factory(list))
    kwargs = attr.ib(type=dict, default=attr.Factory(dict))
