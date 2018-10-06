from __future__ import absolute_import

import itertools

import attr
import six

from ._base import Call, Const, Entity


@attr.s
class Compiler(object):
    intents = attr.ib(type=list, default=attr.Factory(list))
    aliases = attr.ib(type=list, default=attr.Factory(list))
    slots = attr.ib(type=list, default=attr.Factory(list))
    functions = attr.ib(type=dict, default=attr.Factory(dict))
    filters = attr.ib(type=dict, default=attr.Factory(dict))

    def process(self, node):
        return node.__compile__(self)

    @staticmethod
    def entity(type_, name, ref_names):
        return Entity(type_, name, ref_names)

    @staticmethod
    def concat(*parts):
        if isinstance(parts, (list,)) and len(parts) == 1:
            return parts[0]

        return list(itertools.chain(*parts))

    @staticmethod
    def function(name, method, args, kwargs):
        args = Compiler._args(args)
        kwargs = Compiler._kwargs(kwargs)
        return Call(name, method, args, kwargs)

    @staticmethod
    def filter(name, value, args, kwargs):
        args_w_value = [value]
        args_w_value.extend(Compiler._args(args))
        return Call(name, args_w_value, kwargs)

    @staticmethod
    def text(value):
        return Const(value)

    @staticmethod
    def any(*choices):
        return list(choices)

    @staticmethod
    def nothing():
        return None

    @staticmethod
    def _args(args):
        args = [Const(arg) for arg in args]
        return args

    @staticmethod
    def _kwargs(kwargs):
        kwargs = {k: Const(v) for k, v in six.iteritems(kwargs)}
        return kwargs
