import random
from .card import Card


class Deck:

    def __init__(self):
        self.deck = []
        self.add_deck()
        self._shuffle()

    def add_deck(self):
        for i in range(2, 15):
            card = Card(i)
            temp = [card] * 4
            self.deck.extend(temp)

    def _shuffle(self):
        random.shuffle(self.deck)

    def deal_new_hand(self):
        self._check_for_deck_size()
        cards = []
        cards.append(self.deck.pop())
        cards.append(self.deck.pop())
        return cards

    def _deck_size(self):
        return len(self.deck)

    def _check_for_deck_size(self):
        if self._deck_size() < 3:
            self.add_deck()
        self._shuffle()
