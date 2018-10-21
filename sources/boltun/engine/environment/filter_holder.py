import attr
import six

from boltun.engine.environment.extensions import Filter


@attr.s
class FilterHolder(object):
    _environment = attr.ib()
    _items = attr.ib(type=dict, default=attr.Factory(dict), init=False)

    def add(self, filter_, names=None):
        if not names:
            names = self._get_filter_names(filter_)

        for name in names:
            if name in self._items:
                raise KeyError(
                    "Filter '{name}' is already defined".format(name=name))

        self.set(filter_, names)

    def set(self, filter_, names=None):
        if not names:
            names = self._get_filter_names(filter_)

        if not names:
            raise ValueError(
                "No names were provided for filter: {fltr}".format(
                    fltr=filter_))

        for name in names:
            self._items[name] = filter_

    def extend(self, list_or_dict, set_=False):
        func = self.set if set_ else self.add

        if isinstance(list_or_dict, (list,)):
            for v in list_or_dict:
                func(v)

        if isinstance(list_or_dict, (dict,)):
            for k, v in six.iteritems(list_or_dict):
                func(v, k)

    def get(self, name):
        if name not in self._items:
            raise KeyError(
                "No filter with name '{name}' were found".format(name=name))

        filter_callable = self._items[name]

        if issubclass(filter_callable, Filter):
            instance = filter_callable(self._environment)
            return instance.__apply__

        return filter_callable

    @staticmethod
    def _get_filter_names(filter_):
        names = None

        if issubclass(filter_, (Filter,)):
            names = filter_.__names__()
        elif filter_.__boltun_names__:
            names = filter_.__boltun_names__

        return names
