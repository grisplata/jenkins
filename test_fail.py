import unittest

class TestFail(unittest.TestCase):
    def test_failure(self):
        expected = 42
        actual = 314
        self.assertEqual(expected, actual)
