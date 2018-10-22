import unittest

from boltun.engine import Engine
from boltun.engine.grammar.antlr4 import Antlr4Grammar
from boltun.engine.template import Template
from boltun.engine.template.graph import ObjectGraphCompiler


class MyTestCase(unittest.TestCase):

    def test_something(self):
        grammar = Antlr4Grammar()
        compiler = ObjectGraphCompiler()
        engine = Engine(grammar, compiler)
        render_iter = engine.render(
            "Hello, I would like to buy "
            "[[> range(1, 10, 2) ]] "
            "[[> any('orange', 'fruit', 'apple') ]]"
        )

        Template.print_all(render_iter)


if __name__ == '__main__':
    unittest.main()