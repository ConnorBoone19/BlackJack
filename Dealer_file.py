from Card_File import *
from Deck_file import *


class Dealer:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points = 0
        # at casinos dealers can not draw after if they have a certain point
        self.canDraw = True
        self.gameOver = False
        self.winner = False
        self.oneMoreDraw = False
    def deal(self):
        self.cards.pop()
        return self.cards.pop()

    def draw(self, deck):
        # Checks to see if the game is over or not
        if not self.gameOver:
            # Checks to see if the dealer can draw or not
            if self.canDraw:
                # print("The dealers hand is:")
                self.cardDrawn = deck.drawCard()
                self.cards.append(self.cardDrawn)
                # the ace safety
                if self.cardValue() == 1:
                    self.points += 11
                    if self.points > 21:
                        self.points -= 10

                else:
                    self.points += self.cardValue()
                if self.points > 21:
                    self.canDraw = False
                    self.gameOver = True
                    self.showHand()
                elif self.points == 21:
                    self.showHand()
                    self.canDraw = False

                    # print("the dealer wins! \n")

                elif self.points >= 17:
                    # Rule is, dealer can not hit on 17 or higher
                    self.canDraw = False
                    self.showHand()
                    # print(f"the dealers score is {self.points} and cannot draw again \n")

                else:
                    self.showHand()
                    # print(f"Dealers points are {self.points} \n")
            else:
                # print(f"Dealer cannot draw because there score of {self.points}\n")
                return "end"
        else:
             #print(f"\nDealer went bust and has a score of {self.points}")
            return "end"

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

    def dealerPoints(self):
        self.points += self.cardValue()
        return self.points

    def showHand(self):
        for card in self.cards:
            card.show()

    def whatActions(self):
        # gives a list of actions the dealer can take
        if self.points < 21:
            if self.points >= 17:
                self.canDraw = False
                self.gameOver = False
                return
            else:
                self.canDraw = True
                self.gameOver = False
        elif self.points >= 21:
            self.canDraw = False
            self.gameOver = True
            self.winner = False
            return self.winner

