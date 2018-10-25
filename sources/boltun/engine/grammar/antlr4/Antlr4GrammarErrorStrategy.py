from __future__ import absolute_import, division, print_function

from antlr4 import BailErrorStrategy


class Antlr4GrammarErrorStrategy(BailErrorStrategy):

    def recover(self, recognizer, e):
        raise e

    def reportError(self, recognizer, e):
        pass


__all__ = ['Antlr4GrammarErrorStrategy']
