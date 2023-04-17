import unittest
from services.tool import Tool
from entities.card import Card


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.tool = Tool()

    def test_tool_exists(self):
        self.assertNotEqual(self.tool, None)

    def test_tool_new_hand_deals_two_for_player(self):
        self.tool.tool_new_hand()
        self.assertTrue(self.tool.player.current_hand())

    def test_tool_new_hand_deals_two_for_house(self):
        self.tool.tool_new_hand()
        self.assertTrue(self.tool.house.current_hand())

    def test_show_hands_shows_correct_upcard_with_number(self):
        facecard_hand = [Card(8), Card(11)]
        house_hand_with_upcard_ace = [Card(14), Card(2)]
        self.tool.house.new_hand(house_hand_with_upcard_ace)
        self.tool.player.new_hand(facecard_hand)
        self.assertEqual(self.tool.show_hands(),
                         f"\nHouse is showing A\n\nyou have [8, J]\n")

    def test_check_for_blackjack_returns_true_with_21(self):
        blackjack = [Card(14), Card(11)]
        self.tool.player.new_hand(blackjack)
        self.assertTrue(self.tool.check_for_blackjack())

    def test_check_for_blackjack_returns_false_with_not_21(self):
        not_blackjack = [Card(11), Card(11)]
        self.tool.player.new_hand(not_blackjack)
        self.assertFalse(self.tool.check_for_blackjack())

    def test_tracking_adds_wins_with_identical_inputs(self):
        self.tool.tracking("s", "s")
        self.assertEqual(self.tool.return_stats()["W"], 1)

    def test_tracking_adds_losses_with_differing_inputs(self):
        self.tool.tracking("s", "h")
        self.assertEqual(self.tool.return_stats()["L"], 1)

    def test_tracking_does_not_add_losses_with_identical_inputs(self):
        self.tool.tracking("s", "s")
        self.assertEqual(self.tool.return_stats()["L"], 0)

    def test_tracking_does_not_add_wins_with_differing_inputs(self):
        self.tool.tracking("s", "h")
        self.assertEqual(self.tool.return_stats()["W"], 0)

    def test_reset_inputs_resets_wins(self):
        self.tool.tracking_dict = {"W": 5, "L": 5}
        self.tool.reset_stats()
        self.assertEqual(self.tool.return_stats()["W"], 0)

    def test_reset_inputs_resets_losses(self):
        self.tool.tracking_dict = {"W": 5, "L": 5}
        self.tool.reset_stats()
        self.assertEqual(self.tool.return_stats()["L"], 0)

    # testing split outcomes

    # double aces, single outcome
    def test_split_pairs_returns_correct_output_with_double_A(self):
        ace_hand = [Card(14), Card(14)]
        self.tool.tool_new_hand()
        self.tool.player.new_hand(ace_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    # double facecards, single outcome
    def test_split_pairs_returns_correct_output_with_double_facecard(self):
        facecard_hand = [Card(11), Card(12)]
        self.tool.tool_new_hand()
        self.tool.player.new_hand(facecard_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    # split outcomes with double nines
    def test_split_pairs_returns_correct_output_with_double_9_house_upcard_2(self):
        nine_hand = [Card(9), Card(9)]
        two_hand = [Card(2), Card(2)]
        self.tool.player.new_hand(nine_hand)
        self.tool.house.new_hand(two_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_9_house_upcard_3(self):
        nine_hand = [Card(9), Card(9)]
        three_hand = [Card(3), Card(3)]
        self.tool.player.new_hand(nine_hand)
        self.tool.house.new_hand(three_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_9_house_upcard_4(self):
        nine_hand = [Card(9), Card(9)]
        four_hand = [Card(4), Card(4)]
        self.tool.player.new_hand(nine_hand)
        self.tool.house.new_hand(four_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_9_house_upcard_5(self):
        nine_hand = [Card(9), Card(9)]
        five_hand = [Card(5), Card(5)]
        self.tool.player.new_hand(nine_hand)
        self.tool.house.new_hand(five_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_9_house_upcard_6(self):
        nine_hand = [Card(9), Card(9)]
        six_hand = [Card(6), Card(6)]
        self.tool.player.new_hand(nine_hand)
        self.tool.house.new_hand(six_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_9_house_upcard_7(self):
        nine_hand = [Card(9), Card(9)]
        seven_hand = [Card(7), Card(7)]
        self.tool.player.new_hand(nine_hand)
        self.tool.house.new_hand(seven_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_9_house_upcard_8(self):
        nine_hand = [Card(9), Card(9)]
        eight_hand = [Card(8), Card(8)]
        self.tool.player.new_hand(nine_hand)
        self.tool.house.new_hand(eight_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_9_house_upcard_9(self):
        nine_hand = [Card(9), Card(9)]
        self.tool.player.new_hand(nine_hand)
        self.tool.house.new_hand(nine_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_9_house_upcard_facecard(self):
        nine_hand = [Card(9), Card(9)]
        jack_hand = [Card(11), Card(11)]
        self.tool.player.new_hand(nine_hand)
        self.tool.house.new_hand(jack_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_9_house_upcard_ace(self):
        nine_hand = [Card(9), Card(9)]
        ace_hand = [Card(14), Card(14)]
        self.tool.player.new_hand(nine_hand)
        self.tool.house.new_hand(ace_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    # double eights, single outcome
    def test_split_pairs_returns_correct_output_with_double_8(self):
        eight_hand = [Card(8), Card(8)]
        self.tool.tool_new_hand()
        self.tool.player.new_hand(eight_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    # split outcomes with double sevens
    def test_split_pairs_returns_correct_output_with_double_7_house_upcard_2(self):
        seven_hand = [Card(7), Card(7)]
        two_hand = [Card(2), Card(2)]
        self.tool.player.new_hand(seven_hand)
        self.tool.house.new_hand(two_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_7_house_upcard_3(self):
        seven_hand = [Card(7), Card(7)]
        three_hand = [Card(3), Card(3)]
        self.tool.player.new_hand(seven_hand)
        self.tool.house.new_hand(three_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_7_house_upcard_4(self):
        seven_hand = [Card(7), Card(7)]
        four_hand = [Card(4), Card(4)]
        self.tool.player.new_hand(seven_hand)
        self.tool.house.new_hand(four_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_7_house_upcard_5(self):
        seven_hand = [Card(7), Card(7)]
        five_hand = [Card(5), Card(5)]
        self.tool.player.new_hand(seven_hand)
        self.tool.house.new_hand(five_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_7_house_upcard_6(self):
        seven_hand = [Card(7), Card(7)]
        six_hand = [Card(6), Card(6)]
        self.tool.player.new_hand(seven_hand)
        self.tool.house.new_hand(six_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_7_house_upcard_7(self):
        seven_hand = [Card(7), Card(7)]
        self.tool.player.new_hand(seven_hand)
        self.tool.house.new_hand(seven_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_7_house_upcard_8(self):
        seven_hand = [Card(7), Card(7)]
        eight_hand = [Card(8), Card(8)]
        self.tool.player.new_hand(seven_hand)
        self.tool.house.new_hand(eight_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_7_house_upcard_9(self):
        seven_hand = [Card(7), Card(7)]
        nine_hand = [Card(9), Card(9)]
        self.tool.player.new_hand(seven_hand)
        self.tool.house.new_hand(nine_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_7_house_upcard_facecard(self):
        seven_hand = [Card(7), Card(7)]
        jack_hand = [Card(11), Card(11)]
        self.tool.player.new_hand(seven_hand)
        self.tool.house.new_hand(jack_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_7_house_upcard_ace(self):
        seven_hand = [Card(7), Card(7)]
        ace_hand = [Card(14), Card(14)]
        self.tool.player.new_hand(seven_hand)
        self.tool.house.new_hand(ace_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    # split outcomes with double sixes
    def test_split_pairs_returns_correct_output_with_double_6_house_upcard_2(self):
        six_hand = [Card(6), Card(6)]
        two_hand = [Card(2), Card(2)]
        self.tool.player.new_hand(six_hand)
        self.tool.house.new_hand(two_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_6_house_upcard_3(self):
        six_hand = [Card(6), Card(6)]
        three_hand = [Card(3), Card(3)]
        self.tool.player.new_hand(six_hand)
        self.tool.house.new_hand(three_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_6_house_upcard_4(self):
        six_hand = [Card(6), Card(6)]
        four_hand = [Card(4), Card(4)]
        self.tool.player.new_hand(six_hand)
        self.tool.house.new_hand(four_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_6_house_upcard_5(self):
        six_hand = [Card(6), Card(6)]
        five_hand = [Card(5), Card(5)]
        self.tool.player.new_hand(six_hand)
        self.tool.house.new_hand(five_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_6_house_upcard_6(self):
        six_hand = [Card(6), Card(6)]
        self.tool.player.new_hand(six_hand)
        self.tool.house.new_hand(six_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_6_house_upcard_7(self):
        six_hand = [Card(6), Card(6)]
        seven_hand = [Card(7), Card(7)]
        self.tool.player.new_hand(six_hand)
        self.tool.house.new_hand(seven_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_6_house_upcard_8(self):
        six_hand = [Card(6), Card(6)]
        eight_hand = [Card(8), Card(8)]
        self.tool.player.new_hand(six_hand)
        self.tool.house.new_hand(eight_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_6_house_upcard_9(self):
        six_hand = [Card(6), Card(6)]
        nine_hand = [Card(9), Card(9)]
        self.tool.player.new_hand(six_hand)
        self.tool.house.new_hand(nine_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_6_house_upcard_facecard(self):
        six_hand = [Card(6), Card(6)]
        jack_hand = [Card(11), Card(11)]
        self.tool.player.new_hand(six_hand)
        self.tool.house.new_hand(jack_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_6_house_upcard_ace(self):
        six_hand = [Card(6), Card(6)]
        ace_hand = [Card(14), Card(14)]
        self.tool.player.new_hand(six_hand)
        self.tool.house.new_hand(ace_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    # single outcome with double fives
    def test_split_pairs_returns_correct_output_with_double_facecard(self):
        five_hand = [Card(5), Card(5)]
        self.tool.tool_new_hand()
        self.tool.player.new_hand(five_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    # split outcomes with double fours
    def test_split_pairs_returns_correct_output_with_double_4_house_upcard_2(self):
        four_hand = [Card(4), Card(4)]
        two_hand = [Card(2), Card(2)]
        self.tool.player.new_hand(four_hand)
        self.tool.house.new_hand(two_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_4_house_upcard_3(self):
        four_hand = [Card(4), Card(4)]
        three_hand = [Card(3), Card(3)]
        self.tool.player.new_hand(four_hand)
        self.tool.house.new_hand(three_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_4_house_upcard_4(self):
        four_hand = [Card(4), Card(4)]
        self.tool.player.new_hand(four_hand)
        self.tool.house.new_hand(four_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_4_house_upcard_5(self):
        four_hand = [Card(4), Card(4)]
        five_hand = [Card(5), Card(5)]
        self.tool.player.new_hand(four_hand)
        self.tool.house.new_hand(five_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_4_house_upcard_6(self):
        four_hand = [Card(4), Card(4)]
        six_hand = [Card(6), Card(6)]
        self.tool.player.new_hand(four_hand)
        self.tool.house.new_hand(six_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_4_house_upcard_7(self):
        four_hand = [Card(4), Card(4)]
        seven_hand = [Card(7), Card(7)]
        self.tool.player.new_hand(four_hand)
        self.tool.house.new_hand(seven_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_4_house_upcard_8(self):
        four_hand = [Card(4), Card(4)]
        eight_hand = [Card(8), Card(8)]
        self.tool.player.new_hand(four_hand)
        self.tool.house.new_hand(eight_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_4_house_upcard_9(self):
        four_hand = [Card(4), Card(4)]
        nine_hand = [Card(9), Card(9)]
        self.tool.player.new_hand(four_hand)
        self.tool.house.new_hand(nine_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_4_house_upcard_facecard(self):
        four_hand = [Card(4), Card(4)]
        jack_hand = [Card(11), Card(11)]
        self.tool.player.new_hand(four_hand)
        self.tool.house.new_hand(jack_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_4_house_upcard_ace(self):
        four_hand = [Card(4), Card(4)]
        ace_hand = [Card(14), Card(14)]
        self.tool.player.new_hand(four_hand)
        self.tool.house.new_hand(ace_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    # split outcomes with double threes
    def test_split_pairs_returns_correct_output_with_double_3_house_upcard_2(self):
        three_hand = [Card(3), Card(3)]
        two_hand = [Card(2), Card(2)]
        self.tool.player.new_hand(three_hand)
        self.tool.house.new_hand(two_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_3_house_upcard_3(self):
        three_hand = [Card(3), Card(3)]
        self.tool.player.new_hand(three_hand)
        self.tool.house.new_hand(three_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_3_house_upcard_4(self):
        three_hand = [Card(3), Card(3)]
        four_hand = [Card(4), Card(4)]
        self.tool.player.new_hand(three_hand)
        self.tool.house.new_hand(four_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_3_house_upcard_5(self):
        three_hand = [Card(3), Card(3)]
        five_hand = [Card(5), Card(5)]
        self.tool.player.new_hand(three_hand)
        self.tool.house.new_hand(five_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_3_house_upcard_6(self):
        three_hand = [Card(3), Card(3)]
        six_hand = [Card(6), Card(6)]
        self.tool.player.new_hand(three_hand)
        self.tool.house.new_hand(six_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_3_house_upcard_7(self):
        three_hand = [Card(3), Card(3)]
        seven_hand = [Card(7), Card(7)]
        self.tool.player.new_hand(three_hand)
        self.tool.house.new_hand(seven_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_3_house_upcard_8(self):
        three_hand = [Card(3), Card(3)]
        eight_hand = [Card(8), Card(8)]
        self.tool.player.new_hand(three_hand)
        self.tool.house.new_hand(eight_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_3_house_upcard_9(self):
        three_hand = [Card(3), Card(3)]
        nine_hand = [Card(9), Card(9)]
        self.tool.player.new_hand(three_hand)
        self.tool.house.new_hand(nine_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_3_house_upcard_facecard(self):
        three_hand = [Card(3), Card(3)]
        jack_hand = [Card(11), Card(11)]
        self.tool.player.new_hand(three_hand)
        self.tool.house.new_hand(jack_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_3_house_upcard_ace(self):
        three_hand = [Card(3), Card(3)]
        ace_hand = [Card(14), Card(14)]
        self.tool.player.new_hand(three_hand)
        self.tool.house.new_hand(ace_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    # split outcomes with double twos
    def test_split_pairs_returns_correct_output_with_double_2_house_upcard_2(self):
        two_hand = [Card(2), Card(2)]
        self.tool.player.new_hand(two_hand)
        self.tool.house.new_hand(two_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_2_house_upcard_3(self):
        two_hand = [Card(2), Card(2)]
        three_hand = [Card(3), Card(3)]
        self.tool.player.new_hand(two_hand)
        self.tool.house.new_hand(three_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_2_house_upcard_4(self):
        two_hand = [Card(2), Card(2)]
        four_hand = [Card(4), Card(4)]
        self.tool.player.new_hand(two_hand)
        self.tool.house.new_hand(four_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_2_house_upcard_5(self):
        two_hand = [Card(2), Card(2)]
        five_hand = [Card(5), Card(5)]
        self.tool.player.new_hand(two_hand)
        self.tool.house.new_hand(five_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_2_house_upcard_6(self):
        two_hand = [Card(2), Card(2)]
        six_hand = [Card(6), Card(6)]
        self.tool.player.new_hand(two_hand)
        self.tool.house.new_hand(six_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_2_house_upcard_7(self):
        two_hand = [Card(2), Card(2)]
        seven_hand = [Card(7), Card(7)]
        self.tool.player.new_hand(two_hand)
        self.tool.house.new_hand(seven_hand)
        self.assertEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_2_house_upcard_8(self):
        two_hand = [Card(2), Card(2)]
        eight_hand = [Card(8), Card(8)]
        self.tool.player.new_hand(two_hand)
        self.tool.house.new_hand(eight_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_2_house_upcard_9(self):
        two_hand = [Card(2), Card(2)]
        nine_hand = [Card(9), Card(9)]
        self.tool.player.new_hand(two_hand)
        self.tool.house.new_hand(nine_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_2_house_upcard_facecard(self):
        two_hand = [Card(2), Card(2)]
        jack_hand = [Card(11), Card(11)]
        self.tool.player.new_hand(two_hand)
        self.tool.house.new_hand(jack_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")

    def test_split_pairs_returns_correct_output_with_double_2_house_upcard_ace(self):
        two_hand = [Card(2), Card(2)]
        ace_hand = [Card(14), Card(14)]
        self.tool.player.new_hand(two_hand)
        self.tool.house.new_hand(ace_hand)
        self.assertNotEqual(self.tool._split_pairs(), "Y")
