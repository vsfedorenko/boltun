from __future__ import absolute_import, division, print_function

from abc import ABCMeta, abstractmethod as abstract_method

import attr
import six
from six import with_metaclass


@attr.s
class Iterator(object):
    _iter = attr.ib(init=False)

    def next(self):
        return self.__next__()

    def __next__(self):
        return six.advance_iterator(self._iter)


@attr.s
class ResettableIterator(with_metaclass(ABCMeta, Iterator)):

    @abstract_method
    def __reset__(self):
        raise NotImplementedError()


@attr.s
class AutoResettableIterator(with_metaclass(ABCMeta, ResettableIterator)):

    @abstract_method
    def __reset__(self):
        raise NotImplementedError()

    def __next__(self):
        try:
            return super(AutoResettableIterator, self).__next__()
        except StopIteration:
            self.__reset__()
            return self.__next__()


@attr.s
class CollectionResettableIterator(ResettableIterator):
    _collection = attr.ib(init=True)

    def __attrs_post_init__(self):
        self.__reset__()

    def __create__(self):
        return iter(self._collection)

    def __reset__(self):
        self._iter = self.__create__()


@attr.s
class CollectionAutoResettableIterator(CollectionResettableIterator,
                                       AutoResettableIterator):
    pass
