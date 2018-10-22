from __future__ import absolute_import

from boltun.engine.environment.extensions import Function


class RangeFunction(Function):

    @classmethod
    def __names__(cls):
        return ['range']

    def __execute__(self, x, y, step=1):
        return list(range(x, y, step))
