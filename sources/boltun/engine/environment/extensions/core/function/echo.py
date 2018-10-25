from __future__ import absolute_import, division, print_function

from boltun.engine.environment.extensions import Function


class EchoFunction(Function):

    @classmethod
    def __names__(cls):
        return ['echo', 'print']

    def __execute__(self, value):
        return value
