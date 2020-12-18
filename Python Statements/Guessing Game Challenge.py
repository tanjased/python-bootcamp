import random

# Machine picks number
num = random.randint(1,100)

# Automatically it evaluates as False.
guesses = [0]

# The loop runs until the following conditions are satisfied
while True:
    # First part defines 2 main conditions: the input value, if it's in the interval
    # if not asks to type another value.
    # the 2nd condition says if your choice equals to machine's choice.
    guess = int(input("Please enter a number from 1 to 100: "))
    if guess < 1 or guess > 100:
        print("You're out of bounds! Try again: ")
        continue
    elif guess == num:
        print(f"you win. Needed only {len(guesses)} guesses.")
        break

    # Here we add all the previous choices to the condition as we need to store it
    # to compare how closer the new guess is to num than the previous one.
    #
    guesses.append(guess)
    if guesses[-2]:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')

