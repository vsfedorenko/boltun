from __future__ import absolute_import, division, print_function

import attr

from boltun.engine.environment.extension import Extension


@attr.s
class DebugExtension(Extension):

    def __functions__(self):
        return [

        ]

    def __filters__(self):
        return [

        ]
