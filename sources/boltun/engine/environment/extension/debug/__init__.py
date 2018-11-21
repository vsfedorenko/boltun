from __future__ import absolute_import, division, print_function

import attr

from boltun.engine.environment.extension import Extension


@attr.s
class DebugExtension(Extension):

    def __boltun_function_definitions__(self):
        return [

        ]

    def __boltun_filters_definitions__(self):
        return [

        ]
