import unittest
from entities.player import Player
from entities.card import Card


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.test_hand = [Card(8), Card(11)]
        self.player.new_hand(self.test_hand)

    def test_player_exists(self):
        self.assertNotEqual(self.player, None)

    def test_new_hand_works(self):
        self.assertEqual(len(self.player.hand), 2)

    def test_upcard_returns_card_with_correct_face(self):
        self.assertEqual(str(self.player.upcard()), "8")

    def test_upcard_returns_card_with_correct_value(self):
        self.assertEqual(self.player.upcard().ret_value(), 8)

    def test_downcard_returns_card_with_correct_face(self):
        self.assertEqual(str(self.player.downcard()), "J")

    def test_downcard_returns_card_with_correct_value(self):
        self.assertEqual(self.player.downcard().ret_value(), 10)

    def test_get_total(self):
        self.assertEqual(self.player.get_total(), 18)

    def test_get_pair_returns_true_with_numbers(self):
        self.test_hand = [Card(8), Card(8)]
        self.player.new_hand(self.test_hand)
        self.assertTrue(self.player.get_pair())

    def test_get_pair_returns_true_with_facecards(self):
        self.test_hand = [Card(11), Card(11)]
        self.player.new_hand(self.test_hand)
        self.assertTrue(self.player.get_pair())

    def test_get_pair_returns_true_with_aces(self):
        self.test_hand = [Card(14), Card(14)]
        self.player.new_hand(self.test_hand)
        self.assertTrue(self.player.get_pair())

    def test_get_pair_returns_false_with_different_value_cards(self):
        self.assertFalse(self.player.get_pair())

    def test_get_pair_returns_false_with_larger_hands(self):
        self.test_hand = [Card(8), Card(8), Card(8)]
        self.player.new_hand(self.test_hand)
        self.assertFalse(self.player.get_pair())

    def test__str__returns_correct_output(self):
        self.test_hand = [Card(8), Card(14)]
        self.player.new_hand(self.test_hand)
        self.assertEqual(self.player.__str__(), "[8, A]")

    def test__repr__returns_correct_output(self):
        self.test_hand = [Card(8), Card(14)]
        self.player.new_hand(self.test_hand)
        self.assertEqual(self.player.__repr__(), "[8, A]")
