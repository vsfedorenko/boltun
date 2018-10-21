import sys

import six

from boltun.engine.environment.extensions import Filter


class SplitFilter(Filter):

    @classmethod
    def __names__(cls):
        return ['split']

    def __apply__(self, input_, sep=',', maxsplit=None, **kwargs):
        if not maxsplit:
            maxsplit = sys.maxsize

        if isinstance(input_, six.string_types):
            return input_.split(sep, maxsplit)
