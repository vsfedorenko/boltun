from __future__ import absolute_import, division, print_function

from abc import ABCMeta, abstractmethod as abstract_method

import attr
from six import with_metaclass


@attr.s
class Extension(with_metaclass(ABCMeta, object)):

    def __namespaces__(self):
        return []

    def __functions__(self):
        return []

    def __filters__(self):
        return []


class Namespace(Extension):

    @classmethod
    @abstract_method
    def __names__(cls):
        raise NotImplementedError()
