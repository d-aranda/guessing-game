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
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess not in range(1,101):
                print("Guess not in range.")
            elif guess < randomnum:
                print("Guess too low")
            elif guess > randomnum:
                print("Guess too high")
            tries = tries + 1
        except:
            print("Please enter a valid integer.")
    print(f"Congrats {name}, you got it in {tries} tries!")
    return tries
        
    
guessinggame()
