import unittest

import generator


class TestSmoke(unittest.TestCase):
    def test_version_is_string(self):
        self.assertIsInstance(generator.__version__, str)
        self.assertTrue(generator.__version__)

    def test_main_callable(self):
        self.assertTrue(callable(generator.main))


if __name__ == "__main__":
    unittest.main()
