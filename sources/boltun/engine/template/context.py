from __future__ import absolute_import, division, print_function

import attr
import six


@attr.s
class FunctionContext(object):
    name = attr.ib(type=six.string_types)
    arg_params = attr.ib(type=list, factory=list)
    kwarg_params = attr.ib(type=dict, factory=dict)


@attr.s
class FilterContext(object):
    name = attr.ib(type=six.string_types)
    value = attr.ib()
    arg_params = attr.ib(type=list, factory=list)
    kwarg_params = attr.ib(type=dict, factory=dict)
