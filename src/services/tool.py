from entities.deck import Deck
from entities.player import Player

class Tool:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.house = Player()
    
    def _new_hand(self):
        self.deck._deal_new_hand(self.player)
        self.deck._deal_new_hand(self.house)
    
    def _show_hands(self):
        upcard = self.house._upcard()
        player_hand = self.player._current_hand()
        print(f"House is showing {upcard}\n\nyou have {player_hand}")

    def _double(self):
        pass

    def _surrender(self):
        pass

    def _hit(self):
        pass
    
    def _stand(self):
        pass
    
    def _split(self):
        pass