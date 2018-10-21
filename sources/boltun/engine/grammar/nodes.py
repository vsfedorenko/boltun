from abc import ABCMeta, abstractmethod as abstract_method

import attr
import six
from six import with_metaclass


@attr.s
class Node(with_metaclass(ABCMeta, object)):

    @abstract_method
    def __compile__(self, compiler, environment):
        raise NotImplementedError()


@attr.s
class FunctionNode(Node):
    name = attr.ib(type=six.string_types)
    filters = attr.ib(type=list, default=attr.Factory(list))

    @abstract_method
    def __compile__(self, compiler, environment):
        raise NotImplementedError()


@attr.s
class NodeFilter(object):
    name = attr.ib(type=six.string_types)

    @abstract_method
    def __compile__(self, compiler, environment, values):
        raise NotImplementedError()

    @staticmethod
    def compile_sequence(compiler, environment, filters, values):
        if not filters:
            return values

        filter_ = filters[0]
        filtered_values = filter_.__compile__(compiler, environment, values)

        return NodeFilter.compile_sequence(compiler, environment, filters[1:],
                                           filtered_values)


__all__ = ['Node', 'FunctionNode', 'NodeFilter']
