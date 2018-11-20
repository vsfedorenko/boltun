from __future__ import absolute_import, division, print_function

import attr

from boltun.engine.environment.extension import Extension, Namespace


@attr.s
class Environment(object):
    engine = attr.ib()

    extensions = attr.ib(type=dict, factory=dict, init=False)
    namespaces = attr.ib(type=dict, factory=dict, init=False)
    functions = attr.ib(type=dict, factory=dict, init=False)
    filters = attr.ib(type=dict, factory=dict, init=False)
    variables = attr.ib(type=dict, factory=dict, init=False)

    def add_extension(self, extension_type):
        extension = extension_type(self)

        for namespace in extension.__namespaces__():
            self.add_namespace(namespace)

        for function_ in extension.__functions__():
            self.add_function(function_)

        for filter_ in extension.__filters__():
            self.add_filter(filter_)

        self.extensions[type(extension)] = extension

    def get_extensions(self):
        return dict(self.extensions)

    def get_extension(self, extension_type):
        return self.extensions[extension_type]

    def add_namespace(self, namespace_type, name_prefix=None):
        namespace = namespace_type(self)
        names = namespace.__names__()

        for name in names:
            self.namespaces[name] = namespace

        for function_ in namespace.__functions__():
            self.add_function(function_)

        for filter_ in namespace.__filters__():
            self.add_filter(filter_)

        for sub_namespace in namespace.__namespaces__():
            self.add_namespace(sub_namespace, name_prefix=names)

    def get_namespaces(self):
        pass

    def get_namespace(self, name):
        pass

    def add_function(self, function_):
        return

    def get_functions(self):
        pass

    def get_function(self, name):
        pass

    def add_filter(self, filter_):
        return

    def get_filters(self):
        pass

    def get_filter(self, name):
        pass

    def set_variable(self, name, value):
        pass

    def get_variable(self, name):
        pass

    def del_variable(self, name):
        pass
