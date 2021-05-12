
class Card:
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val
    def show(self):
        # Printing the Cards in the deck
        print("{} of {}".format(self.value,self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    # Populates deck
    def build(self):
        for s in ['Diamonds','Hearts','Spades','Clubs']:
            for v in ['Ace']:
                self.cards.append(Card(s,v))
            for v in range(2,14):
                self.cards.append(Card(s,v))
            for v in ['Jack','Queen','King']:
                self.cards.append(Card(s,v))
    def show(self):
        for c in self.cards:
            c.show()
deck = Deck()
deck.show()