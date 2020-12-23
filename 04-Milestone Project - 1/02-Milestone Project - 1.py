def display_list(lst):
    return(f'{lst[:3]}\n{lst[3:6]}\n{lst[6:]}')

lst = display_list([' ']*9)

def user1_pos():
    choice = 'wrong'
    while choice.isdigit() == False or int(choice) not in range(0,10):
        choice = input("Choose the position: ")
        if choice.isdigit() == False:
            print('Please, choose a number')
        elif int(choice) not in range(0,10):
            print('Your choice is out of range')
    return(int(choice))
# user1_pos()

def user2_pos():
    choice = 'wrong'
    while choice.isdigit() == False or int(choice) not in range(0,10):
        choice = input("Choose the position: ")
        if choice.isdigit() == False:
            print('Please, choose a number')
        elif int(choice) not in range(0,10):
            print('Your choice is out of range')
    return(int(choice))
# user2_pos()

def user1_placement(lst,position):
    value = input('Make your move: ')
    while False:
        if value != 'x' or value != 'o':
            print('Put x or o please')

    lst[position] = value
    return(lst)
user1_placement(lst,2)

