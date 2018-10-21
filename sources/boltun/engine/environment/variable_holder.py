import attr


@attr.s
class VariableHolder(object):
    _environment = attr.ib()
    _items = attr.ib(type=dict, default=attr.Factory(dict), init=False)

    def add(self, name, value):
        if name in self._items:
            raise KeyError(
                "Variable '{name}' is already defined".format(name=name))

        self.set(name, value)

    def set(self, name, value):
        self._items[name] = value

    def get(self, name):
        return self._items[name]

    def get_or_default(self, name, default=None):
        try:
            return self.get(name)
        except KeyError:
            return default
