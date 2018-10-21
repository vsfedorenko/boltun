import attr
import six

from boltun.engine.environment.extensions import Function


@attr.s
class FunctionHolder(object):
    _environment = attr.ib()
    _items = attr.ib(type=dict, default=attr.Factory(dict), init=False)

    def add(self, function_, names=None):
        if not names:
            names = self._get_function_names(function_)

        for name in names:
            if name in self._items:
                raise KeyError(
                    "Function '{name}' is already defined".format(name=name))

        self.set(function_, names)

    def set(self, function_, names=None):
        if not names:
            names = self._get_function_names(function_)

        if not names:
            raise ValueError("No names were provided "
                             "for function: {func}".format(func=function_))

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
                "No function with name '{name}' were found".format(name=name))

        function_callable = self._items[name]

        if issubclass(function_callable, Function):
            instance = function_callable(self._environment)

            if method:
                return getattr(instance, method)

            return instance.__execute__

        return function_callable

    @staticmethod
    def _get_function_names(function_):
        names = None

        if issubclass(function_, Function):
            names = function_.__names__()
        elif function_.__boltun_names__:
            names = function_.__boltun_names__

        return names
