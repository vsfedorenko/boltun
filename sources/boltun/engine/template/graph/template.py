import random

import attr

from boltun.engine.environment import Environment
from boltun.engine.template import Template
from .nodes import Any, Call, Const


@attr.s
class ObjectGraphTemplate(Template):
    _graph = attr.ib(type=list)
    _environment = attr.ib(type=Environment)

    def render(self):
        return self.__generator(self._graph)

    def __generator(self, items, shuffle=False):
        if not items:
            yield ""
            return
        else:
            current = items.pop()

            current = self.__render_item(current)

            forward_generator = self.__generator(items)

            if isinstance(current, list):
                current = [
                    self.__render_item(item)
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

    def __render_item(self, item):
        if isinstance(item, list):
            return "".join([self.__render_item(v) for v in item])

        if isinstance(item, Any):
            return [self.__render_item(v) for v in item.values]

        if isinstance(item, Call):
            current_callable = item.callable
            return current_callable()

        if isinstance(item, Const):
            return item.value

        return item
