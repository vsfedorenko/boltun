import attr

from boltun.engine.environment.extensions import Extension
from boltun.engine.environment.extensions.core.filter import JsonFilter, \
    ListFilter, StringFilter, YamlFilter
from boltun.engine.environment.extensions.core.function import AnyFunction, \
    EchoFunction, EnvironmentFunction, IncludeFunction, RangeFunction, \
    RepeatFunction


@attr.s
class CoreExtension(Extension):

    def functions(self):
        return [
            AnyFunction,
            EchoFunction,
            EnvironmentFunction,
            IncludeFunction,
            RangeFunction,
            RepeatFunction
        ]

    def filters(self):
        return [
            JsonFilter,
            ListFilter,
            StringFilter,
            YamlFilter
        ]
