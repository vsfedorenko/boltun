import unittest

from boltun.engine import Engine
from boltun.engine.grammar.antlr4 import Antlr4Grammar
from boltun.engine.template.graph import ObjectGraphCompiler


class MyTestCase(unittest.TestCase):

    def test_something(self):
        grammar = Antlr4Grammar()
        compiler = ObjectGraphCompiler()
        engine = Engine(grammar, compiler)
        engine.render("Hello, [[> env('PATH') | upper | lower | upper ]] "
                      "[[> range(0, 10) | to_str | split(',') ]]"
                      "[[> any('test', 'fest') | json.dump ]]")


if __name__ == '__main__':
    unittest.main()
