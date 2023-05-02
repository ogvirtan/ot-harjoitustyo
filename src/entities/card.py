class Card:
    """"Class representing cards

        Suit does not matter in blackjack, so only faces and values are given as attributes.

        Attributes:
            face: the face printed on the card
            value: the numeric value of the card
    """

    def __init__(self, value_passed):
        """Value and face are determined here

            Args:
                value_passed: numerical value of a card
        """
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
        """Returns:
            value of card
        """
        return self.value

    def __str__(self):
        return str(self.face)

    def __repr__(self):
        return self.__str__()
