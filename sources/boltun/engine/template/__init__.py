from __future__ import absolute_import, division, print_function

import sys
from abc import ABCMeta, abstractmethod as abstract_method

import attr
import six
from six import with_metaclass


@attr.s
class Template(with_metaclass(ABCMeta, object)):

    @abstract_method
    def render(self, shuffle=False):
        raise NotImplementedError()

    @staticmethod
    def print_all(result, print_func=None, handle=sys.stdout):
        if not print_func:
            def py_print(v, handle):
                return six.print_(v, file=handle)

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
