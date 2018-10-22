from __future__ import absolute_import

import attr


@attr.s
class LeafNodeFactory(object):

    def create_call_node(self):
        pass

    def create_comment_node(self):
        pass

    def create_data_node(self):
        pass


__all__ = ['LeafNodeFactory']
