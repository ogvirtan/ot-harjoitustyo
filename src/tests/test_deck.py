import unittest
from entities.deck import Deck


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_deck_exists(self):
        self.assertNotEqual(self.deck, None)

    def test_deck_size_vanilla(self):
        self.assertEqual(self.deck._deck_size(), 52)

    def test_deck_size_multiple(self):
        self.deck.add_deck()
        self.assertEqual(self.deck._deck_size(), 104)

    def test_check_for_deck_size_adds_new_deck_when_empty(self):
        self.deck.deck = []
        self.deck._check_for_deck_size()
        self.assertEqual(self.deck._deck_size(), 52)

    def test_deal_new_hand_reduces_number_of_cards_in_deck(self):
        self.deck.deal_new_hand()
        self.assertEqual(self.deck._deck_size(), 50)

    def test_deal_new_hand_works_with_empty_deck(self):
        self.deck.deck = []
        self.deck.deal_new_hand()
        self.assertEqual(self.deck._deck_size(), 50)

    # def test_shuffle(self):
