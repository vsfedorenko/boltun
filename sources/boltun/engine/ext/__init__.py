import logging
from abc import ABCMeta

import attr
from six import with_metaclass

from .base import (Filter, Function)

LOGGER = logging.getLogger(__name__)


@attr.s
class Extension(with_metaclass(ABCMeta, object)):

    def functions(self):
        return []

    def filters(self):
        return []


@attr.s
class ExtensionSet(object):
    _engine = attr.ib()
    _extensions = attr.ib(type=dict, default=attr.Factory(dict))
    _functions = attr.ib(type=dict, default=attr.Factory(dict))
    _filters = attr.ib(type=dict, default=attr.Factory(dict))

    def append(self, extension, force_replace=False):
        self._init_extension(extension)

    def extend(self, extensions, force_replace=False):
        for extension in extensions:
            self.append(extension, force_replace)

    def get_extension(self, type_):
        return self._extensions[type_]

    def get_extensions(self):
        return dict(self._extensions)

    def get_functions(self):
        return dict(self._functions)

    def get_filters(self):
        return dict(self._filters)

    def _init_extension(self, extension):
        for function_ in extension.functions():
            self._init_function(function_)

        for filter_ in extension.filters():
            self._init_function(filter_)

        self._extensions[type(extension)] = extension

    def _init_function(self, function_):
        pass

    def _init_filter(self, filter_):
        pass
