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
class FilteredNode(Node):
    filters = attr.ib(type=list, factory=list, init=False)

    @abstract_method
    def __compile__(self, compiler, environment):
        raise NotImplementedError()

    def add_filter(self, filter_):
        # type: (NodeFilter) -> None
        self.filters.append(filter_)

    def add_filters(self, filters):
        self.filters.extend(filters)


@attr.s
class FunctionNode(FilteredNode):
    name = attr.ib(type=six.string_types)

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
            if isinstance(values, list) and len(values) == 1:
                return values[0]

            return values

        filter_ = filters[0]
        filtered_values = filter_.__compile__(compiler, environment, values)

        return NodeFilter.compile_sequence(compiler, environment, filters[1:],
                                           filtered_values)
