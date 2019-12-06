#import the unit test package and functions we want to test out
import unittest
from sqrt import newton_sqrt1, newton_sqrt2, lazy_sqrt, builtin_sqrt

class SqrtTests(unittest.TestCase):
    """Obligatory docstring, test square root functions!"""
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)

    def test_sqrt2(self):
        self.assertAlmostEqual(lazy_sqrt(2)**2,2)

    def builtin_sqrt(self):
        self.assertIs(lazy_sqrt(0),0)

class SquaringTests(unittest.TestCase):
    def test_thing(self):
        pass

if __name__ == '__main__':
    unittest.main()
