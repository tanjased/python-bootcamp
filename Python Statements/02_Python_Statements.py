# words start with 's'
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word.startswith('s'):
        print(word)
    else:
        pass

# print all even numbers. ODD 1 3 5 7 9
for i in range(0,11):
    if i % 2 == 0:
        print(f"That's an even number: {i}")

# numbers divisible by 3
mylist = [x for x in range(0,51) if x % 3 == 0]
print(mylist)

# length of the words is even
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(f'Length of {word} is even!')


for i in range(0,101):
    if i % 3 == 0 and i % 5 == 0 :
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('FizzBuzz')
    else:
        print(i)


# list of first letters
st = 'Create a list of the first letters of every word in this string'
flist = [x[0] for x in st.split()]
print(flist)

