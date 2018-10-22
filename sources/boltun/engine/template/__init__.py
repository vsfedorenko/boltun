import itertools
import sys
from abc import ABCMeta, abstractmethod as abstract_method

import attr
import six
from six import with_metaclass


@attr.s
class Template(with_metaclass(ABCMeta, object)):

    @abstract_method
    def render(self):
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
    def entity(self, environment, type_, name, ref_names):
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

    def nothing(self, environment):
        return None

    def concat(self, parts, *other_parts):
        if not isinstance(parts, (list,)):
            parts = [parts]

        if other_parts:
            parts.extend(other_parts)

        if len(parts) == 1:
            return parts[0]

        if all([isinstance(x, (list,)) for x in parts]):
            return list(itertools.chain(*parts))

        return parts

    def any(self, choices, *other_choices):
        if not isinstance(choices, (list,)):
            choices = [choices]

        if other_choices:
            choices.extend(other_choices)

        if len(choices) < 2:
            raise ValueError("Choices count must be greater or equal 2")

        return list(choices)
