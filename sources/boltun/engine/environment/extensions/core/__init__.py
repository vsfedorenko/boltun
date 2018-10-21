import attr

from boltun.engine.environment.extensions import Extension
from boltun.engine.environment.extensions.core.filter import LowerFilter, \
    SplitFilter, ToStringFilter, UpperFilter
from boltun.engine.environment.extensions.core.function import EchoFunction, \
    EnvironmentFunction, IncludeFunction, RangeFunction


@attr.s
class CoreExtension(Extension):

    def functions(self):
        return [
            EchoFunction,
            EnvironmentFunction,
            IncludeFunction,
            RangeFunction
        ]

    def filters(self):
        return [
            LowerFilter,
            SplitFilter,
            ToStringFilter,
            UpperFilter,
        ]
