from __future__ import absolute_import

import attr

from .__base__ import ForkNode


@attr.s
class ChoiceNode(ForkNode):

    def __compile__(self, compiler):
        return compiler.any(super(ChoiceNode, self).__compile__(compiler))


__all__ = ['ChoiceNode']
