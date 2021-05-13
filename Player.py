import Cards
from Cards import *
from Deck import Deck
from WelcomeScreen import name



class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.points = 0

    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def showHand(self):
        for card in self.hand:
            card.show()



deck = Deck()
deck.shuffle()

print("p1")
bob = Player("Bob")
bob.draw(deck)
bob.draw(deck)
bob.showHand()


print("p2")


tim = Player("Bob")
tim.draw(deck)
tim.draw(deck)
tim.showHand()
print("deck")
deck.show()
