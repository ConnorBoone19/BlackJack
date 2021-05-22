from Dealer_file import *
from Deck_file import *
from Player import *
from Card_File import *

deck = Deck()
deck.shuffle()
dealer = Dealer("dealer")
user = Player("Bob")

while dealer.draw(deck) != "end":
    dealer.draw(deck)

