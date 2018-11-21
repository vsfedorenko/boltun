from abc import ABCMeta

import attr
from six import with_metaclass

from boltun.engine.environment.mapping._base import Mapping, MappingResolver, \
    MappingType
from ._base import FilterDef, FunctionDef


@attr.s
class DefinitionMappingResolver(with_metaclass(ABCMeta, MappingResolver)):
    pass


@attr.s
class FunctionDefinitionMappingResolver(DefinitionMappingResolver):

    def __accepts__(self, item):
        return isinstance(item, FunctionDef)

    def __apply__(self, item):
        name = item.name
        function_callable = item.callable

        return [
            Mapping(MappingType.FUNCTION, name, function_callable)
        ]


@attr.s
class FilterDefinitionMappingResolver(DefinitionMappingResolver):

    def __accepts__(self, item):
        return isinstance(item, FilterDef)

    def __apply__(self, item):
        name = item.name
        filter_callable = item.callable

        return [
            Mapping(MappingType.FILTER, name, filter_callable)
        ]
