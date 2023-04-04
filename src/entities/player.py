class Player:

    def __init__(self):
        self.hand = []

    def _current_hand(self):
        return self.hand

    def _new_hand(self, new_hand):
        self.hand = new_hand

    def _upcard(self):
        return self.hand[0]
    
    def __str__(self):
        return str(self.hand)
    
    def __repr__(self):
        return self.__str__()