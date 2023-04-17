class Card:

    # suit does not matter in blackjack, so only values are used for now.
    # Might introduce suits as added flair later
    def __init__(self, value_passed):
        if value_passed == 11:
            self.face = "J"
            self.value = 10
        elif value_passed == 12:
            self.face = "Q"
            self.value = 10
        elif value_passed == 13:
            self.face = "K"
            self.value = 10
        elif value_passed == 14:
            self.face = "A"
            self.value = 11
        else:
            self.value = value_passed
            self.face = str(value_passed)

    def ret_value(self):
        return self.value

    def _ace_it_down(self):
        if self.face == "A" and self.value == 11:
            self.value = 1

    def __str__(self):
        return str(self.face)

    def __repr__(self):
        return self.__str__()
