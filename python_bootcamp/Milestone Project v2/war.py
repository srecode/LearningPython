#CARD
#SUIT #RANK # VALUE

#DECK
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():

    def __init__(self):
        self.all_cards =  []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player():

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            print("1")
            # this is for multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # this is for single card object
            self.all_cards.append(new_cards)
            print("2")

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

##LOGIC

player_one = Player("one")
player_two = Player("two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_number = 0

while game_on:
    round_number += 1
    print(f"Round {round_number}")

    if len(player_one.all_cards) == 0:
        print("Player one out of cards, player two wins")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player two out of cards, player one wins")
        game_on = False
        break



##PRINTS


two_of_hearts = Card("heart", "Two")
three_of_clubs = Card("Clubs", "Three")

print(two_of_hearts)
print(two_of_hearts.suit)
print(values[two_of_hearts.rank])

print(three_of_clubs)
print(three_of_clubs.suit)
print(three_of_clubs.rank)
print(three_of_clubs.value)

new_deck = Deck()

print(new_deck.all_cards[-1])

new_deck.shuffle()

print(new_deck.all_cards[0])

deal_one = new_deck.deal_one()

print(deal_one)

print(len(new_deck.all_cards))

new_player = Player('Sam')

print(new_player)

new_player.add_cards(three_of_clubs)
new_player.add_cards(two_of_hearts)

print(new_player)

new_player.add_cards(['one','two','three'])

print(new_player)

new_player.remove_card()

print(new_player)