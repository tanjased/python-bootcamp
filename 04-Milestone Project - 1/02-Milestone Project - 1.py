## First step is to display the game board
def display_board():
    # lst = ['']*9
    lst = ['X','O','X','O','O','O','X','O','X']
    # print(*lst)
    # print(f'{lst[:3]}\n{lst[3:6]}\n{lst[6:]}'
    return lst    # Had problem with displaying on a few lines


lst = display_board()
# print(lst)

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

check_win(lst,'O')


## Check if they want to continue.
def gameon():
    answer = ''
    options = ['Y', 'N']
    while answer not in options:
        answer = input('Do you want to keep playing? ')
        print('Please choose Y or N. ')
    if answer == 'Y':
        return True
    elif answer == 'N':
        print('Ok. Come back later')
# gameon()