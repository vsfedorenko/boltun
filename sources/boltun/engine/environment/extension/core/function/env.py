from __future__ import absolute_import, division, print_function

import os

import attr

from boltun.engine.environment.extension import Function


@attr.s
class EnvironmentFunction(Function):

    @classmethod
    def __names__(cls):
        return ['env', 'environ', 'environment']

    def __execute__(self, name, *args, **kwargs):
        return os.environ.get(name)
