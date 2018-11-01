from __future__ import absolute_import, division, print_function

from boltun.engine.environment.extension import Namespace, boltun
from boltun.util import recursive


class StringNamespace(Namespace):

    @classmethod
    def __names__(cls):
        return ['str', 'string']

    @boltun
    @recursive
    def lower(self, value):
        return value.lower()

    @boltun
    @recursive
    def upper(self, value):
        return value.upper()

    @boltun
    @recursive
    def capitalize(self, value):
        return value.capitalize()

    @boltun
    @recursive
    def strip(self, value):
        return value.strip()

    @boltun
    @recursive
    def lstrip(self, value):
        return value.lstrip()

    @boltun
    @recursive
    def rstrip(self, value):
        return value.rstrip()
