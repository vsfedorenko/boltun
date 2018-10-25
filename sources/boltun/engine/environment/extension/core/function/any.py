from __future__ import absolute_import, division, print_function

import attr

from boltun.engine.environment.extension import Function


@attr.s
class AnyFunction(Function):

    @classmethod
    def __names__(cls):
        return ['any', 'any_of']

    def __execute__(self, *args, **kwargs):
        return list(args)
