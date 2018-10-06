from __future__ import absolute_import

from boltun.engine.ext import Function


class EchoFunction(Function):

    def __execute__(self, *args, **kwargs):
        pass


__all__ = ['EchoFunction']
