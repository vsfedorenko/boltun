from __future__ import absolute_import, division, print_function

import attr

from boltun.engine.grammar.antlr4.node import NodeFilter
from boltun.engine.grammar.nodes import FunctionNode
from boltun.engine.template.context import FunctionContext
from ._base import LeafNode


@attr.s
class CallNode(LeafNode, FunctionNode):
    optional = attr.ib(type=bool, default=False)
    arg_params = attr.ib(type=list, factory=list)
    kwarg_params = attr.ib(type=dict, factory=dict)

    def __compile__(self, compiler, environment):
        function_context = \
            FunctionContext(self.name, self.arg_params, self.kwarg_params)

        compiled_function = compiler.function(environment, function_context)

        compiled_function = \
            NodeFilter.compile_sequence(compiler, environment, self.filters,
                                        compiled_function)

        if self.optional:
            compiled_function = compiler.optional(compiled_function)

        return compiled_function
