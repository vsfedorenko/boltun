from __future__ import absolute_import

import attr
import six

from boltun.engine.template.node import Filter
from .base import LeafNode


@attr.s
class CallNode(LeafNode):
    name = attr.ib()
    optional = attr.ib(type=bool, default=False)
    method = attr.ib(type=six.string_types, default=None)
    args = attr.ib(type=list, default=attr.Factory(list))
    kwargs = attr.ib(type=dict, default=attr.Factory(dict))
    filters = attr.ib(type=list, default=attr.Factory(list))

    def add_filter(self, filter_):
        # type: (Filter) -> None
        self.filters.append(filter_)

    def __compile__(self, compiler):
        compiled_values = \
            [compiler.function(self.name, self.method, self.args, self.kwargs)]

        compiled_values = \
            Filter.compile_sequence(compiler, self.filters, compiled_values)

        if self.optional:
            compiled_values.append(None)

        if len(compiled_values) == 1:
            return compiled_values[0]

        return compiled_values


__all__ = ['CallNode']
