from __future__ import absolute_import, division, print_function

from boltun.engine.environment.extension import Namespace, boltun_filter, \
    boltun_function
from boltun.util import recursive_callable


class StringNamespace(Namespace):

    @classmethod
    def __names__(cls):
        return ['str', 'string']

    @boltun_function()
    @boltun_filter()
    @recursive_callable()
    def lower(self, value):
        return value.lower()

    @boltun_function()
    @boltun_filter()
    @recursive_callable()
    def upper(self, value):
        return value.upper()

    @boltun_function()
    @boltun_filter()
    @recursive_callable()
    def capitalize(self, value):
        return value.capitalize()

    @boltun_function()
    @boltun_filter()
    @recursive_callable()
    def strip(self, value):
        return value.strip()

    @boltun_function()
    @boltun_filter()
    @recursive_callable()
    def lstrip(self, value):
        return value.lstrip()

    @boltun_function()
    @boltun_filter()
    @recursive_callable()
    def rstrip(self, value):
        return value.rstrip()
