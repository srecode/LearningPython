def display_game(game_list):
    print("Here is your list")
    print(game_list)

def position_choice():
    choice = 'wrong'
    while choice not in ['0', '1', '2']:
        choice = input("Pick a position to replace (0, 1, 2): ")
        if choice not in ['0', '1', '2']:
            print("Please choose a valid position")

    return int(choice)

def replace_position(game_list, position):
    user_placement = input("Type a string to replace position")
    game_list[position] = user_placement

    return game_list

def gameon_choice():
    choice = 'wrong'

    while choice not in ('Y', 'N'):
        choice = input("Do you still want to play, 'Y or 'N: ")

        if choice not in ('Y', 'N'):
            print("Please select 'Y or 'N'")


    if choice == 'Y':
        return True
    else:
        return False

game_on = True
game_list = [0, 1, 2]

while game_on:
    display_game(game_list)
    position = position_choice()

    game_list = replace_position(game_list, position)

    display_game(game_list)

    game_on