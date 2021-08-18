#guess the number auto
import random

secretNumber = random.randint(1,1000)
print("Looking for secret number...")

guess = 0
for guessesTaken in range(1,950):
    print("guessing number")
    guess = random.randint(1, 1000)
    
    print("I'm guessing: " + str(guess))
    if guess < secretNumber:
        print("Guess was too low, trying again.")
    elif guess > secretNumber:
        print("Guess was too high, trying again.")
    else:
        break

if guess == secretNumber:
    print("Aha! The number is " + str(secretNumber) + ", It only took me " + str(guessesTaken) + " guesses!")
else:
    print("I could not find the number, you win.")
    print("***SECRET NUMBER WAS: " + str(secretNumber) + "***")
    
