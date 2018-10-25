from __future__ import absolute_import, division, print_function

from abc import ABCMeta, abstractmethod as abstract_method

import attr
from six import with_metaclass


def boltun_function(names=None):
    def callable_instance(func):
        func.__boltun_function__ = True
        func.__boltun_names__ = names if names else None

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return callable_instance


@attr.s
class Function(with_metaclass(ABCMeta, object)):
    _environment = attr.ib()

    @classmethod
    @abstract_method
    def __names__(cls):
        raise NotImplementedError()

    @abstract_method
    def __execute__(self, *args, **kwargs):
        raise NotImplementedError()
