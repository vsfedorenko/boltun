import itertools
import random
import unittest

from parameterized import parameterized

from boltun.util import recursive_callable


@recursive_callable(value_pos=1)
def _method_with_pos_reference_1(fake_value, other_value):
    """
    :type other_value: [list, dict, str]
    """
    return other_value.lower()


@recursive_callable(value_pos=1)
def _method_with_pos_reference_2(fake_value, other_value,
                                 another_fake_value=2):
    """
    :type other_value: [list, dict, str]
    """
    return other_value.lower()


@recursive_callable(value_key='other_value')
def _method_with_key_reference(fake_value, other_value):
    """
    :type other_value: [list, dict, str]
    """
    return other_value.lower()


def _randint():
    return random.randint(0, 100)


class FakeClass(object):

    @classmethod
    @recursive_callable(value_pos=2)
    def cls_method_with_pos_reference(cls, fake_value, other_value):
        """
        :type other_value: [list, dict, str]
        """
        return other_value.lower()

    @recursive_callable
    def self_method_without_any_reference(self, other_value):
        """
        :type other_value: [list, dict, str]
        """
        return other_value.lower()

    @recursive_callable(value_key='other_value')
    def self_method_with_pos_reference(self, fake_value, other_value):
        """
        :type other_value: [list, dict, str]
        """
        return other_value.lower()


_fake_class_instance = FakeClass()


class TestRecursiveCallable(unittest.TestCase):
    functions = [
        lambda x: _method_with_pos_reference_1(_randint(), x),
        lambda x: _method_with_pos_reference_1(_randint(), other_value=x),
        lambda x: _method_with_pos_reference_2(_randint(), x, _randint()),
        lambda x: _method_with_key_reference(_randint(), x),
        lambda x: _method_with_key_reference(
            fake_value=_randint(), other_value=x
        ),
        lambda x: FakeClass.cls_method_with_pos_reference(_randint(), x),
        lambda x: _fake_class_instance.cls_method_with_pos_reference(
            _randint(), x
        ),
        lambda x: _fake_class_instance.self_method_without_any_reference(x),
        lambda x: _fake_class_instance.self_method_with_pos_reference(
            _randint(), x
        ),
    ]

    @parameterized.expand(list(
        itertools.chain(
            *[
                [
                    (func, 'TEXT', 'text'),
                    (func, 'Hello WORLD', 'hello world'),
                    (func, ['Hello'], ['hello']),
                    (func, ['Hello', 'World'], ['hello', 'world']),
                    (
                            func, [[['Hello', 'World']]],
                            [[['hello', 'world']]]
                    ),
                    (
                            func, [['Hello'], ['World']],
                            [['hello'], ['world']]
                    ),
                    (func, {'key': 'VALUE'}, {'key': 'value'}),
                    (
                            func,
                            {'key': {'key2': 'ValuE'}},
                            {'key': {'key2': 'value'}}
                    ),
                    (
                            func,
                            {'key': {'key2': 'vAL'}, 'key3': 'What?'},
                            {'key': {'key2': 'val'}, 'key3': 'what?'}
                    ),
                ]
                for func in functions
            ])
    ))
    def test_text_recursion(self, func, actual, expected):
        assert func(actual) == expected


if __name__ == '__main__':
    unittest.main()
