# a simple blackjack game

import random


class Card:
    
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return " of ".join((self.value, self.suit))


class Deck:

    def __init__(self):
        self.cards = [Card(v,s) for v in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] for s in ["Clubs","Diamonds","Hearts","Spades"]]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

    def __repr__(self):
        return "The deck has " + str(len(self.cards)) + " cards"


deck = Deck()
print(deck)
deck.shuffle()
for i in deck.cards:
    print(i)


