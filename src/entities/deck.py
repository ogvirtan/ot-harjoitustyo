import random
from .card import Card
from .player import Player

class Deck:

    def __init__(self):
        self.deck = []
        for i in range(2,15):
            if i == 11:
                i ="J"
            elif i == 12:
                i = "Q"
            elif i == 13:
                i = "K"
            elif i == 14:
                i = "A"
            card = Card(i)
            temp = [card] * 4
            self.deck.extend(temp)
        self._shuffle()
        self.size = len(self.deck)
    
    def _shuffle(self):
        random.shuffle(self.deck)

    def _deal_new_hand(self, player):
        #check for cards in deck
        cards = []
        cards.append(self.deck.pop())
        cards.append(self.deck.pop())
        self.size -= 2
        player._new_hand(cards)
    
    def __str__(self):
        return str(self.deck)
    
    def __repr__(self):
        return self.__str__()