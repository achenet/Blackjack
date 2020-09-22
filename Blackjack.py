# a simple blackjack game

import random


class Card:
    
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __repr__(self,):
        return " of ".join((self.value, self.suit))



card = Card("Q","Hearts")
print(card)
