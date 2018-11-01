from __future__ import absolute_import, division, print_function

import sys
from abc import ABCMeta, abstractmethod as abstract_method

import attr
import six
from six import with_metaclass


@attr.s
class Sample(object):
    content = attr.ib(type=str, converter=str)
    id = attr.ib(default=0)
    next_sample = attr.ib(type='self', default=None)

    def composite_id(self):
        composite_id = [self.id]
        if self.next_sample:
            composite_id.extend(self.next_sample.composite_id())
        return composite_id

    @next_sample.validator
    def __validate_child_sample(self, attrib, value):
        if value is not None and not issubclass(type(value), Sample):
            raise TypeError("Only Sample and it sub-classes can be a child")

    def __str__(self):
        child_content = str(self.next_sample) if self.next_sample else ''
        return self.content + child_content


@attr.s
class Template(with_metaclass(ABCMeta, object)):

    @abstract_method
    def render(self, shuffle=False):
        raise NotImplementedError()

    @staticmethod
    def print_all(result, print_func=None, handle=sys.stdout):
        if not print_func:
            def py_print(value, handle):
                return six.print_(value, file=handle)

            print_func = py_print

        try:
            while True:
                print_func(next(result), handle=handle)
        except StopIteration:
            pass


@attr.s
class Compiler(with_metaclass(ABCMeta, object)):

    @abstract_method
    def __process__(self, grammar_node_tree, environment):
        raise NotImplementedError()

    @abstract_method
    def __template__(self, grammar_node_tree, environment):
        raise NotImplementedError()

    @abstract_method
    def function(self, environment, function_context):
        raise NotImplementedError()

    @abstract_method
    def filter(self, environment, filter_context):
        raise NotImplementedError()

    @abstract_method
    def text(self, environment, value):
        raise NotImplementedError()

    @abstract_method
    def concat(self, part, *other_parts):
        raise NotImplementedError()

    @abstract_method
    def any(self, choice, *other_choices):
        raise NotImplementedError()

    def nothing(self, environment):
        return None
