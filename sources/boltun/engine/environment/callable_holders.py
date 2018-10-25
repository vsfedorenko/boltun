from __future__ import absolute_import, division, print_function

from abc import ABCMeta, abstractmethod as abstract_method

import attr
import six
from six import with_metaclass

from boltun.engine.environment.extensions import Filter, Function


@attr.s
class CallableHolder(with_metaclass(ABCMeta, object)):
    _environment = attr.ib()
    _items = attr.ib(type=dict, default=attr.Factory(dict), init=False)

    @classmethod
    @abstract_method
    def callable_name(cls):
        raise NotImplementedError()

    @classmethod
    @abstract_method
    def callable_class_type(cls):
        raise NotImplementedError()

    @abstract_method
    def default_class_method(self, instance):
        raise NotImplementedError()

    def add(self, function_, names=None):
        if not names:
            names = self._get_names(function_)

        if not names:
            raise ValueError(
                "No names were provided "
                "for the {callable_name}: {func}".format(
                    callable_name=self.callable_name(), func=function_))

        for name in names:
            if name in self._items:
                raise KeyError(
                    "{callable_name} '{name}' is already defined".format(
                        callable_name=self.callable_name().capitalize(),
                        name=name))

        self.set(function_, names)

    def set(self, function_, names=None):
        if not names:
            names = self._get_names(function_)

        if not names:
            raise ValueError(
                "No names were provided "
                "for the {callable_name}: {func}".format(
                    callable_name=self.callable_name(), func=function_))

        for name in names:
            self._items[name] = function_

    def extend(self, list_or_dict, set_=False):
        func = self.set if set_ else self.add

        if isinstance(list_or_dict, (list,)):
            for v in list_or_dict:
                func(v)

        if isinstance(list_or_dict, (dict,)):
            for k, v in six.iteritems(list_or_dict):
                func(v, k)

    def get(self, name, method=None):
        if name not in self._items:
            raise KeyError(
                "No {callable_name} with "
                "name '{name}' were found".format(
                    callable_name=self.callable_name(), name=name))

        callable_ = self._items[name]

        if issubclass(callable_, self.callable_class_type()):
            instance = callable_(self._environment)

            if method:
                return getattr(instance, method)

            return self.default_class_method(instance)

        return callable_

    def _get_names(self, callable_):
        names = None

        if issubclass(callable_, self.callable_class_type()):
            names = callable_.__names__()
            if not isinstance(names, (list,)):
                names = [names]
        elif callable_.__boltun_names__:
            names = callable_.__boltun_names__

        return names


@attr.s
class FunctionHolder(CallableHolder):

    @classmethod
    def callable_name(cls):
        return 'function'

    @classmethod
    def callable_class_type(cls):
        return Function

    def default_class_method(self, instance):
        return instance.__execute__


@attr.s
class FilterHolder(CallableHolder):

    @classmethod
    def callable_name(cls):
        return 'filter'

    @classmethod
    def callable_class_type(cls):
        return Filter

    def default_class_method(self, instance):
        return instance.__apply__
