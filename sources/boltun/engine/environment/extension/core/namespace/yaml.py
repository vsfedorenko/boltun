from __future__ import absolute_import, division, print_function

import yaml

from boltun.engine.environment.extension import Namespace, boltun_filter, \
    boltun_function


class YamlNamespace(Namespace):

    @classmethod
    def __names__(cls):
        return ['yaml']

    @boltun_function()
    @boltun_filter()
    def load(self, value):
        return yaml.load(value)

    @boltun_function()
    @boltun_filter()
    def dump(self, value, **kwargs):
        return yaml.dump(value, **kwargs)
