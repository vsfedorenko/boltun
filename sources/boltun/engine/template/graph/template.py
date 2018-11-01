import attr

from boltun.engine.environment import Environment
from boltun.engine.template import Sample, Template
from .nodes import Any, Call, Const


@attr.s
class ObjectGraphTemplate(Template):
    _graph = attr.ib(type=list)
    _environment = attr.ib(type=Environment)

    def render(self, shuffle=False):
        return self.generator(self._graph)

    def generator(self, items):
        if not items:
            yield None
            return

        current = self.render_item(items[0])

        for forward_item in self.generator(items[1:]):
            if isinstance(current, list):
                for index, item in enumerate(current):
                    yield Sample(item, id=index, next_sample=forward_item)
            else:
                yield Sample(current, next_sample=forward_item)

    def render_item(self, item):
        result = item

        if isinstance(item, (list,)):
            result = [
                self.render_item(v)
                for v in item
            ]
        elif isinstance(item, (Any,)):
            result = [
                self.render_item(v)
                for v in item.values
            ]
        elif isinstance(item, (Call,)):
            current_callable = item.callable
            result = current_callable()
        elif isinstance(item, Const):
            result = item.value

        return result
