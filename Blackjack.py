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


    def display(self):
        if self.dealer:
            print("hidden")
            print(self.cards[1])
        else:
            for card in self.cards :
                print(card)
        print("Value " + str(self.getValue()))


class Game:
    
    def __init__(self):
        pass

    def play(self):

        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hard = Hand(dealer=True)

            for i in range(2):
                self.player_hand.addCard(self.deck.deal())
                self.dealer_hand.addCard(self.deck.deal())

            print("your hand is ")
            self.player_hand.display()
            print("dealer hand is ")
            self.dealer_hand.display()

            game_over = False
            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack,dealer_has_blackjack)
                    continue
               choice = input("Please enter Hit, or 'h' if you wish to hit, and Stick, or 's' if you wish to stick").lower()
               while choice not in ["h","s","hit","stick"]:
                   choice = input("Please enter 'Hit' or 'Stick' (or H/S)").lower()
    


    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.getValue() == 21:
            player = True
        if self.dealer_hand.getValue() == 21:
            dealer = True

        return player,dealer

    def show_blackjack_results(self,player,dealer):
        if player and dealer:
            print("Both have blackjack. Draw. ")
        elif player:
            print("You have blackjack! A winner is you!")
        elif dealer:
            print("Dealer has blackjack! Dealer wins. ")



