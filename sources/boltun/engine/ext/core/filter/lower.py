from __future__ import absolute_import

from boltun.engine.ext import Filter


class LowerFilter(Filter):

    def __apply__(self, input_, *args, **kwargs):
        pass


__all__ = ['LowerFilter']
