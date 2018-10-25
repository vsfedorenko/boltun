import unittest

from parameterized import parameterized

from boltun.engine.environment.extension.core import StringNamespace


class TestStringNamespace(unittest.TestCase):

    def setup_method(self, method):
        self.namespace = StringNamespace()

    @parameterized.expand([
        ('Hello', 'hello'),
        ('HELLO', 'hello'),
        ('HellO World', 'hello world'),
        ('123ABC', '123abc'),
        ('aB 123 CD', 'ab 123 cd'),

        (['Hello'], ['hello']),
        (['Hello', 'World', '!'], ['hello', 'world', '!']),
        ([['Hello'], ['World', ['!']]], [['hello'], ['world', ['!']]]),

        ({'key': 'VALUE'}, {'key': 'value'}),
        ({'key': {'key2': 'vAluE'}}, {'key': {'key2': 'value'}}),
        (
                {'key': {'key2': 'VALUE'}, 'key3': {'key4': 'VAL'}},
                {'key': {'key2': 'value'}, 'key3': {'key4': 'val'}}
        ),
    ])
    def test_lower(self, actual, expected):
        assert self.namespace.lower(actual) == expected

    @parameterized.expand([
        ('Hello', 'HELLO'),
        ('HELlO', 'HELLO'),
        ('HellO World', 'HELLO WORLD'),
        ('123ABC', '123ABC'),
        ('aB 123 CD', 'AB 123 CD'),

        (['Hello'], ['HELLO']),
        (['Hello', 'World', '!'], ['HELLO', 'WORLD', '!']),
        ([['Hello'], ['World', ['!']]], [['HELLO'], ['WORLD', ['!']]]),

        ({'key': 'value'}, {'key': 'VALUE'}),
        ({'key': {'key2': 'vAluE'}}, {'key': {'key2': 'VALUE'}}),
        (
                {'key': {'key2': 'valuE'}, 'key3': {'key4': 'vAl'}},
                {'key': {'key2': 'VALUE'}, 'key3': {'key4': 'VAL'}}
        ),
    ])
    def test_upper(self, actual, expected):
        assert self.namespace.upper(actual) == expected

    @parameterized.expand([
        ('HeLlo', 'Hello'),
        ('HELlO', 'Hello'),
        ('hellO World', 'Hello world'),
        ('123ABC', '123abc'),
        ('aB 123 CD', 'Ab 123 cd'),

        (['hello'], ['Hello']),
        (['hello', 'world', '!'], ['Hello', 'World', '!']),
        ([['hello'], ['world', ['!']]], [['Hello'], ['World', ['!']]]),

        ({'key': 'value'}, {'key': 'Value'}),
        ({'key': {'key2': 'ValuE'}}, {'key': {'key2': 'Value'}}),
        (
                {'key': {'key2': 'valuE'}, 'key3': {'key4': 'vAl'}},
                {'key': {'key2': 'Value'}, 'key3': {'key4': 'Val'}}
        ),
    ])
    def test_capitalize(self, actual, expected):
        assert self.namespace.capitalize(actual) == expected

    @parameterized.expand([
        ('   Hello  ', 'Hello'),
        ('HELlO   ', 'HELlO'),
        ('    hellO World   ', 'hellO World'),
        ('   123ABC   ', '123ABC'),
        ('aB 123 CD     ', 'aB 123 CD'),

        (['hello'], ['hello']),
        (['hello', '    world', '!'], ['hello', 'world', '!']),
        ([['hello    '], ['world', ['  !']]], [['hello'], ['world', ['!']]]),

        ({'key': 'value     '}, {'key': 'value'}),
        ({'key': {'key2': '    ValuE   '}}, {'key': {'key2': 'ValuE'}}),
        (
                {'key': {'key2': '      valuE'}, 'key3': {'key4': '    vAl'}},
                {'key': {'key2': 'valuE'}, 'key3': {'key4': 'vAl'}}
        ),
    ])
    def test_strip(self, actual, expected):
        assert self.namespace.strip(actual) == expected

    @parameterized.expand([
        ('   Hello  ', 'Hello  '),
        ('HELlO   ', 'HELlO   '),
        ('    hellO World   ', 'hellO World   '),
        ('   123ABC   ', '123ABC   '),
        ('aB 123 CD     ', 'aB 123 CD     '),

        (['hello'], ['hello']),
        (['hello', '    world', '!'], ['hello', 'world', '!']),
        (
                [['hello    '], ['world', ['  !']]],
                [['hello    '], ['world', ['!']]]
        ),

        ({'key': 'value     '}, {'key': 'value     '}),
        ({'key': {'key2': '    ValuE   '}}, {'key': {'key2': 'ValuE   '}}),
        (
                {'key': {'key2': '      valuE'}, 'key3': {'key4': '    vAl'}},
                {'key': {'key2': 'valuE'}, 'key3': {'key4': 'vAl'}}
        ),
    ])
    def test_lstrip(self, actual, expected):
        assert self.namespace.lstrip(actual) == expected

    @parameterized.expand([
        ('   Hello  ', '   Hello'),
        ('HELlO   ', 'HELlO'),
        ('    hellO World', '    hellO World'),
        ('   123ABC   ', '   123ABC'),
        ('aB 123 CD     ', 'aB 123 CD'),

        (['hello    '], ['hello']),
        (['hello', '    world', '!'], ['hello', '    world', '!']),
        (
                [['hello    '], ['  world', ['  !']]],
                [['hello'], ['  world', ['  !']]]
        ),

        ({'key': 'value     '}, {'key': 'value'}),
        ({'key': {'key2': '    ValuE   '}}, {'key': {'key2': '    ValuE'}}),
        (
                {'key': {'key2': '      valuE'}, 'key3': {'key4': '    vAl'}},
                {'key': {'key2': '      valuE'}, 'key3': {'key4': '    vAl'}}
        ),
    ])
    def test_rstrip(self, actual, expected):
        assert self.namespace.rstrip(actual) == expected


if __name__ == '__main__':
    unittest.main()
