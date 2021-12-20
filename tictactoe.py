import random

'''
Tic Tac Toe Game 
'''

def display_board(board):

    print()
    print(" {} | {} | {} ".format(board[7],board[8],board[9]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[4],board[5],board[6]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[1],board[2],board[3]))
    print()

def user_input(pl1):

    marker = " "

    while marker!='x' and marker!='o':
        marker = input(f"\n{pl1} - Choose x or o : ")

        player1 = marker

        if player1=='x':
            player2 = 'o'
        else:
            player2='x'

    return (player1,player2)

def first_turn(pl1="Player 1",pl2="Player 2"):

    flip = random.randint(0,1)

    if flip==0:
        return pl1
    else:
        return pl2

def player_choice(board,turn,p):
    
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):     
        try:
            position = int(input(f"{turn} ({p}) Choose Position 1-9 : "))
        except:
            print("enter a valid input\n")
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

print("Welcome to TIC TAC TOE !\n")

while True:

    test_board = [' ']*10

    pl1 = input("enter player 1 name : ")
    pl2 = input("enter player 2 name : ")

    p1,p2 = user_input(pl1)

    turn = first_turn(pl1,pl2)

    print("\n"+turn + " will start the game")

    select = input("\nAre you ready to play y or n : ")

    if select =='y':
        game_on = True
    else:
        game_on=False

    while game_on:

        if turn==pl1:

            display_board(test_board)

            pos = player_choice(test_board,turn,p1)

            place_marker(test_board,p1,pos)

            if win_check(test_board,p1):
                display_board(test_board)
                print("Player 1 Has Won\n")
                game_on = False
            else:
                if full_check(test_board):
                    display_board(test_board)
                    print("Tie Game\n")
                    game_on = False
                else:
                    turn=pl2
        else:

            display_board(test_board)

            pos = player_choice(test_board,turn,p2)

            place_marker(test_board,p2,pos)

            if win_check(test_board,p2):
                display_board(test_board)
                print("Player 2 Has Won\n")
                game_on = False
            else:
                if full_check(test_board):
                    display_board(test_board)
                    print("Tie Game\n")
                    game_on = False
                else:
                    turn=pl1
        
    if not replay():

        print("Exiting Game ...")
        break
