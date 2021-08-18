#guessTheNumber.py
#Guess the number game

import random

secretNum = random.randint(1,21)
print("I'm thinking of a number between 1 and 20.")

#Ask player to guess 6 times
for guessesTaken in range(1,7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNum:
        print("Your guess is too low.")
    elif guess > secretNum:
        print("Your guess is too high.")
    else:
        break #This condition is the correct guess

if guess == secretNum:
    print("Good Job! You guessed the number in " +  str(guessesTaken) + " guesses!")
else:
    print("Nope, the number I was thinking of was " + str(secretNum))              
