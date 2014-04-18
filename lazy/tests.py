import unittest

from itertools import count
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
        self.assertFalse(L.realized)
        with self.assertRaises(IndexError):
            L[8]
        self.assertEqual(L[0], 2)
        self.assertTrue(L.realized)

    def test_repr(self):
        i = xrange(1)
        self.assertEqual(repr(lazy(i)), u'lazy(%r)' % i)

    def test_first(self):
        self.assertEqual(lazy(count(10)).first(), 10)

    def test_rest(self):
        self.assertEqual(lazy(count(10)).rest().first(), 11)

    def test_rest_skip_past_end(self):
        i = lazy(xrange(10))
        with self.assertRaises(IndexError):
            for _ in xrange(11):
                i = i.rest()
            i.first()
