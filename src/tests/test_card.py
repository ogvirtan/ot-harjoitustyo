import unittest
from entities.card import Card


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card(2)

    def test_card_exists(self):
        self.assertNotEqual(self.card, None)

    def test_ret_value_with_number(self):
        self.assertEqual(self.card.ret_value(), 2)

    def test__str__with_number(self):
        self.assertEqual(self.card.__str__(), "2")

    def test__repr__with_number(self):
        self.assertEqual(self.card.__repr__(), "2")

    def test_ret_value_with_face_card(self):
        self.card = Card(11)
        self.assertEqual(self.card.ret_value(), 10)

    def test__str__with_face_card(self):
        self.card = Card(11)
        self.assertEqual(self.card.__str__(), "J")

    def test__repr_with_face_card(self):
        self.card = Card(11)
        self.assertEqual(self.card.__repr__(), "J")

    def test_ret_value_with_ace(self):
        self.card = Card(14)
        self.assertEqual(self.card.ret_value(), 11)

    def test__str__with_ace(self):
        self.card = Card(14)
        self.assertEqual(self.card.__str__(), "A")

    def test__repr_with_ace(self):
        self.card = Card(14)
        self.assertEqual(self.card.__repr__(), "A")
