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
        return self.suit + " of " + self.rank


class Deck():
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Create a card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            #List of cards
            self.all_cards.extend(new_cards)
        else:
            #For single card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards in hand"


new_card = Deck()

my_card = new_card.deal_one()

new_player = Player("Jose")
print(new_player)
new_player.add_card(my_card)
print(new_player)
print(new_player.all_cards[0])
new_player.add_card([my_card,my_card,my_card,my_card])
print(new_player)
new_player.remove_one()
print(new_player)
# new_deck = Deck()
#
# print(new_deck.all_cards[1])
#
# pop_card = new_deck.deal_one()
# print(pop_card)
# print(len(new_deck.all_cards))
# two_of_hearts = Card("Hearts", "Two")
# three_of_clubs = Card("Clubs", "Three")
#
# print(two_of_hearts)
# print(two_of_hearts.rank)
# print(two_of_hearts.suit)
# print(two_of_hearts.value)
#
# print(two_of_hearts.value < three_of_clubs.value)