import attr
from antlr4 import CommonTokenStream, InputStream

from .Antlr4GrammarErrorStrategy import Antlr4GrammarErrorStrategy
from .Antlr4GrammarLexer import Antlr4GrammarLexer
from .Antlr4GrammarParser import Antlr4GrammarParser
from .Antlr4GrammarVisitor import Antlr4GrammarVisitor
from ..base import Grammar, GrammarMode, GrammarParseResult


@attr.s
class Antlr4Grammar(Grammar):
    error_strategy = attr.ib(default=attr.Factory(Antlr4GrammarErrorStrategy))
    visitor = attr.ib(default=attr.Factory(Antlr4GrammarVisitor))
    listeners = attr.ib(type=list, default=attr.Factory(list))
    mode = attr.ib(type=GrammarMode, default=GrammarMode.NLP)

    def parse(self, input_str, mode=None, **kwargs):
        """

        :param str input_str: input str
        :param Antlr4GrammarMode mode: parser mode
        :param kwargs: arbitrary keyword arguments

        :rtype: .GrammarParseResult
        """
        input_stream = InputStream(input_str)
        lexer = Antlr4GrammarLexer(input_stream)
        token_stream = CommonTokenStream(lexer)

        parser = Antlr4GrammarParser(token_stream)
        parser.recognition_mode = mode if mode else self.mode
        parser.error_strategy = self.error_strategy

        for listener in self.listeners:
            parser.addParseListener(listener)

        parser.reset()

        grammar_tree = parser.document()
        node_tree = parser.node_stack.pop()

        self.visitor.visit(grammar_tree)

        return GrammarParseResult(grammar_tree, node_tree)


__all__ = ['Antlr4Grammar']
