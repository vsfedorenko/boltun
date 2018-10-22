import attr

from boltun.engine.environment.extensions import Extension
from boltun.engine.environment.extensions.core.filter import JsonFilter, \
    LowerFilter, SplitFilter, ToStringFilter, UpperFilter, YamlFilter
from boltun.engine.environment.extensions.core.function import AnyFunction, \
    EchoFunction, EnvironmentFunction, IncludeFunction, RangeFunction


@attr.s
class CoreExtension(Extension):

    def functions(self):
        return [
            AnyFunction,
            EchoFunction,
            EnvironmentFunction,
            IncludeFunction,
            RangeFunction
        ]

    def filters(self):
        return [
            JsonFilter,
            LowerFilter,
            SplitFilter,
            ToStringFilter,
            UpperFilter,
            YamlFilter
        ]
