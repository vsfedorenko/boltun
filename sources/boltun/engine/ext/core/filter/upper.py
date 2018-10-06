from __future__ import absolute_import

from boltun.engine.ext import Filter


class UpperFilter(Filter):

    def __apply__(self, input_, *args, **kwargs):
        pass


__all__ = ['UpperFilter']
