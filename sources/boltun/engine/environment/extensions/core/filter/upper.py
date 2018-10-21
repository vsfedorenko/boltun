from __future__ import absolute_import

from boltun.engine.environment.extensions import Filter


class UpperFilter(Filter):

    @classmethod
    def __names__(cls):
        return ['upper', 'uppercase']

    def __apply__(self, input_, *args, **kwargs):
        if isinstance(input_, (list,)):
            return [v.upper() for v in input_]

        return input_.upper()
