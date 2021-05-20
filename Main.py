import Card_File_Finder as CFF

points = 0
deck = Deck()
deck.shuffle()
user = Player("Bob")


def drawACard(name):
    global points
    name.draw(deck)
    points += name.cardValue()
    return points


drawACard(user)
user.showHand()
CFF.image_finder(user)
# print(f"The card drawn was a {user.DrawnValue()}")
# print(f"The suit of the card drawn is {user.DrawnSuit()}")

print(f"The user has a score of {points}")


