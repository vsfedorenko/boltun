from __future__ import absolute_import, division, print_function

import ast
import json
import os

import attr
import six
import yaml

from boltun.engine.environment.extension import Extension
from boltun.engine.environment.mapping import FilterDef, FunctionDef
from boltun.util import recursive


@attr.s
class CoreExtension(Extension):

    def __boltun_name__(self):
        return 'core'

    def __boltun_function_definitions__(self):
        return [
            FunctionDef('any', self.any),
            FunctionDef('echo', self.echo),
            FunctionDef('env', self.env),
            FunctionDef('range', self.range),
            FunctionDef('lower', self.lower),
            FunctionDef('upper', self.upper),
            FunctionDef('capitalize', self.capitalize),
            FunctionDef('strip', self.strip),
            FunctionDef('lstrip', self.lstrip),
            FunctionDef('rstrip', self.rstrip),
            FunctionDef('split', self.split),
            FunctionDef('repeat', self.repeat),
            FunctionDef('yaml_load', self.yaml_load),
            FunctionDef('yaml_dump', self.yaml_dump),
            FunctionDef('json_load', self.json_load),
            FunctionDef('json_dump', self.json_dump),
            FunctionDef('list', self.list_function),
            FunctionDef('dict', self.dict),
        ]

    def __boltun_filters_definitions__(self):
        return [
            FilterDef('lower', self.lower),
            FilterDef('upper', self.upper),
            FilterDef('capitalize', self.capitalize),
            FilterDef('strip', self.strip),
            FilterDef('lstrip', self.lstrip),
            FilterDef('rstrip', self.rstrip),
            FilterDef('split', self.split),
            FilterDef('repeat', self.repeat),
            FilterDef('list', self.list_filter),
            FilterDef('dict', self.dict),
        ]

    def any(self, *args, **kwargs):
        return list(args)

    def echo(self, value, *args, **kwargs):
        return value

    def env(self, value, *args, **kwargs):
        return os.environ.get(value)

    def range(self, x, y, step=1, **kwargs):
        return list(range(x, y, step))

    @recursive
    def lower(self, value):
        return value.lower()

    @recursive
    def upper(self, value):
        return value.upper()

    @recursive
    def capitalize(self, value):
        return value.capitalize()

    @recursive
    def strip(self, value):
        return value.strip()

    @recursive
    def lstrip(self, value):
        return value.lstrip()

    @recursive
    def rstrip(self, value):
        return value.rstrip()

    @recursive
    def split(self, value, sep):
        return value.split(sep)

    @recursive
    def repeat(self, value, count):
        if isinstance(count, list):
            return [
                self.repeat(value, current_count)
                for current_count in count
            ]

        return "".join([value for _ in range(0, count)])

    @recursive
    def yaml_load(self, value):
        return yaml.load(value)

    def yaml_dump(self, value, **kwargs):
        return yaml.dump(value, **kwargs)

    @recursive
    def json_load(self, value, *args, **kwargs):
        return json.loads(value, *args, **kwargs)

    def json_dump(self, value, *args, **kwargs):
        return json.dumps(value, *args, **kwargs)

    def list_function(self, *args):
        return list(args)

    def list_filter(self, value):
        return ast.literal_eval(value)

    def dict(self, **kwargs):
        return {k: v for k, v in six.iteritems(kwargs)}
