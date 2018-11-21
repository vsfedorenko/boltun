from __future__ import absolute_import, division, print_function

import attr

from boltun.engine.template import Compiler
from .nodes import Any, Call, Const
from .template import ObjectGraphTemplate


@attr.s
class ObjectGraphCompiler(Compiler):

    def __process__(self, grammar_node_tree, environment):
        compiled_obj_graph = grammar_node_tree.__compile__(self, environment)
        return compiled_obj_graph

    def __template__(self, grammar_node_tree, environment):
        compiled_obj_graph = self.__process__(grammar_node_tree, environment)
        return ObjectGraphTemplate(compiled_obj_graph, environment)

    def function(self, environment, function_context):
        function_name = function_context.name
        function_args = function_context.arg_params
        function_kwargs = function_context.kwarg_params

        function_callable = environment.get_function(function_name)

        def defer_function_callable():
            return function_callable(*function_args, **function_kwargs)

        return Call(defer_function_callable)

    def filter(self, environment, filter_context):
        filter_name = filter_context.name
        filter_value = filter_context.value
        filter_args = filter_context.arg_params
        filter_kwargs = filter_context.kwarg_params

        filter_callable = environment.get_filter(filter_name)

        def defer_filter_callable():
            return filter_callable(filter_value(), *filter_args,
                                   **filter_kwargs)

        return Call(defer_filter_callable)

    def text(self, environment, value):
        return Const(value)

    def concat(self, part, *other_parts):
        parts = [part]

        if other_parts:
            parts.extend(other_parts)

        concat_parts = []
        for part_item in parts:
            if isinstance(part_item, list):
                concat_parts.extend(part_item)
            else:
                concat_parts.append(part_item)

        return concat_parts

    def any(self, choice, *other_choices):
        choices = [choice]

        if other_choices:
            choices.extend(other_choices)

        if len(choices) < 2:
            raise ValueError("Choices count must be greater or equal 2")

        return Any(choices)
