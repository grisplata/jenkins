import unittest

class TestPass(unittest.TestCase):
    def test_success(self):
        expected = 42
        actual = 42
        self.assertEqual(expected, actual)
