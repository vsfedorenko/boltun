from __future__ import absolute_import, division, print_function

import os

from boltun.engine.environment.extensions import Function


class EnvironmentFunction(Function):

    @classmethod
    def __names__(cls):
        return ['env', 'environ', 'environment']

    def __execute__(self, name):
        return os.environ.get(name)
