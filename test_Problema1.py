from unittest import TestCase

from Problema1 import edad


class Test(TestCase):
    def test_edad(self):
        self.assertEqual(70,edad(20,2020))
