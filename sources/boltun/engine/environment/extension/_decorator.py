import attr


@attr.s
class BoltunContext(object):
    name = attr.ib(type=str, default=None)
    function_name = attr.ib(type=str, default=None)
    filter_name = attr.ib(type=str, default=None)

    function = attr.ib(type=bool, default=False)
    filter = attr.ib(type=bool, default=False)
    filter_value_pos = attr.ib(type=int, default=0)
    filter_value_key = attr.ib(type=str, default=None)

    environment_pos = attr.ib(type=int, default=None)
    environment_key = attr.ib(type=str, default=None)


def boltun(maybe_target=None, context=None):
    def _decorator(func):
        def _wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return _wrapper

    return _decorator(maybe_target) \
        if callable(maybe_target) else _decorator
