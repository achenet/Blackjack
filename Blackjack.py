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


class Hand:

    def __init__(self, dealer=False):
        self.dealer=dealer
        self.cards = []
        self.value = 0

    def addCard(self,card):
        self.cards.append(card)


    def calculatValue(self):
       self.value = 0
       aces = 0
       for card in self.cards():
           if card.isnumeric():
               self.value += int(card.value)
            else:
                if card.value == "A":
                    aces += 1
                    self.value += 11
                else: 
                    self.value += 10
        while self.value > 21 and aces > 0:
            self.value -= 10
            aces -=1


    def getValue(self):
        self.calculateValue()
        return self.value

