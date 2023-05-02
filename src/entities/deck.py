import random
from .card import Card


class Deck:
    """Class Deck representing the remaining cards in the deck, from which 
    the cards to play blackjack are dealt from

        Attributes:
            deck= a list of cards
    """

    def __init__(self):
        self.deck = []
        self.add_deck()
        self._shuffle()

    def add_deck(self):
        """Adding deck
        """
        for i in range(2, 15):
            card = Card(i)
            temp = [card] * 4
            self.deck.extend(temp)

    def _shuffle(self):
        """Shuffles deck
        """
        random.shuffle(self.deck)

    def deal_new_hand(self):
        """Returns:
            a list containing the two topmost cards in deck
        """
        self._check_for_deck_size()
        cards = []
        cards.append(self.deck.pop())
        cards.append(self.deck.pop())
        return cards

    def _deck_size(self):
        """Returns:
            a numeric value of cards left in the list 'deck'             
        """
        return len(self.deck)

    def _check_for_deck_size(self):
        """If deck contains less than 3 cards, a new deck is added
        """
        if self._deck_size() < 3:
            self.add_deck()
        self._shuffle()
