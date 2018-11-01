import attr

from ._base import Namespace


@attr.s
class DefaultNamespace(Namespace):

    @classmethod
    def __names__(cls):
        return [None, '__default__']
