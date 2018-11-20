from __future__ import absolute_import, division, print_function

import yaml

from boltun.engine.environment.extension import Namespace, boltun
from boltun.util import recursive


class YamlNamespace(Namespace):

    def __names__(self):
        return ['yaml']

    @boltun
    @recursive
    def load(self, value):
        return yaml.load(value)

    @boltun
    def dump(self, value, **kwargs):
        return yaml.dump(value, **kwargs)
