from __future__ import absolute_import

from boltun.engine.environment.extensions import Function


class IncludeFunction(Function):

    @classmethod
    def __names__(cls):
        return ['include']

    def __execute__(self, *args, **kwargs):
        pass
