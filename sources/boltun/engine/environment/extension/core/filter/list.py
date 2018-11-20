from __future__ import absolute_import, division, print_function

import ast
import sys

import attr
import six

from boltun.engine.environment.extension import Filter


@attr.s
class ListFilter(Filter):

    @classmethod
    def __names__(cls):
        return ['list']

    def __apply__(self, input_, *args, **kwargs):
        return list(ast.literal_eval(input_))

    def split(self, input_, sep=',', maxsplit=None, **kwargs):
        if not maxsplit:
            maxsplit = sys.maxsize

        if isinstance(input_, six.string_types):
            return input_.split(sep, maxsplit)