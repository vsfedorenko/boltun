from __future__ import absolute_import, division, print_function

import attr
from enum import IntEnum


@attr.s
class Antlr4GrammarMode(IntEnum):
    DATA = 1
    CALL = 2
