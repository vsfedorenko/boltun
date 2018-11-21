from __future__ import absolute_import, division, print_function

import inspect

import attr

from boltun.engine.environment.extension import Extension
from boltun.engine.environment.mapping import MappingType
from boltun.engine.environment.mapping.definition import \
    FilterDefinitionMappingResolver, FunctionDefinitionMappingResolver


@attr.s
class Environment(object):
    engine = attr.ib()

    extensions = attr.ib(type=dict, factory=dict)
    functions = attr.ib(type=dict, factory=dict)
    filters = attr.ib(type=dict, factory=dict)
    variables = attr.ib(type=dict, factory=dict)

    _mapping_resolvers = attr.ib(type=list, init=False)

    @_mapping_resolvers.default
    def __init_mapping_resolvers__(self):
        return [
            FunctionDefinitionMappingResolver(),
            FilterDefinitionMappingResolver()
        ]

    def add_extension(self, maybe_extension):
        extension = maybe_extension() \
            if inspect.isclass(maybe_extension) else maybe_extension

        if not issubclass(extension.__class__, Extension):
            raise ValueError("Undefined value was passed as an Extension")

        mappings = self._get_mappings(extension)
        for mapping in mappings:
            self._apply_mapping(mapping)

        self.extensions[extension.__boltun_name__()] = extension

    def get_extensions(self):
        return self.extensions.copy()

    def get_extension(self, extension_name):
        return self.extensions[extension_name]

    def get_functions(self):
        return self.functions.copy()

    def get_function(self, name):
        return self.functions[name]

    def get_filters(self):
        return self.filters.copy()

    def get_filter(self, name):
        return self.filters[name]

    def set_variable(self, name, value):
        self.variables[name] = value
        return value

    def get_variable(self, name):
        return self.variables[name]

    def del_variable(self, name):
        del self.variables[name]

    def _get_mappings(self, extension):
        mappings = []

        candidates = []
        candidates.extend(extension.__boltun_function_definitions__())
        candidates.extend(extension.__boltun_filters_definitions__())

        for candidate in candidates:
            for resolver in self._mapping_resolvers:
                if not resolver.__accepts__(candidate):
                    continue
                mappings.extend(resolver.__apply__(candidate))
                break

        return mappings

    def _apply_mapping(self, mapping):
        mapping_type = mapping.type

        if mapping_type == MappingType.FUNCTION:
            holder = self.functions
        elif mapping_type == MappingType.FILTER:
            holder = self.filters
        else:
            raise ValueError("Undefined mapping type")

        holder[mapping.name] = mapping.callable
