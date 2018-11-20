from __future__ import absolute_import, division, print_function

from abc import ABCMeta, abstractmethod as abstract_method

import attr
from six import with_metaclass


@attr.s
class Filter(with_metaclass(ABCMeta, object)):
    environment = attr.ib()

    @abstract_method
    def __names__(self):
        raise NotImplementedError()

    @abstract_method
    def __apply__(self, input_, *args, **kwargs):
        raise NotImplementedError()


@attr.s
class FilterDef(object):
    names = attr.ib(type=list)
    callable = attr.ib(type=callable)
