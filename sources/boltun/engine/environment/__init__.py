from __future__ import absolute_import, division, print_function

import attr

from boltun.engine.environment.namespace_holder import NamespaceHolder
from .variable_holder import VariableHolder


@attr.s
class Environment(object):
    engine = attr.ib()

    variables = attr.ib(type=VariableHolder,
                        default=attr.Factory(VariableHolder, takes_self=True),
                        init=False)

    namespaces = attr.ib(type=NamespaceHolder,
                         default=attr.Factory(NamespaceHolder,
                                              takes_self=True), init=False)

    extensions = attr.ib(type=dict, factory=dict, init=False)

    def get_extensions(self):
        return dict(self.extensions)

    def get_extension(self, extension_type):
        return self.extensions[extension_type]

    def add_extension(self, extension, replace=False):
        extension_type = type(extension)

        if not replace and extension_type in self.extensions:
            raise KeyError("Extension '{type}' is already "
                           "registered".format(type=extension_type))

        self.extensions[extension_type] = extension


__all__ = ['Environment']
