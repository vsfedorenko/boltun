import unittest

from mock import Mock

from boltun.engine.environment import Environment
from boltun.engine.environment.extension.core import EchoFunction


class TestEchoFunction(unittest.TestCase):

    def setup_method(self, method):
        environment = Mock(spec=Environment)
        self.function = EchoFunction(environment)

    def test_echo_function(self):
        assert self.function.__execute__('Hello') == 'Hello'
