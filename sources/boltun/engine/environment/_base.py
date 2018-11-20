from __future__ import absolute_import, division, print_function

import inspect

import attr

from boltun.engine.environment.extension import BoltunContext, Extension, \
    FilterDef, FunctionDef, Namespace


@attr.s
class Environment(object):
    engine = attr.ib()

    extensions = attr.ib(type=dict, factory=dict, init=False)
    functions = attr.ib(type=dict, factory=dict, init=False)
    filters = attr.ib(type=dict, factory=dict, init=False)
    variables = attr.ib(type=dict, factory=dict, init=False)

    def add_extension(self, maybe_extension):
        extension = maybe_extension() \
            if inspect.isclass(maybe_extension) else maybe_extension

        if not isinstance(extension, Extension):
            raise ValueError("Undefined values was passed as Extension")

        for namespace in extension.__namespaces__():
            self._add_namespace(namespace)

        decorated_members = self.__get_decorated_methods(extension)
        for member in decorated_members:
            print(member)

        for function_ in extension.__functions__():
            self.add_function(function_)

        for filter_ in extension.__filters__():
            self.add_filter(filter_)

        self.extensions[type(extension)] = extension

    def get_extensions(self):
        return dict(self.extensions)

    def get_extension(self, extension_type):
        return self.extensions[extension_type]

    def add_function(self, function_):
        if isinstance(function_, FunctionDef):
            pass
        return

    def get_functions(self):
        pass

    def get_function(self, name):
        pass

    def add_filter(self, filter_):
        if isinstance(filter_, FilterDef):
            pass
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

    def _add_namespace(self, maybe_namespace, name_prefix=None):
        namespace = maybe_namespace() \
            if inspect.isclass(maybe_namespace) else maybe_namespace

        if not isinstance(namespace, Namespace):
            raise ValueError("Undefined values was passed as Namespace")

        names = namespace.__names__()

        for sub_namespace in namespace.__namespaces__():
            self._add_namespace(sub_namespace, name_prefix=names)

        for function_ in namespace.__functions__():
            self.add_function(function_)

        for filter_ in namespace.__filters__():
            self.add_filter(filter_)

    @classmethod
    def __get_decorated_methods(cls, target):
        decorator_attribute = BoltunContext.__decorator_attribute__()

        for member in inspect.getmembers(target.__class__, inspect.ismethod):
            method = member[1]

            if hasattr(method, decorator_attribute):
                context = getattr(method, decorator_attribute)

                yield method, context
            else:
                continue
