import attr
import yaml

from boltun.engine import Engine


@attr.s
class YamlProcessor(object):
    engine = attr.ib(default=attr.Factory(Engine))

    def __enable__(self, tag="!boltun", resolver=False):
        yaml.add_constructor(tag, self)

        if resolver:
            yaml.add_implicit_resolver(tag, self._match)

    def __call__(self, loader, node, **kwargs):
        return self.engine.render(node.value)

    def _match(self, input_):
        try:
            template = self.engine.create_template(input_)
        except Exception:
            return False

        return True if template else False
