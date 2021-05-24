from Card_File import *
from Deck_file import *


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points = 0
        self.game_over = False

    def draw(self, deck):
        # draws a card
        print("user hand:")
        self.cardDrawn = deck.drawCard()
        self.cards.append(self.cardDrawn)
        # the ace safety
        if self.cardValue() == 1:
            self.points += 11
            if self.points > 21:
                self.points -= 10

        else:
            self.points += self.cardValue()
        self.showHand()

        if self.points > 21:
            print("You went bust! ")
            self.game_over = True
            return
        else:
            print(f"user's points are {self.points} \n")
            return self.points

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
        # returns the players points
        if self.cardValue() == "Ace":
            self.points += 11
            if self.points >21:
                self.points -= 10

        else:
            self.points += self.cardValue()
        return self.points

    def showHand(self):
        # shows the players hand
        for card in self.cards:
            card.show()

    def resetPlayer(self):
        self.points = 0
        self.cards = []
