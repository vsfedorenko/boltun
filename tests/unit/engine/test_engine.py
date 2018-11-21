import collections
import unittest

from parameterized import parameterized

from boltun.engine import Engine


class TestEngine(unittest.TestCase):

    @parameterized.expand([
        ("Hello", ["Hello"]),
        ("Hello, World !", ["Hello, World !"]),
        ("Hello, {{ World || Me }} !", [
            "Hello, World !",
            "Hello, Me !"
        ]),
        ("Hello, {{ Mike || John || Adella }}, how are you ?", [
            "Hello, Mike, how are you ?",
            "Hello, John, how are you ?",
            "Hello, Adella, how are you ?"
        ]),
        ("Hello, [[ 'what the weather' | upper? ]] outside ??", [
            "Hello, what the weather outside ??",
            "Hello, WHAT THE WEATHER outside ??"
        ])
    ])
    def test_engine_default(self, input_, expected_strings):
        engine = Engine()

        samples = engine.render(input_)
        assert samples is not None
        assert isinstance(samples, collections.Iterable)

        samples_list = list(samples)
        samples_list_len = len(samples_list)
        assert samples_list_len != 0
        assert samples_list_len == len(expected_strings)
        for actual, expected in zip(samples_list, expected_strings):
            assert str(actual) == expected


if __name__ == '__main__':
    unittest.main()
