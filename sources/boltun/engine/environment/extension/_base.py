from __future__ import absolute_import, division, print_function

from abc import ABCMeta, abstractmethod as abstract_method

import attr
from six import with_metaclass


@attr.s
class Extension(with_metaclass(ABCMeta, object)):

    @abstract_method
    def __boltun_name__(self):
        raise NotImplementedError()

    def __boltun_function_definitions__(self):
        return []

    def __boltun_filters_definitions__(self):
        return []
