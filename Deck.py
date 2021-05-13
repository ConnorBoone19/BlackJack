from Cards import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    # Populates deck
    def build(self):
        for s in ['Diamonds', 'Hearts', 'Spades', 'Clubs']:
            for v in ['Ace']:
                self.cards.append(Card(s, v))
            for v in range(2, 10):
                self.cards.append(Card(s, v))
            for v in ['Jack', 'Queen', 'King']:
                self.cards.append(Card(s, v))


    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            num = random.randint(0, i)
            self.cards[i], self.cards[num] = self.cards[num], self.cards[i]

    def drawCard(self):
        return self.cards.pop()
