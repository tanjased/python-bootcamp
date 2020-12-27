def display_board():
    lst = ['X','O','X','O','X','O','X','O','X']
    print(*lst)

    # return f'{lst[:3]}\n{lst[3:6]}\n{lst[6:]}'



lst = display_board()
# lst[2]=2
print(type(lst))


def user1_pos():
    choice = 'wrong'
    while choice.isdigit() == False or int(choice) not in range(0, 10):
        choice = input("Choose the position: ")
        if choice.isdigit() == False:
            print('Please, choose a number')
        elif int(choice) not in range(0, 10):
            print('Your choice is out of range')
    return int(choice)


# user1_pos()

def user2_pos():
    choice = 'wrong'
    while choice.isdigit() == False or int(choice) not in range(0, 10):
        choice = input("Choose the position: ")
        if choice.isdigit() == False:
            print('Please, choose a number')
        elif int(choice) not in range(0, 10):
            print('Your choice is out of range')
    return int(choice)


# pos2 = user2_pos()


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
