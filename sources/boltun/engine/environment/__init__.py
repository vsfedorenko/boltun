import attr

from .callable_holders import (FilterHolder, FunctionHolder)
from .variable_holder import VariableHolder


@attr.s(frozen=True)
class Environment(object):
    engine = attr.ib()

    variables = attr.ib(type=VariableHolder,
                        default=attr.Factory(VariableHolder, takes_self=True),
                        init=False)

    functions = attr.ib(type=FunctionHolder,
                        default=attr.Factory(FunctionHolder, takes_self=True),
                        init=False)

    filters = attr.ib(type=FilterHolder,
                      default=attr.Factory(FilterHolder, takes_self=True),
                      init=False)

    _extensions = attr.ib(type=dict, default=attr.Factory(dict), init=False)

    def get_extensions(self):
        return dict(self._extensions)

    def get_extension(self, extension_type):
        return self._extensions[extension_type]

    def add_extension(self, extension, replace=False):
        extension_type = type(extension)

        if not replace and extension_type in self._extensions:
            raise KeyError("Extension '{type}' is already "
                           "registered".format(type=extension_type))

        self.functions.extend(extension.functions(), replace)
        self.filters.extend(extension.filters(), replace)

        self._extensions[extension_type] = extension


__all__ = ['Environment']
