from .card import Card


class Player:
    """Class representing participants in the game of blackjack

    Attributes:
        hand: empty list representing hand
    """

    def __init__(self):
        self.hand = []

    def new_hand(self, new_hand):
        """replaces existing hand with hand offered in parameters

        Args:
            new_hand: a new hand that replaces current hand
        """
        self.hand = new_hand

    def upcard(self) -> Card:
        """Returns top card in hand

        Returns:
            card in list 'hand' at index 0
        """
        return self.hand[0]

    def downcard(self) -> Card:
        """Returns bottom card in hand

        Returns:
            card in list 'hand' at index 1
        """
        return self.hand[1]

    def current_hand(self):
        """
        Returns:
            list 'hand'
        """
        return self.hand

    def get_total(self):
        """Returns:
            the sum of numeric values in current hand
        """
        total = 0
        card: Card
        for card in self.hand:
            total += card.ret_value()
        return total

    def get_pair(self):
        """Determines whether the values of cards in hand are identical or not
        """
        if len(self.current_hand()) != 2:
            return False
        card_one: Card = self.hand[0]
        card_two: Card = self.hand[1]
        if card_one.ret_value() == card_two.ret_value():
            return True
        return False

    def __str__(self):
        return str(self.hand)

    def __repr__(self):
        return self.__str__()
