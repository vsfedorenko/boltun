from __future__ import absolute_import, division, print_function

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

    def __compile__(self, compiler, environment):
        function_context = \
            FunctionContext(self.name, self.method, self.arg_params,
                            self.kwarg_params)

        compiled_function = compiler.function(environment, function_context)

        compiled_function = \
            NodeFilter.compile_sequence(compiler, environment, self.filters,
                                        compiled_function)

        if self.optional:
            if not isinstance(compiled_function, list):
                compiled_function = [compiled_function]
            compiled_function.append(None)

        return compiled_function
