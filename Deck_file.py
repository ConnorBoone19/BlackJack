import random
from Card_File import *



class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    # Populates deck
    def build(self):
        for s in ['Diamonds', 'Hearts', 'Spades', 'Clubs']:
            for v in ['Ace']:
                self.cards.append(Card(s, v))
            for v in range(2, 11):
                self.cards.append(Card(s, v))
            for v in ['Jack', 'Queen', 'King']:
                self.cards.append(Card(s, v))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            num = random.randint(0, i)
            self.cards[i], self.cards[num] = self.cards[num], self.cards[i]

    def drawCard(self, i=0):
        if len(self.cards) < 1:
            # Checks to see if there is the proper amount of cards in deck
            exit("No more cards in deck!")
        return self.cards.pop(i)

    def show(self):
        for c in self.cards:
            c.show()

    def resetDeck(self):
        self.cards = []
