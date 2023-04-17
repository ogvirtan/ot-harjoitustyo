from entities.deck import Deck
from entities.player import Player


class Tool:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.house = Player()
        self.tracking_dict = {"W": 0,
                              "L": 0
                              }

    def tool_new_hand(self):
        player_new_hand = self.deck.deal_new_hand()
        house_new_hand = self.deck.deal_new_hand()
        self.player.new_hand(player_new_hand)
        self.house.new_hand(house_new_hand)

    def show_hands(self):
        upcard = self.house.upcard()
        player_hand = self.player.current_hand()
        return f"\nHouse is showing {upcard.face}\n\nyou have {player_hand}\n"

    def check_for_blackjack(self):
        if self.player.get_total() == 21:
            return True
        return False

    def tracking(self, player_input, best_input):
        if player_input == best_input:
            self.tracking_dict["W"] += 1
        else:
            self.tracking_dict["L"] += 1

    def return_stats(self):
        return self.tracking_dict

    def reset_stats(self):
        self.tracking_dict["W"] = 0
        self.tracking_dict["L"] = 0

    def strategy(self):
        # Splitting pairs strategy
        if self.player.get_pair():
            return self._split_pairs()

        # Soft totals
        if self.player.downcard().face == "A" or self.player.upcard().face == "A":
            return self._ace_in_hand()

        # Hard totals/surrender
        return self._hard_totals()

    def _split_pairs(self):
        player_upcard_value = self.player.upcard().ret_value()
        house_upcard_value = self.house.upcard().ret_value()
        if player_upcard_value == 11:
            return "Y"
        if player_upcard_value == 9 and house_upcard_value not in [7, 10, 11]:
            return "Y"
        if player_upcard_value == 8:
            return "Y"
        if player_upcard_value == 7 and house_upcard_value < 8:
            return "Y"
        if player_upcard_value == 6 and house_upcard_value < 7:
            return "Y"
        if player_upcard_value == 4 and house_upcard_value in [5, 6]:
            return "Y"
        if player_upcard_value == 3 and house_upcard_value < 8:
            return "Y"
        if player_upcard_value == 2 and house_upcard_value < 8:
            return "Y"
        # Hard totals if not splitting
        return self._hard_totals()

    def _ace_in_hand(self):
        we_check_this_card = self.player.downcard().ret_value()
        if self.player.downcard().face == "A":
            we_check_this_card = self.player.upcard().ret_value()
        if we_check_this_card == 9:
            return "S"
        if we_check_this_card == 8:
            if self.house.upcard().ret_value() == 6:
                return "D"
            if self.house.upcard().ret_value() <= 8:
                return "S"
            return "H"
        if we_check_this_card == 7:
            if self.house.upcard().ret_value() <= 6:
                return "D"
            if self.house.upcard().ret_value() <= 8:
                return "S"
            return "H"
        if we_check_this_card == 6:
            if 3 <= self.house.upcard().ret_value() <= 6:
                return "D"
            return "H"
        if we_check_this_card in [5, 4]:
            if 4 <= self.house.upcard().ret_value() <= 6:
                return "D"
            return "H"
        # card is either 3 or 2
        if 5 <= self.house.upcard().ret_value() <= 6:
            return "D"
        return "H"

    def _hard_totals(self):
        player_total = self.player.get_total()
        if player_total >= 17:
            return "S"
        if 13 <= player_total <= 16:
            # check for surrender
            if self.house.upcard().ret_value() < 7:
                return "S"
            return "H"
        if player_total == 12:
            if 3 < self.house.upcard().ret_value() < 7:
                return "S"
            return "H"
        if player_total == 11:
            return "D"
        if player_total == 10:
            if self.house.upcard().ret_value() < 10:
                return "D"
            return "H"
        if player_total == 9:
            if 2 < self.house.upcard().ret_value() < 7:
                return "D"
            return "H"
        return "H"
