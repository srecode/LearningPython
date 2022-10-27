import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank+ " of "+self.suit


class Deck():

    def __init__(self):
        self.deck = [] # Start with empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        self.deck_comp = ''
        for card in self.deck:
            self.deck_comp += '\n' + card.__str__()
        return "the deck has "+ self.deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand():
    def __init__(self):
        self.card = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        #this is going to be from Deck.deal() --> single Card(suit, rank)
        self.card.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # If total value is more than 21 with ace, consider ace as 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lost_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f"Sorry you do not have enough chips, you have {chips.total}")
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_and_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter H or S ")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player would like to stand")
            playing = False
        else:
            print("Sorry, I don't understand the input. Please enter S or H only")
            continue
        break

def  show_some(player, dealer):

    #show one of the dealers card
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.card[1])

    #show two of the players card.
    print("\n printing player's hand:")
    for c in player.card():
        print(c)

def show_all(player, dealer):
    #Show both dealer and players card

    # print("\n printing dealer's hand:")
    # for card in dealer.cards():
    #     print(card)
    # You can also write above code as
    print("\n print dealer's hand", *dealer.card,sep='\n')
    print(f"Dealer value {dealer.value}")
    print("\n printing player's hand:")
    for c in player.card():
        print(c)
    print(f"Dealer value {player.value}")

def player_burst(player, dealer, chips):
    print("BURST PLAYER")
    chips.lost_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS")
    chips.win_bet()

def dealer_burst(player, dealer, chips):
    print("PLAYER WINS, DEALER BURSTED")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER WINS")
    chips.lost_bet()

def push(player, dealer):
    print("Dealer and Player tie! PUSH")


while True:
    print("Welcome to BlackJack")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)


    show_some(player_hand, dealer_hand)

    while playing:
        hit_and_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_burst(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value < 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_burst(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(dealer_hand, player_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(dealer_hand, player_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print(f"\n total player chips are: {player_chips}")

    new_game = input("Would you like to play again? y/n")

    if new_game[0].lower == 'y':
        playing = True
        continue
    else:
        print("Thanks for Playing")
    break




# if __name__ == '__main__':
#     mydeck = Deck()
#     mydeck.shuffle()
#     test_player = Hand()
#     pull_card = mydeck.deal()
#     print(f"pull card : {pull_card}")
#     test_player.add_card(pull_card)
#     print(f"test_player {test_player.value}")


