from __future__ import absolute_import, division, print_function

import attr

from boltun.engine.environment.extension import Function


@attr.s
class IncludeFunction(Function):

    @classmethod
    def __names__(cls):
        return ['include']

    def __execute__(self, *args, **kwargs):
        pass
