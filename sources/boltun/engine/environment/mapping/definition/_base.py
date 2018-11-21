from __future__ import absolute_import, division, print_function

import attr


@attr.s
class FunctionDef(object):
    name = attr.ib(type=str)
    callable = attr.ib(type=callable)


@attr.s
class FilterDef(object):
    name = attr.ib(type=str)
    callable = attr.ib(type=callable)
