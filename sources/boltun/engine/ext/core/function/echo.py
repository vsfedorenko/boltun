from __future__ import absolute_import

from boltun.engine.ext import Function


class EchoFunction(Function):

    def __names__(self):
        return ['echo', 'print']

    def __execute__(self, *args, **kwargs):
        pass


__all__ = ['EchoFunction']
