from __future__ import absolute_import

from abc import ABCMeta, abstractmethod as abstract_method

import attr
from six import with_metaclass

from .exceptions import RecognitionDisabledException
from .nodes import Node


@attr.s
class Result(object):
    """

    """

    node_tree = attr.ib(type=Node)


@attr.s
class Grammar(with_metaclass(ABCMeta, object)):
    """

    """

    @abstract_method
    def parse(self, input_):
        """
        :param str input_: input str

        :rtype: Result
        """
        raise NotImplementedError()