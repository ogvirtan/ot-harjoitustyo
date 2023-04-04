import unittest
from entities.deck import Deck

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_deck_exists(self):
        self.assertNotEqual(self.deck, None)

    def test_return_size(self):
        self.assertEqual(self.deck.size, 52)