
import random

def display_board(board):
    print('    |   |')
    print('  '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('______________')
    print('    |   |')
    print('  '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('______________')
    print('    |   |')
    print('  '+ board[1] + ' | ' + board[2] + ' | ' + board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Please select 'X or 'O': ")
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

# print(player_input())

def place_maker(board, marker, position):
    board[position] = marker

# place_maker(test_board, '$', 8)
# display_board(test_board)


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))

# print(win_check(test_board,'X'))

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player1'
    else:
        return 'Player2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Please choose a position in range of (1-9): "))

    return position

def replay():

    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('Y')


print("Welcome to Tic Toc Toe game")

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " Will go first.")

    play_game = input("Are you ready to play, Yes or No: ")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_maker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Congratulations, you have won the game!!!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is draw")
                    break
                else:
                    turn = 'Player2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_maker(theBoard, player2_marker, position)
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("Congratulations, you have won the game!!!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is draw")
                    break
                else:
                    turn = 'Player1'

    if not replay():
        break





