import random

def display_board(b):

    print()
    print(" {} | {} | {} ".format(b[7],b[8],b[9]))
    print("---|---|---")
    print(" {} | {} | {} ".format(b[4],b[5],b[6]))
    print("---|---|---")
    print(" {} | {} | {} ".format(b[1],b[2],b[3]))
    print()

def user_input():

    marker = " "

    while marker!='x' and marker!='o':
        marker = input("Player 1 - Choose x or o : ")

        player1 = marker

        if player1=='x':
            player2 = 'o'
        else:
            player2='x'

    return (player1,player2)

def first_turn():

    flip = random.randint(0,1)

    if flip==0:
        return "Player 1"
    else:
        return "Player 2"

def player_choice(board):
    
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose Position 1-9 : "))

    return position

def place_marker(board,mark,position):
    board[position]=mark

def win_check(board,mark):

    if (
    (board[1]==mark and board[2]==mark and board[3]==mark) or 
    (board[4]==mark and board[5]==mark and board[6]==mark) or 
    (board[7]==mark and board[8]==mark and board[9]==mark) or 
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[9]==mark and board[6]==mark and board[3]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) or
    (board[9]==mark and board[5]==mark and board[1]==mark) ) :
        return True

    else:
        return False

def space_check(board,position):

    return board[position]==" "

def full_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def replay():

    choice = input("Ready to play again ? Yes or No : ")

    return choice=='Yes'

# test_board = ['#','x','o','x','o','x','o','x','o','x']

print("Welcome to TIC TAC TOE")

while True:

    test_board = [' ']*10

    p1,p2 = user_input()

    turn = first_turn()

    print(turn + " will start the game")

    select = input("are you ready to play y or n : ")

    if select =='y':
        game_on = True
    else:
        game_on=False

    while game_on:

        if turn=="Player 1":

            display_board(test_board)

            pos = player_choice(test_board)

            place_marker(test_board,p1,pos)

            if win_check(test_board,p1):
                display_board(test_board)
                print("Player 1 Has Won")
                game_on = False
            else:
                if full_check(test_board):
                    display_board(test_board)
                    print("Tie Game")
                    game_on = False
                else:
                    turn="Player 2"
        else:

            display_board(test_board)

            pos = player_choice(test_board)

            place_marker(test_board,p2,pos)

            if win_check(test_board,p2):
                display_board(test_board)
                print("Player 2 Has Won")
                game_on = False
            else:
                if full_check(test_board):
                    display_board(test_board)
                    print("Tie Game")
                    game_on = False
                else:
                    turn="Player 1"
        
    if not replay():
        print("Exiting Game ...")
        break