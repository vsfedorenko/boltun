from abc import ABCMeta, abstractmethod as abstract_method

import attr
from six import with_metaclass


@attr.s
class Template(with_metaclass(ABCMeta, object)):

    @abstract_method
    def render(self, input_):
        raise NotImplementedError()


class Compiler(with_metaclass(ABCMeta, object)):

    @abstract_method
    def __process__(self, input_):
        raise NotImplementedError()
