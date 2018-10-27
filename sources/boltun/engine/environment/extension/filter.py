from __future__ import absolute_import, division, print_function

from abc import ABCMeta, abstractmethod as abstract_method

import attr
from six import with_metaclass


def boltun_filter(func_or_method=None, names=None):
    def callable_instance(func):
        func.__boltun_filter__ = True
        func.__boltun_names__ = names if names else None

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return callable_instance(func_or_method) \
        if callable(func_or_method) else callable_instance


@attr.s
class Filter(with_metaclass(ABCMeta, object)):
    _environment = attr.ib()

    @classmethod
    @abstract_method
    def __names__(cls):
        raise NotImplementedError()

    @abstract_method
    def __apply__(self, input_, *args, **kwargs):
        raise NotImplementedError()
