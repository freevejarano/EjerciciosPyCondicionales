from unittest import TestCase

from Problema3 import firstFinal


class Test(TestCase):
    def test_first_final(self):
        self.assertEqual(['h','a'],firstFinal('hola'))
        self.assertEqual(['a','a'],firstFinal('arquitectura'))

