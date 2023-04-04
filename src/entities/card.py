class Card:

    #suit does not matter in blackjack, so only values are used for now. Might introduce suits as added flair later
    def __init__(self, value):
        self.value = value

    def _ret_value(self):
        return self.value
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return self.__str__()