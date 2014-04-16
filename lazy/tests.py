import unittest

from . import lazy


class TestLazy(unittest.TestCase):

    def test_getitem(self):
        L = lazy(xrange(2, 10))
        self.assertFalse(L.realized)
        self.assertEqual(L[0], 2)
        self.assertFalse(L.realized)
        self.assertEqual(L[5], 7)
        self.assertFalse(L.realized)
        self.assertEqual(L[7], 9)
        self.assertTrue(L.realized)
        with self.assertRaises(IndexError):
            L[8]
        self.assertEqual(L[0], 2)
        self.assertTrue(L.realized)
