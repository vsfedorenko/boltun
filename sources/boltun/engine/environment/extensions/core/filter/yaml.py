from __future__ import absolute_import, division, print_function

from boltun.engine.environment.extensions import Filter


class YamlFilter(Filter):

    @classmethod
    def __names__(cls):
        return ['yaml']

    def __apply__(self, input_, *args, **kwargs):
        pass
