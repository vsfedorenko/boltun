from __future__ import absolute_import, division, print_function

import attr


@attr.s
class NamespaceHolder(object):
    _environment = attr.ib()
    _items = attr.ib(type=dict, factory=dict, init=False)
