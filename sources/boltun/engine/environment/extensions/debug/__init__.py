from __future__ import absolute_import, division, print_function

import attr

from boltun.engine.environment.extensions import Extension


@attr.s
class DebugExtension(Extension):

    def functions(self):
        return [

        ]

    def filters(self):
        return [

        ]
