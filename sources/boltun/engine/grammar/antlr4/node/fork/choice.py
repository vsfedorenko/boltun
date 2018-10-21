from __future__ import absolute_import

import attr

from .base import ForkNode


@attr.s
class ChoiceNode(ForkNode):

    def __compile__(self, compiler, environment):
        return compiler.any(
            super(ChoiceNode, self).__compile__(compiler, environment))


__all__ = ['ChoiceNode']
