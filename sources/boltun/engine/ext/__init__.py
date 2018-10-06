import logging
from abc import ABCMeta

import attr
from six import with_metaclass

from .base import (Filter, Function)

LOGGER = logging.getLogger(__name__)


@attr.s
class Extension(with_metaclass(ABCMeta, object)):
    functions = attr.ib(type=dict, default=attr.Factory(dict))
    filters = attr.ib(type=dict, default=attr.Factory(dict))

    def add_function(self, names, callable_or_function):
        if not isinstance(names, (list,)):
            names = [names]

        if not callable(callable_or_function) and not \
                isinstance(callable_or_function, (Function,)):
            raise Exception("Expecting callable or Function instance. "
                            "Got: %s" % type(callable_or_function))

        for name in names:
            if name in self.functions.keys():
                LOGGER.warn("Overriding existing "
                            "function declaration: {name}", name=name)

            self.functions[name] = callable_or_function

    def add_filter(self, names, callable_or_filter):
        if not isinstance(names, (list,)):
            names = [names]

        if not callable(callable_or_filter) and not \
                isinstance(callable_or_filter, (Filter,)):
            raise Exception("Expecting callable or Filter instance. "
                            "Got: %s" % type(callable_or_filter))

        for name in names:
            if name in self.functions.keys():
                LOGGER.warn("Overriding existing "
                            "function declaration: {name}", name=name)

            self.functions[name] = callable_or_filter
