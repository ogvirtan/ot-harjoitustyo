from entities.deck import Deck
from entities.player import Player


class Tool:
    """Class Tool is in charge of the application logic.

    Players hand and the card that house is showing are taken into account here,
    and optimal strategy is being determined based on what options are available
    to the player. Tool is in charge of tracking how many times the player picked
    correctly or incorrectly and for the resetting of said statistics.

    Attributes:
        deck: deck of cards configured to be infinite for the purposes of the game
        player: the player making strategy choices
        house: the player to beat using optimal strategy
        tracking_dict: dictionary for keeping score on whether the player played optinal or not
        surrender: boolean determining whether surrendering is an option
        das: boolean determining whether doubling after split is an option
    """

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.house = Player()
        self.tracking_dict = {"W": 0,
                              "L": 0
                              }
        self.surrender = True
        self.das = True

    def tool_new_hand(self):
        """Get new hand for house and player
        """
        player_new_hand = self.deck.deal_new_hand()
        house_new_hand = self.deck.deal_new_hand()
        self.player.new_hand(player_new_hand)
        self.house.new_hand(house_new_hand)

    def show_hands(self):
        """Have player show his hand and house show their top card

            Returns:
                a string containing information about the game state
        """
        upcard = self.house.upcard()
        player_hand = self.player.current_hand()
        return f"\nHouse is showing {upcard.face}\n\nyou have {player_hand}\n"

    def check_for_blackjack(self):
        """Check if player hand has blackjack

            Returns:
                boolean value
        """
        if self.player.get_total() == 21:
            return True
        return False

    def tracking(self, player_input, best_input):
        """Add note of the strategy the player chose
        """
        if player_input == best_input:
            self.tracking_dict["W"] += 1
        else:
            self.tracking_dict["L"] += 1

    def return_stats(self):
        """Returns:
            statistics of the players strategy accuracy
        """
        return self.tracking_dict

    def reset_stats(self):
        """Reset statistics
        """
        self.tracking_dict["W"] = 0
        self.tracking_dict["L"] = 0

    def strategy(self):
        """Determining which method needs to be called
        """
        if self.player.get_pair():
            return self._split_pairs()
        if self.player.downcard().face == "A" or self.player.upcard().face == "A":
            return self._ace_in_hand()
        return self._hard_totals()

    def _split_pairs(self):
        """Check if pairs should be split

            Returns:
                a character which represents the optimal strategy
        """
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
            if not self.das and house_upcard_value == 2:
                return self._hard_totals()
            return "Y"
        if player_upcard_value == 4 and self.das and house_upcard_value in [5, 6]:
            return "Y"
        if player_upcard_value == 3 and house_upcard_value < 8:
            if house_upcard_value < 4 and not self.das:
                return self._hard_totals()
            return "Y"
        if player_upcard_value == 2 and house_upcard_value < 8:
            if house_upcard_value < 4 and not self.das:
                return self._hard_totals()
            return "Y"
        return self._hard_totals()

    def _ace_in_hand(self):
        """Checks for the optimal strategy when the player is holding an ace

        Returns:
                a character which represents the optimal strategy
        """
        we_check_this_card = self.player.downcard().ret_value()
        if self.player.downcard().face == "A":
            we_check_this_card = self.player.upcard().ret_value()
        if we_check_this_card == 9:
            return "S"
        if we_check_this_card == 8:
            if self.house.upcard().ret_value() == 6:
                return "D"
            return "S"
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
        if 5 <= self.house.upcard().ret_value() <= 6:
            return "D"
        return "H"

    def _hard_totals(self):
        """Checks for the optimal strategy when only the total value of hand matters

            Returns:
                a character which represents the optimal strategy
        """
        player_total = self.player.get_total()
        if player_total >= 17:
            return "S"
        if 13 <= player_total <= 16:
            if self.surrender:
                if 9 <= self.house.upcard().ret_value() <= 11 and player_total == 16:
                    return "F"
                if self.house.upcard().ret_value() == 10 and player_total == 15:
                    return "F"
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

    def change_surrender_status(self):
        """Enables/disables the option to surrender
        """
        if self.surrender:
            self.surrender = False
        else:
            self.surrender = True

    def change_das_status(self):
        """Enables/disables the option to double after split
        """
        if self.das:
            self.das = False
        else:
            self.das = True
