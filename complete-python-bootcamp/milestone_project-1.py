import random

#Consider board as a list, where each index 1-9 corresponds with a number on a number pad. Here, we get a 3 by 3 board
#  representation
def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')



#this functionn is for taking input from the player
def player_input():
    marker =''
    while not(marker == 'O' or marker =='X'):
        marker = (input("Player 1: Do you want to X or O?")).upper()

    if marker == 'O':
        return ('O','X')
    else:
        return ('X','O')


#function to assign the desired position to the marker
def  place_marker(position, board, marker):
    board[position] = marker


#to check if someone  win the game.
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


#function to choose which player go first

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


#function to indicating  whether a space on the board is freely available
def check_space(board, position):
    return board[position] == ' '


#function to check, if the board is full or not
def full_board_check(board):
    for i in range(1,10):
        if check_space(board, i):
            return False
    return True


#function that asks for player next position as a number(1-9)
def player_choice(board):
    position = ' '

    while position not in '1 2 3 4 5 6 7 8 9'.split() or not check_space(board, int(position)):
        position = input("Choose your next-position:  (1-9) ")
    return int(position)

#fuction to ask the players, if they play again
def replay():
    return input("Do you want to play again ? Enter Yes or No").lower().startswith('y')


#Here we use all above functions to run the game

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + "will go first!")
    game_on = True

    while game_on:

        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(position, theBoard, player1_marker)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Congratulaions, You have won the match")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is tie")
                    break
                else:
                    turn = 'Player 2'


        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(position, theBoard, player2_marker)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("Player 2 has won the match")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is tie")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break




