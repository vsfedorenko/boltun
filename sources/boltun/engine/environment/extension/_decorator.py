from inspect import isclass as is_class, isfunction as is_function, \
    ismethod as is_method

import attr


@attr.s
class BoltunContext(object):

    @classmethod
    def __decorator_attribute__(cls):
        return "__boltun_context__"

    name = attr.ib(type=str, default=None)
    visibility = attr.ib(type=str, default='global')
    function_name = attr.ib(type=str, default=None)
    filter_name = attr.ib(type=str, default=None)

    function = attr.ib(type=bool, default=True)
    filter = attr.ib(type=bool, default=False)
    filter_value_pos = attr.ib(type=int, default=0)
    filter_value_key = attr.ib(type=str, default=None)

    environment_pos = attr.ib(type=int, default=None)
    environment_key = attr.ib(type=str, default=None)


def boltun(maybe_target=None, context=None, **kwargs):
    if not context and not kwargs:
        context = BoltunContext(**kwargs)

    def _decorator(target):
        def _wrapper(*args, **kwargs):
            return target(*args, **kwargs)

        setattr(_wrapper, BoltunContext.__decorator_attribute__(), context)

        return _wrapper

    is_function_ = is_function(maybe_target)
    is_class_ = is_class(maybe_target)
    is_method_ = is_method(maybe_target)

    decorator = _decorator(maybe_target) if (
            is_function_ or is_class_ or is_method_) else _decorator

    return decorator
