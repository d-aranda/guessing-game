"""A number-guessing game."""

# Put your code here

import random


def guessinggame():
    print("Hi!")
    name = input("Whats your name?: ")
    randomnum = random.randint(1,100)
    guess = 0
    tries = 0
    while randomnum != guess:
        guess = int(input("Guess a number between 1 and 100: "))
        tries = tries + 1 
        if guess < randomnum:
            print("Guess too low")
        elif guess > randomnum:
            print("Guess too high")
        else: 
            print(f"Congrats, you got it in {tries} tries!")
        
        
    
guessinggame()
