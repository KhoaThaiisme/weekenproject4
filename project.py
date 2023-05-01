import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f'{self.suit} of {self.value}'

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Spades', 'Diamonds', 'Hearts', 'Clubs']:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards_in_hand = []

    def add_card(self, card): #getting card when it is not 21
        self.cards_in_hand.append(card)

    def get_value(self): # adding enough point to see if close to 21 or not
        value = 0
        ace = False
        for card in self.cards_in_hand:
            if card == 1:
                ace = True
            value += card

        if ace + card <= 21:
            


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __repr__(self):
        pass

    def hit(self, card):
        self.hand.add_card(card)

    def can_hit(self):
        return self.hand.get_value() < 21

class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Player('Dealer')
        self.player = Player('Player')

    def play(self):
        self.dealer.hit(self.deck.deal())
        self.player.hit(self.deck.deal())
        self.dealer.hit(self.deck.deal(hidden=True))
        self.player.hit(self.deck.deal())

        while self.player.can_hit():
            res = input('Do you want to hit? yes/no \n')
            if res.lower() == 'yes':
                self.player.hit(self.deck.deal())
            else:
                break

        if self.dealer.hand.get_value() < 17:
            self.dealer.hit(self.deck.deal())

        if self.player.hand.get_value() > 21:
            print('You bust!!!')
            return

        if self.dealer.hand.get_value() > 21:
            print('Player win!!!')
        elif self.player.hand.get_value() > self.dealer.hand.get_value():
            print('Player win, dealer suck')
        elif self.player.hand.get_value() < self.dealer.hand.get_value():
            print('Deal win, you lose, go home!!!!')
        else: 
            print('tied, it\'s a tie, play again?')

