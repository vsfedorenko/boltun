from __future__ import absolute_import, division, print_function

import yaml

from boltun.engine.environment.extension import Namespace, boltun


class YamlNamespace(Namespace):

    @classmethod
    def __names__(cls):
        return ['yaml']

    @boltun
    def load(self, value):
        return yaml.load(value)

    @boltun
    def dump(self, value, **kwargs):
        return yaml.dump(value, **kwargs)
