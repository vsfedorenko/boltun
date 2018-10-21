from abc import ABCMeta

import attr
from six import with_metaclass


@attr.s
class Extension(with_metaclass(ABCMeta, object)):

    def functions(self):
        return []

    def filters(self):
        return []
