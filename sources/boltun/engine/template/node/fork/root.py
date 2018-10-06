from __future__ import absolute_import

import attr

from .__base__ import ForkNode


@attr.s
class RootNode(ForkNode):

    def __compile__(self, compiler):
        return compiler.concat(*super(RootNode, self).__compile__(compiler))


__all__ = ['RootNode']
