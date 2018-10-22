import random

import attr

from boltun.engine.environment import Environment
from boltun.engine.template import Template


@attr.s
class ObjectGraphTemplate(Template):
    _graph = attr.ib(type=list)
    _environment = attr.ib(type=Environment)

    def render(self):
        return self._generator(self._graph)

    def _generator(self, items, shuffle=False):
        if not items:
            yield ""
            return
        else:
            current = items.pop()
            forward_generator = self._generator(items)

            if callable(current):
                current = current()

            if isinstance(current, list):
                current = [
                    item() if callable(item) else item
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
