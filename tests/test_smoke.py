import os
import sys

# Ensure project root is on sys.path so we can import 'hsl3' and 'src'
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
if ROOT_DIR+'\\src' not in sys.path:
    sys.path.insert(0, ROOT_DIR+'\\src')


import unittest
from src.hsl3.hsl3_generator import generator


class TestSmoke(unittest.TestCase):
    def test_version_is_string(self):
        self.assertIsInstance(generator.__version__, str)
        self.assertTrue(generator.__version__)

    def test_main_callable(self):
        self.assertTrue(callable(generator.main))


if __name__ == "__main__":
    unittest.main()
