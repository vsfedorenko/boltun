from __future__ import absolute_import, division, print_function

from boltun.engine.environment.extensions import Filter


class StringFilter(Filter):

    @classmethod
    def __names__(cls):
        return ['str']

    def __apply__(self, input_, *args, **kwargs):
        return str(input_)

    def lower(self, input_, *args, **kwargs):
        if isinstance(input_, (list,)):
            return [v.lower() for v in input_]

        return input_.lower()

    def upper(self, input_, *args, **kwargs):
        if isinstance(input_, (list,)):
            return [v.upper() for v in input_]

        return input_.upper()
