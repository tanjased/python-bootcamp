# function returns (print to visualize) the lesser of 2 given even numbers
# or the greater if some is odd

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            print(b)
        elif b > a:
            print(a)
    elif a % 2 != 0 or b % 2 != 0:
        if a > b:
            print(a)
        elif b > a:
            print(b)


# lesser_of_two_evens(2, 5)


# returns True if both words begin with the same letter
def animal_crackers(text):
    if text.split()[0][0] == text.split()[1][0]:
        print("rrright")  # instead of return true
    else:
        print("you're wrong. study more.")


# animal_crackers('Levelheaded Llama')


# instead of all these prints needs to be return True or return False
def makes_twenty(n1, n2):
    if n1 + n2 == 20:
        print("Sum is 20")
    elif n1 == 20 or n2 == 20:
        print("One of int is 20")
    else:
        print('return False')


# makes_twenty(20, 4)


def old_macdonald(name):
    name = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    print(name)


# old_macdonald('macdonald')


def master_yoda(text):
    print(" ".join(text.split()[::-1]))


# master_yoda('I am home')
# master_yoda('We are ready')


def almost_there(n):
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        print('Almost there')
    else:
        return False


# almost_there(90)
# almost_there(104)
# almost_there(150)
# almost_there(209)


def has_33(nums):
    for i in range(len(nums[:-1])):
        if nums[i] == 3:
            if nums[i - 1] == 3 or nums[i + 1] == 3:
                print(i)
        # if nums[i] == nums[i - 1] or nums[i] == nums[i + 1]:
        # print(i)


# has_33([1, 3, 3])
# has_33([1, 3, 1, 3])
# has_33([3, 1, 3])



def paper_doll(text):
    new = ''
    for i in text:
        new += i * 3
    print(new)    # prints triple values subsequently for each letter
    # Aa also works well. print() has to be outside the for loop!!

# Works well!
# def paper_doll(text):
#     print("".join([x*3 for x in text]))

# paper_doll('Hello')
# paper_doll('Mississippi')



def blackjack(a, b, c):
    if a + b + c <= 21:
        print(a + b + c)
    elif a + b + c > 21 and (a == 11 or b == 11 or c == 11):
        adj = a + b + c - 10
        if adj > 21:
            print('BUST')
        else:
            print(f'Successful adjustment. Sum is {adj}')

# blackjack(5,6,7)
# blackjack(9,9,9)
# blackjack(11,10,11)

# First define the list with ignored values, then sum the values from not ignored list
# not sure if satisfies all conditions
def summer_69(arr):
    zeros = []
    val = []
    for i in arr:
        if i in range(6, 10):
            zeros.append(i)
    # print(zeros)
        elif i not in zeros:
            val.append(i)
    print(sum(val))

# summer_69([1, 3, 5])
# summer_69([4, 5, 6, 7, 8, 9])
# summer_69([2, 1, 6, 9, 9, 11])


def spy_game(nums):
    for i, val in enumerate(nums):
        if val == 7 and nums[i-2:i] == [0,0]:
            print(f"voila {nums[i-2:i+1]}")
        elif val == 7 and nums[i-2:i] != [0,0]:
            print("Sorry, you're not cool")

    # Alternative. Version of the course. ?
    # code = [0, 0, 7, 'x']
    # for num in nums:
    #     if num == code[0]:
    #         code.pop(0)  # code.remove(num) also works
    # return len(code) == 1

# spy_game([1, 2, 4, 0, 0, 7, 5])
# spy_game([1, 0, 2, 4, 0, 5, 7])
# spy_game([1, 7, 2, 0, 4, 5, 0])


# awful. needs changes
def count_primes(num):
    prime = []
    for i in range(num+1):
        if i != 1 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            prime.append(i)
    prime[:0]=[2, 3, 5, 7]
    print(prime)
    print(len(prime))

# count_primes(100)


# def print_big(letter):
#     dict = {}
#     dict[letter] = "aaa"
#     print(dict.keys())

# for key,val in dict.items() <---  go through keys and values

def print_big(letter):      #works
    dict = {}
    a = "  *  \n * * \n*****\n*   *"
    b = "BBB"
    c = "CCC"
    for value in ['a','b','c']:
        dict[value] = eval(value)       # <--- variables have to have same names as in list
    if letter in ['a','b','c']:
        print(dict[letter])

print_big('a')

# d = {'key1':'value1','key2':'value2'}
# print(d.keys())