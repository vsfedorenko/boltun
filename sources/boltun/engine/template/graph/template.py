import attr

from boltun.engine.environment import Environment
from boltun.engine.template import Template


@attr.s
class ObjectGraphTemplate(Template):
    _graph = attr.ib(type=list)
    _environment = attr.ib(type=Environment)

    def render(self):
        return self._generator(self._graph)

    def _generator(self, items):
        if not items:
            yield ""
        else:
            current_item = items.pop()

            if callable(current_item):
                current_item = current_item()

            forward_generator = self._generator(items)

            if isinstance(current_item, list):
                for forward_item in forward_generator:
                    for item in current_item:
                        yield str(forward_item) + str(item)
            else:
                for forward_item in forward_generator:
                    yield str(forward_item) + str(current_item)
