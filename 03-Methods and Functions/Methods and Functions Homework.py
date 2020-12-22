### Compute volume
import math

# def vol(rad):
#     print(4/3 * math.pi * rad**3)
#     # return 4/3 * math.pi * rad**3

## As lambda expression
# vol = lambda rad: print(4/3 * math.pi * rad**3)
# vol(2)


# def ran_check(num,low,high):
#    if num in range(low,high + 1):
#        print(f'{num} is in the range between {low} and {high}.')
#    else:
#        print(f'{num} is out of the range.')
#
# ran_check(5, 2, 7)


## With booleans
# def ran_bool(num,low,high):
#     if num in range(low,high + 1):
#         return True
#     else:
#         return False
# print(ran_bool(3, 1, 10))


### Calculate the number of uppercase and lowercase. Or in solution a dict can be used instead!
# (dictionary with 2 keys: "upper" and "lower")
# def up_low(s):
#     up = ''
#     low = ''
#     for letter in s:
#         if letter.isupper():
#             up += letter
#         elif letter.islower():
#             low += letter
#     print(len(up),len(low))
#
# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# up_low(s)


### Unique variables in the list
# def unique_list(lst):
#     uniq = []
#     for num in lst:
#         if num not in uniq:
#             uniq.append(num)
#     print(uniq)

# ?? try filter and lambda
# uniq = []
# lst = [1,1,1,1,2,2,3,3,3,3,4,5]
# print([uniq.append(num) for num in lst if num not in uniq])

# Using set() which returns only unique values
# def unique_list(lst):
#     newset = set(lst)
#     unique = list(newset)
#     print(unique)
# unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

# using numpy unique
# Error installing numpy !!!
# import numpy as np
# def unique_list(lst):
#     arr = np.array(lst)
#     print(np.unique(arr))
# unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

# The easiest way
# def multiply(numbers):
#     res = 1
#     for num in numbers:
#         res = res*num
#     print(res)
# multiply([1, 2, 3, -4])

# using reduce function
# from functools import reduce
# lst = [1, 2, 3, -4]
# res = reduce((lambda x, y: x * y), lst)
# print(res)


# def palindrome(s):
#     s = s.replace(' ', '')
#     return s == s[::-1]
#
# print(palindrome('helleh'))

# Check if every letter is in a string
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(' ', '')
    newset = set(str1.lower())
    alphabet = set(alphabet)
    subset = newset.issubset(alphabet) # or intersection could be used. issuperset() - the opposite
    intersect = newset.intersection(alphabet)
    if len(intersect) == len(alphabet):
        print("Entire alphabet is in the string.")
    else:
        print("The alphabet is not presented in this string.")

ispangram("The quick brown fox jumps over the lazy dog")

