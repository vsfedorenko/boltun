import random

import attr

from boltun.engine.environment import Environment
from boltun.engine.template import Template
from .nodes import Any, Call, Const


@attr.s
class ObjectGraphTemplate(Template):
    _graph = attr.ib(type=list)
    _environment = attr.ib(type=Environment)

    def render(self, shuffle=False):
        return self.__generator(self._graph, shuffle)

    def __generator(self, items, shuffle=False):
        if not items:
            yield ""
        else:
            current = items.pop()

            current = self.__render_item(current, shuffle=shuffle)

            forward_generator = self.__generator(items, shuffle=shuffle)

            if isinstance(current, list):
                current = [
                    self.__render_item(item, shuffle=shuffle)
                    for item in current
                ]

                if shuffle:
                    random.shuffle(current)

                for forward_item in forward_generator:
                    for item in current:
                        yield str(forward_item) + str(item)
            else:
                for forward_item in forward_generator:
                    yield str(forward_item) + str(current)

    def __render_item(self, item, shuffle=False):
        result = item

        if isinstance(item, list):
            result = "".join([
                self.__render_item(v, shuffle=shuffle)
                for v in item
            ])
        elif isinstance(item, Any):
            result = [
                self.__render_item(v, shuffle=shuffle)
                for v in item.values
            ]
        elif isinstance(item, Call):
            current_callable = item.callable
            result = current_callable()
        elif isinstance(item, Const):
            result = item.value

        if isinstance(result, list):
            if shuffle:
                random.shuffle(result)

        return result
