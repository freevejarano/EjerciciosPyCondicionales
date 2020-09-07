from unittest import TestCase

from Problema6 import palindroma


class Test(TestCase):
    def test_palindroma(self):
        self.assertEqual(True,palindroma("Ana"))
        self.assertEqual(False,palindroma("Casa"))

