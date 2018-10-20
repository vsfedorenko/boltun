import attr

from boltun.engine.ext import ExtensionSet
from boltun.engine.ext.core import CoreExtension
from boltun.engine.grammar import Grammar
from boltun.engine.grammar.antlr4 import Antlr4Grammar
from boltun.engine.template import Compiler, Template


@attr.s
class Engine(object):
    grammar = attr.ib(type=Grammar)
    compiler = attr.ib(type=Compiler)
    extensions = attr.ib(type=ExtensionSet,
                         default=attr.Factory(ExtensionSet, takes_self=True))
    cache = attr.ib(default=None)

    def __attrs_post_init__(self):
        self.extensions.append(CoreExtension(), force_replace=True)

    def create_template(self, input_str):
        grammar_parse_result = self.grammar.parse(input_str)

        node_tree = grammar_parse_result.node_tree
        self.compiler.process(node_tree)

        return Template()

    def get_extensions(self):
        return set(self.extensions)
