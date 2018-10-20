from __future__ import absolute_import

import attr
import six

from boltun.engine.grammar.antlr4.node import NodeFilter
from boltun.engine.grammar.nodes import FunctionNode
from .base import LeafNode


@attr.s
class CallNode(LeafNode, FunctionNode):
    optional = attr.ib(type=bool, default=False)
    method = attr.ib(type=six.string_types, default=None)
    arg_params = attr.ib(type=list, default=attr.Factory(list))
    kwarg_params = attr.ib(type=dict, default=attr.Factory(dict))
    filters = attr.ib(type=list, default=attr.Factory(list))

    def add_filter(self, filter_):
        # type: (NodeFilter) -> None
        self.filters.append(filter_)

    def add_filters(self, filters):
        self.filters.extend(filters)

    def __compile__(self, compiler):
        compiled_values = [
            compiler.function(self.name, self.method, self.arg_params,
                              self.kwarg_params)
        ]

        compiled_values = \
            NodeFilter.compile_sequence(compiler, self.filters,
                                        compiled_values)

        if self.optional:
            compiled_values.append(None)

        if len(compiled_values) == 1:
            return compiled_values[0]

        return compiled_values


__all__ = ['CallNode']
