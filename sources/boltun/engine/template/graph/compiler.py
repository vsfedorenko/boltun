from __future__ import absolute_import

import attr

from boltun.engine.template import Compiler
from .nodes import Call, Const, Entity
from .template import ObjectGraphTemplate


@attr.s
class ObjectGraphCompiler(Compiler):

    def __process__(self, grammar_node_tree, environment):
        compiled_obj_graph = grammar_node_tree.__compile__(self, environment)
        return compiled_obj_graph

    def __template__(self, grammar_node_tree, environment):
        compiled_obj_graph = self.__process__(grammar_node_tree, environment)
        return ObjectGraphTemplate(compiled_obj_graph, environment)

    def entity(self, environment, type_, name, ref_names):
        return Entity(type_, name, ref_names)

    def function(self, environment, function_context):
        function_name = function_context.name
        function_method = function_context.method
        function_args = function_context.arg_params
        function_kwargs = function_context.kwarg_params

        function_callable = \
            environment.functions.get(function_name, function_method)

        def defer_function_callable():
            return function_callable(*function_args, **function_kwargs)

        return Call(defer_function_callable)

    def filter(self, environment, filter_context):
        filter_name = filter_context.name
        filter_value = filter_context.value
        filter_args = filter_context.arg_params
        filter_kwargs = filter_context.kwarg_params

        filter_callable = environment.filters.get(filter_name)

        def defer_filter_callable():
            return filter_callable(filter_value(), *filter_args,
                                   **filter_kwargs)

        return Call(defer_filter_callable)

    def text(self, environment, value):
        return Const(value)

    def nothing(self, environment):
        super(ObjectGraphCompiler, self).nothing(environment)

    def concat(self, parts, *other_parts):
        return super(ObjectGraphCompiler, self).concat(parts, *other_parts)

    def any(self, choices, *other_choices):
        return super(ObjectGraphCompiler, self).any(choices, *other_choices)
