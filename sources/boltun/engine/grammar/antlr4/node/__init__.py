from __future__ import absolute_import, division, print_function

from abc import abstractmethod as abstract_method

import attr

from boltun.engine.grammar.nodes import Node as BaseNode, \
    NodeFilter as BaseFilter
from boltun.engine.template.context import FilterContext


@attr.s
class Node(BaseNode):
    start = attr.ib(type=int, default=None, init=False)
    stop = attr.ib(type=int, default=None, init=False)

    @abstract_method
    def __compile__(self, compiler, environment):
        raise NotImplementedError()


@attr.s
class NodeFilter(BaseFilter):
    ref_names = attr.ib(type=list, factory=list)
    optional = attr.ib(type=bool, default=False)
    arg_params = attr.ib(type=list, factory=list)
    kwarg_params = attr.ib(type=dict, factory=dict)

    def __compile__(self, compiler, environment, values):
        if not isinstance(values, (list,)):
            values = [values]

        filtered_values = []
        if self.optional:
            filtered_values.extend(values)

        filtered_values.extend([
            compiler.filter(
                environment,
                FilterContext(
                    name=self.name, value=value,
                    ref_names=self.ref_names,
                    arg_params=self.arg_params,
                    kwarg_params=self.kwarg_params
                )
            )

            if value is not None else None
            for value in values
        ])

        return filtered_values
