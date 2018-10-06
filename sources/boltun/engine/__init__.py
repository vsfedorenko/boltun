import attr
import six

from boltun.engine.grammar import Grammar
from boltun.engine.template import Template
from boltun.engine.template.compiler import Compiler


@attr.s
class Engine(object):
    grammar = attr.ib(type=Grammar)
    cache = attr.ib(default=None)
    charset = attr.ib(type=six.string_types, default='utf-8')
    debug = attr.ib(type=bool, default=False, init=False)
    compiler = attr.ib(default=attr.Factory(Compiler))

    def __attrs_post_init__(self):
        pass

    def create_template(self, input_str):
        grammar_parse_result = self.grammar.parse(input_str)

        node_tree = grammar_parse_result.node_tree
        self.compiler.process(node_tree)

        return Template()
