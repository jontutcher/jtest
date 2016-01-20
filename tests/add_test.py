from unittest import TestCase
from maths.add import add


class TestAdd(TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
