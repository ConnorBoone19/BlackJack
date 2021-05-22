import Card_File_Finder as CFF
from  Deck_file import *
from Player import *
points = 0
deck = Deck()
deck.shuffle()
user = Player("Bob")


def drawACard(name):
    global points
    name.draw(deck)
    points += name.cardValue()
    if points > 21:
        print(f"you went bust")
        return False
    else:
        return points


user.draw(deck)
user.draw(deck)
user.draw(deck)
CFF.image_finder(user)
# print(f"The card drawn was a {user.DrawnValue()}")
# print(f"The suit of the card drawn is {user.DrawnSuit()}")

print(f"The user has a score of {user.points}")


