from unittest import TestCase

from Problema11 import fibonacci


class Test(TestCase):
    def test_fibonacci(self):
        self.assertEqual([0,1,1,2,3,5],fibonacci(6))
