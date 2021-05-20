class Card:
    suit_list = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
    value_list = ['Card value_list', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getValue(self):
         return self.value

    def getSuit(self):
        return self.suit

    def show(self):
        print("{} of {}".format(self.value, self.suit))
