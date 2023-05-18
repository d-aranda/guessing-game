"""A number-guessing game."""

# Put your code here

import random


def guessinggame():
    print("Hi!")
    name = input("Whats your name?: ")
    randomnum = random.randint(1,100)
    guess = 0
    while randomnum != guess:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < randomnum:
            print("Guess too low")
        elif guess > randomnum:
            print("Guess too high")
    
guessinggame()