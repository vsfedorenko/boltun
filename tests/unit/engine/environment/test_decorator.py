import unittest

from boltun.engine.environment.extension import boltun


def fake_deco(maybe_target):
    def other(*args, **kwargs):
        pass

    return other


class MyTestCase(unittest.TestCase):

    def test_decorator_context_placement(self):
        class Extension(object):

            @boltun
            def method1(self):
                pass

            @boltun
            @fake_deco
            def method2(self):
                pass

        self.assertTrue(hasattr(Extension.method1, "__boltun_context__"))
        self.assertTrue(hasattr(Extension.method2, "__boltun_context__"))

    def test_decorator_context_placement_bad_usage(self):
        class Extension(object):

            @fake_deco
            @boltun
            def method1(self):
                pass

        self.assertTrue(not hasattr(Extension.method1, "__boltun_context__"))


if __name__ == '__main__':
    unittest.main()
