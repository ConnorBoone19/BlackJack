from Dealer_file import *
from Player import *

# Initializes the game, making and shuffling the deck.
deck = Deck()
deck.shuffle()
# Creates the dealer and player
dealer = Dealer("Dealer")
# Switch to an input statement for the user's name
user = Player("Bob")

