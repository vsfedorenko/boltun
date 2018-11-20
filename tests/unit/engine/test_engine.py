import collections
import unittest

from parameterized import parameterized

from boltun.engine import Engine
from boltun.engine.template import Sample


class TestEngine(unittest.TestCase):

    @parameterized.expand([
        # ("Hello", [Sample("Hello")]),
        # ("Hello, World !", [Sample("Hello, World !")]),
        ("Hello, {{ World || Me }} !", [
            Sample("Hello, World !"),
            Sample("Hello, Me !")
        ]),
        # ("Hello, {{ Mike || John || Adella }}, how are you ?", [
        #     Sample("Hello, Mike !"),
        #     Sample("Hello, John !"),
        #     Sample("Hello, Adella !")
        # ]),
        # ("Hello, [[ what the weather | str.upper? ]] outside ??", [
        #     Sample("Hello, what the weather outside ??"),
        #     Sample("Hello, WHAT THE WEATHER outside ??")
        # ])
    ])
    def test_engine_default(self, input_, expected_samples):
        engine = Engine()
        extensions = engine.default_environment.extensions.get()

        samples = engine.render(input_)
        assert samples is not None
        assert isinstance(samples, collections.Iterable)

        samples_list = list(samples)
        samples_list_len = len(samples_list)
        assert samples_list_len != 0
        assert samples_list_len == len(expected_samples)
        # for actual, expected in zip(samples_list, expected_samples):
        #     assert actual == expected


if __name__ == '__main__':
    unittest.main()
