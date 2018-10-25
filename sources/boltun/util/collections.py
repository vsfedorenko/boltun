from __future__ import absolute_import, division, print_function

import attr


@attr.s
class Stack(object):
    __items = attr.ib(type=list, default=attr.Factory(list))

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    def is_empty(self):
        return len(self.__items) == 0
