import attr

from boltun.engine.environment import Environment
from boltun.engine.template import Sample, Template
from boltun.engine.template.graph.nodes import Optional
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

        current = self._render_item(items[0])

        for forward_item in self.generator(items[1:]):
            if isinstance(current, list):
                for index, item in enumerate(self._deep_iterate(current)):
                    yield Sample(item, id=index, next_sample=forward_item)
            elif current:
                yield Sample(current, next_sample=forward_item)
            else:
                yield Sample('', next_sample=forward_item)

    def _render_item(self, item):
        result = item
        if isinstance(item, (Call,)):
            current_callable = item.callable
            result = current_callable()
        elif isinstance(item, (Any, Const, Optional)):
            result = item()

        if isinstance(result, list):
            result = [self._render_item(v) for v in result]

        return result

    def _deep_iterate(self, items):
        if items and isinstance(items, list):
            current = self._deep_iterate(items[0])
            next = self._deep_iterate(items[1:])
            for item in current:
                yield item
            for item in next:
                yield item
        elif items is None:
            yield ''
        elif not items:
            return
        else:
            yield items
