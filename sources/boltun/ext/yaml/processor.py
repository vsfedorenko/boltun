import attr
from antlr4 import InputStream

from boltun.engine import Engine
from boltun.engine.grammar import RecognitionDisabledException


@attr.s
class YamlProcessor(object):
    engine = attr.ib(default=attr.Factory(Engine))

    def match(self, input_):
        try:
            nodes = self.engine.process(input_stream=InputStream(input_))
        except RecognitionDisabledException:
            return False

        return True if nodes.children else False

    def __call__(self, loader, node, **kwargs):
        engine_result = self.engine.process(InputStream(node.value))
        return str(''.join(engine_result[0]))
