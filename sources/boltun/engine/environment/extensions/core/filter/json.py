from __future__ import absolute_import

import json

from boltun.engine.environment.extensions import Filter


class JsonFilter(Filter):
    @classmethod
    def __names__(cls):
        return ['json']

    def __apply__(self, input_, *args, **kwargs):
        return self.dump(input_, *args, **kwargs)

    @staticmethod
    def dump(input_, *args, **kwargs):
        return json.dumps(input_, *args, **kwargs)
