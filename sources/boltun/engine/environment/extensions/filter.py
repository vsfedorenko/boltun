from __future__ import absolute_import

from abc import ABCMeta, abstractmethod as abstract_method

import attr
from six import with_metaclass


def boltun_filter(cls_or_func):
    def _decorator(names):
        cls_or_func.__boltun_names__ = names

    return _decorator


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
