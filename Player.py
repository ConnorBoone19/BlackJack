from Card_File import *
from Deck_file import *



class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points = 0

    def deal(self):
        self.cards.pop()
        return self.cards.pop()

    def draw(self, deck):
        self.cardDrawn = deck.drawCard()
        self.cards.append(self.cardDrawn)

    def DrawnValue(self):
        # Used to find the value for the Card Finder File Function
        drawn_card_index = Card.value_list.index(str(Card.getValue(self.cardDrawn)))
        drawn_card_value = Card.value_list[drawn_card_index]
        return drawn_card_value

    def DrawnSuit(self):
        # Used to find the suit for the Card Finder File Function
        drawn_card_index_2 = Card.suit_list.index(str(Card.getSuit(self.cardDrawn)))
        drawn_card_suit = Card.suit_list[drawn_card_index_2]
        return drawn_card_suit

    def cardValue(self):
        value = Card.value_list.index(str(Card.getValue(self.cardDrawn)))
        if int(value) > 10:
            value = 10
        return value

    def playerPoints(self):
        self.points += self.cardValue()
        print(self.points)
        return self.points

    def showHand(self):
        for card in self.cards:
            card.show()
