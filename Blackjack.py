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


    def calculateValue(self):
       self.value = 0
       aces = 0
       for c in self.cards:
           if c.value.isnumeric():
               self.value += int(c.value)
           else:
                if c.value == "A":
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
            self.dealer_hand = Hand(dealer=True)

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
                choice = input("Please enter Hit, or 'h' if you wish to hit, and Stick, or 's' if you wish to stick   ").lower()
                while choice not in ["h","s","hit","stick"]:
                   choice = input("Please enter 'Hit' or 'Stick' (or H/S)").lower()
                if choice in ['hit','h']:
                    self.player_hand.addCard(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("You went bust")
                        game_over = True
                else:
                    player_hand_value = self.player_hand.getValue()
                    dealer_hand_value = self.dealer_hand.getValue()

                    print("Final Results ")
                    print("Your hand " + str(player_hand_value))
                    print("Dealer's hand " + str(dealer_hand_value))

                    if player_hand_value > dealer_hand_value :
                        print("You Win!")
                    elif player_hand_value == dealer_hand_value :
                        print("Tie :) ")
                    else : 
                        print("Dealer Wins !")
                    game_over = True
                
            again = input("Play again? [Y/N]").lower()
            while again not in ['y','n']:
                again = input("please input 'y' or 'n' ")
            if again == 'n' :
                print("Thanks for playing :) ")
                playing = False
            else :
                game_over = False

    def player_is_over(self):
        return self.player_hand.getValue() > 21


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


if __name__ == "__main__":
    game = Game()
    game.play()
