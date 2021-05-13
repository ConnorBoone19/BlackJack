Suits = ("Hearts", "Diamonds", "Spades", "Clubs")


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        self.points = val

    def point(self):
        if type(self.value) == int:
            point_value = self.value
            print(point_value)
        elif self.value == "Ace":
            point_value = 1
            print(point_value)
        elif type(self.value) == str:
            point_value = 10
            print(point_value)

    def show(self):
        # Printing the Cards in the deck
        print("{} of {}".format(self.value, self.suit, ))
        print(self.points)
