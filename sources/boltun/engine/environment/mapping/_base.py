from abc import ABCMeta, abstractmethod as abstract_method

import attr
from enum import IntEnum
from six import with_metaclass


class MappingType(IntEnum):
    FUNCTION = 1
    FILTER = 2


@attr.s
class Mapping(object):
    type = attr.ib(type=MappingType)
    name = attr.ib(type=str)
    callable = attr.ib()


@attr.s
class MappingResolver(with_metaclass(ABCMeta)):

    @abstract_method
    def __accepts__(self, item):
        raise NotImplementedError()

    @abstract_method
    def __apply__(self, item):
        raise NotImplementedError()
