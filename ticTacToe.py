#this script is to play ticTacToe game

myBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' '}

    

def printBoard(board):
    print(myBoard['top-l'] + '  | ' + myBoard['top-m'] + ' | ' + myBoard['top-r'])
    print('---+---+---')
    print(myBoard['mid-l'] + '  | ' + myBoard['mid-m'] + ' | ' + myBoard['mid-r'])
    print('---+---+---')
    print(myBoard['low-l']+ '  | ' + myBoard['low-m'] + ' | ' + myBoard['low-r'])
    # print(printBoard)
    
turn = 'X'

for i in range(9):
    print('Turn for ' + turn + ' which space do you want to chose?')
    move = input()
    myBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
        
    printBoard(myBoard)

    # print(myBoard)
