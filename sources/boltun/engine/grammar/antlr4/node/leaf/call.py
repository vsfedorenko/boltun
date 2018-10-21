from __future__ import absolute_import

import attr
import six

from boltun.engine.grammar.antlr4.node import NodeFilter
from boltun.engine.grammar.nodes import FunctionNode
from boltun.engine.template.context import FunctionContext
from .base import LeafNode


@attr.s
class CallNode(LeafNode, FunctionNode):
    optional = attr.ib(type=bool, default=False)
    method = attr.ib(type=six.string_types, default=None)
    arg_params = attr.ib(type=list, default=attr.Factory(list))
    kwarg_params = attr.ib(type=dict, default=attr.Factory(dict))

    def add_filter(self, filter_):
        # type: (NodeFilter) -> None
        self.filters.append(filter_)

    def add_filters(self, filters):
        self.filters.extend(filters)

    def __compile__(self, compiler, environment):
        function_context = \
            FunctionContext(self.name, self.method, self.arg_params,
                            self.kwarg_params)

        compiled_function = compiler.function(environment, function_context)

        compiled_function = \
            NodeFilter.compile_sequence(compiler, environment, self.filters,
                                        compiled_function)

        if self.optional:
            compiled_function.append(None)

        if isinstance(compiled_function, list) and len(compiled_function) == 1:
            return compiled_function[0]

        return compiled_function


__all__ = ['CallNode']
