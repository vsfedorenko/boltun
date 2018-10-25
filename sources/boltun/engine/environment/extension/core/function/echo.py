from __future__ import absolute_import, division, print_function

import attr

from boltun.engine.environment.extension import Function


@attr.s
class EchoFunction(Function):

    @classmethod
    def __names__(cls):
        return ['echo', 'print']

    def __execute__(self, value, *args, **kwargs):
        return value
