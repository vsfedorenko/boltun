from __future__ import absolute_import, division, print_function

import attr

from boltun.engine.environment.extension import Extension
from boltun.engine.environment.extension.core.filter import ListFilter
from boltun.engine.environment.extension.core.function import AnyFunction, \
    EchoFunction, EnvironmentFunction, IncludeFunction, RangeFunction, \
    RepeatFunction
from boltun.engine.environment.extension.core.namespace import IoNamespace, \
    JsonNamespace, StringNamespace, YamlNamespace


@attr.s
class CoreExtension(Extension):

    def __namespaces__(self):
        return [
            IoNamespace,
            JsonNamespace,
            StringNamespace,
            YamlNamespace
        ]

    def __functions__(self):
        return [
            AnyFunction,
            EchoFunction,
            EnvironmentFunction,
            IncludeFunction,
            RangeFunction,
            RepeatFunction
        ]

    def __filters__(self):
        return [
            ListFilter
        ]
