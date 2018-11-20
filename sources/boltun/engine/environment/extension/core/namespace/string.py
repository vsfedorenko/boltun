from __future__ import absolute_import, division, print_function

from boltun.engine.environment.extension import Namespace, \
    boltun
from boltun.util import recursive
from .json import JsonNamespace


class StringNamespace(Namespace):

    def __names__(self):
        return ['str', 'string']

    def __namespaces__(self):
        return [JsonNamespace]

    @boltun(filter=True)
    @recursive
    def lower(self, value):
        return value.lower()

    @boltun(filter=True)
    @recursive
    def upper(self, value):
        return value.upper()

    @boltun(filter=True)
    @recursive
    def capitalize(self, value):
        return value.capitalize()

    @boltun(filter=True)
    @recursive
    def strip(self, value):
        return value.strip()

    @boltun(filter=True)
    @recursive
    def lstrip(self, value):
        return value.lstrip()

    @boltun(filter=True)
    @recursive
    def rstrip(self, value):
        return value.rstrip()
