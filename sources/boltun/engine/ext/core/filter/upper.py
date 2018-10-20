from __future__ import absolute_import

from boltun.engine.ext import Filter


class UpperFilter(Filter):

    def __names__(self):
        return ['upper', 'uppercase']

    def __apply__(self, input_, *args, **kwargs):
        pass


__all__ = ['UpperFilter']
