from __future__ import absolute_import

from boltun.engine.ext import Function


class EnvFunction(Function):

    def __execute__(self, *args, **kwargs):
        pass


__all__ = ['EnvFunction']
