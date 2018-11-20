from __future__ import absolute_import, division, print_function

import json

from boltun.engine.environment.extension import Namespace, boltun
from .yaml import YamlNamespace
from boltun.util import recursive


class JsonNamespace(Namespace):

    def __names__(self):
        return ['json']

    def __namespaces__(self):
        return [YamlNamespace]

    @boltun
    @recursive
    def load(self, value, *args, **kwargs):
        return json.loads(value, *args, **kwargs)

    @boltun
    def dump(self, value, *args, **kwargs):
        return json.dumps(value, *args, **kwargs)
