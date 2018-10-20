from abc import ABCMeta, abstractmethod as abstract_method

import attr
import six
from six import with_metaclass


@attr.s
class Node(with_metaclass(ABCMeta, object)):
    """

    """

    @abstract_method
    def __compile__(self, compiler):
        raise NotImplementedError()


@attr.s
class FunctionNode(Node):
    name = attr.ib(type=six.string_types)

    @abstract_method
    def __compile__(self, compiler):
        raise NotImplementedError()


@attr.s
class NodeFilter(object):
    name = attr.ib(type=six.string_types)

    @abstract_method
    def __compile__(self, compiler, values):
        raise NotImplementedError()

    @staticmethod
    def compile_sequence(compiler, filters, values):
        if not filters:
            return values

        filter_ = filters[0]
        filtered_values = filter_.__compile__(compiler, values)

        return NodeFilter.compile_sequence(compiler, filters[1:],
                                           filtered_values)


__all__ = ['Node', 'FunctionNode', 'NodeFilter']
