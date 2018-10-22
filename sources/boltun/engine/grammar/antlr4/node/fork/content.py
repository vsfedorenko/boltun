from __future__ import absolute_import

import attr

from .base import ForkNode


@attr.s
class ContentNode(ForkNode):

    def __compile__(self, compiler, environment):
        compiled_content = \
            super(ContentNode, self).__compile__(compiler, environment)

        if len(compiled_content) == 1:
            return compiled_content[0]

        return compiler.concat(*compiled_content)
