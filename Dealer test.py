from Dealer_file import *
from Player import *
deck = Deck()
deck.shuffle()
dealer = Dealer("dealer")
user = Player("Bob")
dealer.draw(deck)
dealer.draw(deck)
dealer.draw(deck)
dealer.showHand()

