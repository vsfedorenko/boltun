from __future__ import absolute_import, division, print_function

import json

from boltun.engine.environment.extension import Namespace, boltun_filter, \
    boltun_function


class JsonNamespace(Namespace):

    @classmethod
    def __names__(cls):
        return ['json']

    @boltun_function()
    @boltun_filter()
    def load(self, value, *args, **kwargs):
        return json.loads(value, *args, **kwargs)

    @boltun_function()
    @boltun_filter()
    def dump(self, value, *args, **kwargs):
        return json.dumps(value, *args, **kwargs)
