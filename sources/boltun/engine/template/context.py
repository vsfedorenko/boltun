import attr
import six


@attr.s
class FunctionContext(object):
    name = attr.ib(type=six.string_types)
    method = attr.ib(type=six.string_types, default=None)
    arg_params = attr.ib(type=list, default=attr.Factory(list))
    kwarg_params = attr.ib(type=dict, default=attr.Factory(dict))


@attr.s
class FilterContext(object):
    name = attr.ib(type=six.string_types)
    value = attr.ib()
    method = attr.ib(type=six.string_types, default=None)
    arg_params = attr.ib(type=list, default=attr.Factory(list))
    kwarg_params = attr.ib(type=dict, default=attr.Factory(dict))
