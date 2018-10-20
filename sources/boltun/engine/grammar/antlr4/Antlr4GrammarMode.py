import attr
from enum import IntEnum


@attr.s
class Antlr4GrammarMode(IntEnum):
    DATA = 1
    CALL = 2
    NLP = 3
