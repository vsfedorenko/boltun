import attr

from boltun.engine.ext import Extension
from boltun.engine.ext.core.filter import LowerFilter, UpperFilter
from boltun.engine.ext.core.function import EchoFunction, EnvFunction, \
    IncludeFunction


@attr.s
class CoreExtension(Extension):

    def functions(self):
        return [
            EchoFunction,
            EnvFunction,
            IncludeFunction,
        ]

    def filters(self):
        return [
            LowerFilter,
            UpperFilter,
        ]
