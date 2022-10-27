"""
Creating CARD Class
#SUIT, RANK, VALUE
"""

from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of "+ self.suit

class Deck:
    """
    This Class is used to create deck of cards, shuffle and deal them
    """

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Creat card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def __str__(self):
        return f"{self.all_cards}"

class Player:
    """
    This class is used to hold list of cards for players
    """
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"{self.name}"

#Assigning a names to players
player_one = Player('one')
player_two = Player('two')

#Assigning new deck of cards
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0

while game_on:
    """
    Starting the game with while loop
    """
    #counting the number of rounds
    round_num += 1
    print(f"This is round {round_num}")

    if len(player_one.all_cards) == 0:
        print(f"Player {player_one} has no cards left, player {player_one} lost and player {player_two} wins.")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(f"Player {player_two} has no cards left, player {player_two} lost and player {player_one} wins.")
        game_on = False
        break

    #Current number of cards on board
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())




    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR!")

            if len(player_one.all_cards) < 5:
                print("Player one unable to declare war")
                print("Player TWO WINS")
                game_on = False
                break

            if len(player_two.all_cards) < 5:
                print("Player two unable to declare war")
                print("Player ONE WINS")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


