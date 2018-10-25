from __future__ import absolute_import, division, print_function

import attr

from boltun.engine.environment.extension import Function


@attr.s
class RangeFunction(Function):

    @classmethod
    def __names__(cls):
        return ['range']

    def __execute__(self, x, y, step=1, **kwargs):
        return list(range(x, y, step))
