from __future__ import absolute_import

import os

from boltun.engine.environment.extensions import Function


class EnvironmentFunction(Function):

    @classmethod
    def __names__(cls):
        return ['env', 'environ', 'environment']

    def __execute__(self, name, *args, **kwargs):
        return os.environ.get(name)
