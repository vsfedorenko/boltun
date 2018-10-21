import attr

from boltun.engine.environment import Environment
from boltun.engine.environment.extensions.core import CoreExtension
from boltun.engine.grammar import Grammar
from boltun.engine.template import Compiler


@attr.s
class Engine(object):
    grammar = attr.ib(type=Grammar)
    compiler = attr.ib(type=Compiler)

    _environment = attr.ib(type=Environment,
                           default=attr.Factory(Environment, takes_self=True),
                           init=False)

    def __attrs_post_init__(self):
        self._environment.add_extension(CoreExtension())

    def create_template(self, input_str):
        grammar_parse_result = self.grammar.parse(input_str)

        node_tree = grammar_parse_result.node_tree

        template = \
            self.compiler.__template__(grammar_node_tree=node_tree,
                                       environment=self._environment)
        return template

    def render(self, input_str):
        template = self.create_template(input_str)
        return template.render()
