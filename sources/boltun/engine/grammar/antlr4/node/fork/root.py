from __future__ import absolute_import, division, print_function

import attr

from ._base import ForkNode


@attr.s
class RootNode(ForkNode):

    def __compile__(self, compiler, environment):
        return compiler.concat(
            *super(RootNode, self).__compile__(compiler, environment))
