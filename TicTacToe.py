#creating board
def display_board(board):
    print (f'{board[7]} | {board[8]} | {board[9]}')
    print('---------')
    print (f'{board[4]} | {board[5]} | {board[6]}')
    print('---------')
    print (f'{board[1]} | {board[2]} | {board[3]}')

#options
board=['#','X','O','O','X','X','X','O','X','O']

#random toss
import random
def choose_first():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'

# X or O Selection
def player_input():
    marker=''
    while not (marker=='X' or marker=='O'):
        marker=input('Player 1: Do you want X or O? ').upper()
    if marker=='X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#marker position
def place_marker(board,marker,position):
    board[position]=marker

#winning condition check
def win_check(board,mark):
    return((board[7]==mark and board[8]==mark and board[9]==mark) or
          (board[4]==mark and board[5]==mark and board[6]==mark) or
          (board[1]==mark and board[2]==mark and board[3]==mark) or
          (board[3]==mark and board[6]==mark and board[9]==mark) or
          (board[2]==mark and board[5]==mark and board[8]==mark) or
          (board[1]==mark and board[4]==mark and board[7]==mark) or
          (board[3]==mark and board[5]==mark and board[7]==mark) or
          (board[1]==mark and board[5]==mark and board[9]==mark))

#empty or not check
def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#player entry position check
def player_choice(board,my_str):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Chose your position between (1-9)'))
    return position

#main gaming condition
print("Welcome to Tic-Tac-Toe!")

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn+ ' Will make the first move!')
    
    play_game = input('Are you ready to play the game, yes or no?')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else: 
        game_on = False
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            display_board(theBoard)
            position = player_choice(theBoard, turn)
            place_marker(theBoard, player1_marker, position)
            
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Winner Winner Chicken Dinner!!!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard, turn)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'