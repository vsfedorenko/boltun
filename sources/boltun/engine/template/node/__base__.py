from __future__ import absolute_import

from abc import ABCMeta, abstractmethod as abstract_method

import attr
from six import with_metaclass


@attr.s
class Node(with_metaclass(ABCMeta, object)):
    start = attr.ib(type=int, default=None, init=False)
    stop = attr.ib(type=int, default=None, init=False)

    @abstract_method
    def __compile__(self, compiler):
        raise NotImplementedError()


@attr.s
class Filter(object):
    name = attr.ib()
    optional = attr.ib()
    args = attr.ib(type=list, default=[])
    kwargs = attr.ib(type=dict, default={})

    def __compile__(self, compiler, values):
        if isinstance(values, (list,)):
            values = [values]

        filtered_values = []
        if self.optional:
            filtered_values.extend(values)

        filtered_values.extend([
            compiler.filter(self.name, value, self.args, self.kwargs)
            if value is not None else None
            for value in values
        ])

        return filtered_values

    @staticmethod
    def compile_sequence(compiler, filters, values):
        if not filters:
            return values

        filter_ = filters[0]
        filtered_values = filter_.__compile__(compiler, values)

        return Filter.compile_sequence(compiler, filters[1:], filtered_values)
