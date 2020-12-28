## First step is to display the game board
def display_board():
    lst = ['']*9
    # lst = ['X','1','1','X','0','0','X','7','7']
    print("Let's start the game!")
    print("|".join(lst[:3]))
    print("|".join(lst[3:6]))
    print("|".join(lst[6:]))
    # print(f'{lst[:3]}\n{lst[3:6]}\n{lst[6:]}'
    return lst    # Had problem with displaying on a few lines


# lst = display_board()
# print(lst[0])

## Define the player's index position
def user1_pos():
    choice = 'wrong'
    while choice.isdigit() == False or int(choice) not in range(0, 9):  # indices 0..8
        choice = input("Choose the position: ")
        if choice.isdigit() == False:
            print('Please, choose a number')
        elif int(choice) not in range(0, 9):
            print('Your choice is out of range')
    return int(choice)
# user1_pos()


## Define the player's choice
def user_placement(board, position):
    # value = 'input'
    value = 1
    rng = ['x', 'o']
    while value not in rng:
        value = input('Make your move: ')
        print('Put x or o please')
    board[position] = value
    print(board)

# user_placement(lst, 2)


##### Don't know how to set parameters for 2.


## Check if win
def check_win(board,marker):
    # for n,el in enumerate(board):
    if all(el == marker for el in board[:3]):
        print('yay1')
    elif all(el == marker for el in board[4:6]):
        print('yay2')
    elif all(el == marker for el in board[7:]):
        print('yay3')

    # for i in len(board):
    #     if board[i] == board[i+3]
    elif board[0] == board[3] and board[0] == board[6]:
        print('col1')
    elif board[1] == board[4] and board[1] == board[7]:
        print('col2')
    elif board[2] == board[5] and board[2] == board[8]:
        print('col3')
    elif board[0] == board[4] and board[0] == board[8]:
        print('diag1')
    elif board[2] == board[4] and board[2] == board[6]:
        print('diag2')
    elif ' ' not in board:
        print('tie')
        return True

# check_win(lst,'X')

## Who goes first
import random
def choose_first():
    flip = random.randint(1,2)
    print(f'User {flip} goes first')
# choose_first()

## Check if they want to continue.
def gameon():
    answer = ''
    options = ['Y', 'N']
    while answer not in options:
        answer = input('Do you want to keep playing? ')
        print('Please choose Y or N. ')
    if answer == 'Y':
        return True
    else:
        print('Ok. Come back later')
        return False
# gameon()


game_on = True

while game_on:
    board = display_board()
    choose_first()
    pos = user1_pos()
    marker = user_placement(board, pos)
    check_win(board, marker)
    gameon()