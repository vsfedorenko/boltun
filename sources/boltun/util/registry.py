from __future__ import absolute_import

from collections import OrderedDict

import attr
import six


@attr.s
class Registry(object):
    __items = attr.ib(default=attr.Factory(OrderedDict), init=False)

    def keys(self):
        return self.__items.keys()

    def values(self):
        return self.__items.values()

    def items(self):
        return six.iteritems(self.__items)

    def get(self, key):
        return self.__items.get(key)

    def get_or_default(self, key, default=None):
        return self.__items.get(key, default)

    def add(self, key, value=None):
        if value:
            self.__items[key] = value
            return None

        def _decorator(cls_or_func):
            self.__items[key] = cls_or_func

        return _decorator

    def __call__(self, key, value=None):
        return self.add(key, value)
