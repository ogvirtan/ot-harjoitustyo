from .card import Card


class Player:

    def __init__(self):
        self.hand = []

    def new_hand(self, new_hand):
        self.hand = new_hand

    def upcard(self) -> Card:
        return self.hand[0]

    def downcard(self) -> Card:
        return self.hand[1]

    def current_hand(self):
        return self.hand

    def get_total(self):
        total = 0
        card: Card
        for card in self.hand:
            total += card.ret_value()
        return total

    def get_pair(self):
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
