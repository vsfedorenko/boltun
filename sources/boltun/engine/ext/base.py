from __future__ import absolute_import

from abc import ABCMeta, abstractmethod as abstract_method

import attr
from six import with_metaclass


@attr.s
class Filter(with_metaclass(ABCMeta, object)):

    @abstract_method
    def __apply__(self, input_, *args, **kwargs):
        raise NotImplementedError()


@attr.s
class Function(with_metaclass(ABCMeta, object)):

    @abstract_method
    def __execute__(self, *args, **kwargs):
        raise NotImplementedError()


__all__ = ['Filter', 'Function']
