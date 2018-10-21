import attr

from boltun.engine.environment import Environment
from boltun.engine.template import Template
from .nodes import Call, Const, Entity


@attr.s
class ObjectGraphTemplate(Template):
    _graph = attr.ib(type=list)
    _environment = attr.ib(type=Environment)

    def render(self):
        for obj in self._graph:
            if isinstance(obj, Const):
                print(obj.value)

            if isinstance(obj, Call):
                print(obj.callable())

            if isinstance(obj, Entity):
                print(obj.name)
