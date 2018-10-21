from __future__ import absolute_import

from boltun.engine.environment.extensions import Filter


class LowerFilter(Filter):

    @classmethod
    def __names__(cls):
        return ['lower', 'lowercase']

    def __apply__(self, input_, *args, **kwargs):
        if isinstance(input_, (list,)):
            return [v.lower() for v in input_]

        return input_.lower()
