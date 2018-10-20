from __future__ import absolute_import

from abc import ABCMeta, abstractmethod as abstract_method

import attr
from six import with_metaclass

from boltun.engine.grammar.antlr4.node import NodeFilter
from .base import LeafNode


@attr.s
class EntityNode(with_metaclass(ABCMeta, LeafNode)):
    name = attr.ib()
    ref_names = attr.ib(type=list, default=attr.Factory(list))
    optional = attr.ib(default=False)
    filters = attr.ib(type=list, default=attr.Factory(list))

    def add_filter(self, filter_):
        # type: (NodeFilter) -> None
        self.filters.append(filter_)

    def add_filters(self, filters):
        self.filters.extend(filters)

    def __compile__(self, compiler):
        compiled_values = [self.__entity__(compiler)]

        compiled_values = \
            NodeFilter.compile_sequence(compiler, self.filters, compiled_values)

        if self.optional:
            compiled_values.append(None)

        if len(compiled_values) == 1:
            return compiled_values[0]

        return compiled_values

    @abstract_method
    def __entity__(self, compiler):
        raise NotImplementedError()


@attr.s
class IntentNode(EntityNode):

    def __entity__(self, compiler):
        return compiler.entity('intent', self.name, self.ref_names)


@attr.s
class AliasNode(EntityNode):

    def __entity__(self, compiler):
        return compiler.entity('alias', self.name, self.ref_names)


@attr.s
class SlotNode(EntityNode):

    def __entity__(self, compiler):
        return compiler.entity('slot', self.name, self.ref_names)


__all__ = ['EntityNode', 'IntentNode', 'AliasNode', 'SlotNode']
