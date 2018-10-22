from __future__ import absolute_import

from boltun.engine.environment.extensions import Filter


class ToStringFilter(Filter):

    @classmethod
    def __names__(cls):
        return ['str', 'to_str', 'to_string']

    def __apply__(self, input_, *args, **kwargs):
        return str(input_)