from __future__ import absolute_import

from boltun.engine.ext import Function


class IncludeFunction(Function):

    def __names__(self):
        return ['include']

    def __execute__(self, *args, **kwargs):
        pass


__all__ = ['IncludeFunction']
