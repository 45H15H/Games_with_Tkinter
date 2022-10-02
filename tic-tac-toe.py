'''Tic-Tac-Toe'''


print("Welcome to Tic-Tac-Toe!".center(40, '*'))

# using dictionary to store the board
board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# each key is for each location on the board
# each value is for the character in that location
# the value can be 'X', 'O', or ' '

# now to print this dictionary like an actual board
def printBoard(b):
    print(b['top-L'] + '|' + b['top-M'] + '|' + b['top-R'])
    print('-+-+-')
    print(b['mid-L'] + '|' + b['mid-M'] + '|' + b['mid-R'])
    print('-+-+-')
    print(b['low-L'] + '|' + b['low-M'] + '|' + b['low-R'])

printBoard(board)
# this function can display the the board in its any state.

# now to get input from the user to place their character in the board
# using loops

turn = "X" # -> setting first turn to be X

for i in range(9): # <- Cuz there are 9 spaces
    printBoard(board)
    print("Turn for " + turn + ". Move to which space? ")
    move = input() # move should be a key in the dictionary
    if move in board:
        board[move] = turn
        if turn == 'X': turn = 'O'
        else: turn = 'X'
    else:
        print("You can't go there. Try again")
        continue
    # checking for winning condition
    if board['top-L'] == board['top-M'] == board['top-R'] != ' ':
        printBoard(board)
        print("Game Over. " + turn + " won!")
        break
    elif board['mid-L'] == board['mid-M'] == board['mid-R'] != ' ':
        printBoard(board)
        print("Game Over. " + turn + " won!")
        break
    elif board['low-L'] == board['low-M'] == board['low-R'] != ' ':
        printBoard(board)
        print("Game Over. " + turn + " won!")
        break
    elif board['top-L'] == board['mid-L'] == board['low-L'] != ' ':
        printBoard(board)
        print("Game Over. " + turn + " won!")
        break
    elif board['top-M'] == board['mid-M'] == board['low-M'] != ' ':
        printBoard(board)
        print("Game Over. " + turn + " won!")
        break
    elif board['top-R'] == board['mid-R'] == board['low-R'] != ' ':
        printBoard(board)
        print("Game Over. " + turn + " won!")
        break
    elif board['top-L'] == board['mid-M'] == board['low-R'] != ' ':
        printBoard(board)
        print("Game Over. " + turn + " won!")
        break
    elif board['top-R'] == board['mid-M'] == board['low-L'] != ' ':
        printBoard(board)
        print("Game Over. " + turn + " won!")
        break
    # if its the last stem and none of the above condition met
    elif i == 8:
        printBoard(board)
        print("Game Over. It's a Tie!")
        break
    # but somehow it shows O won instead of X won
    # it also doesn't account for already filled space
printBoard(board)
