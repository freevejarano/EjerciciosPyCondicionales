from unittest import TestCase

from Problema2 import par


class Test(TestCase):
    def test_par(self):
        self.assertEqual(True,par(2))
        self.assertEqual(False,par(3))
