#imports the ability to get a random number (we will learn more about this later!)

from random import *
#Generates a random integer.
aRandomNumber = randint(1, 20)
print(aRandomNumber)
# For Testing: print(aRandomNumber)

trys = 0
for trys in range (2):
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
        print("That's not a positive whole number, try again!")

    else:
         guess = int(guess) # converts a string to an integer

    if guess == aRandomNumber:
        print("That is the correct answer")
        break

    elif guess !=  aRandomNumber:
        trys-=1

        if(guess>aRandomNumber):
            print("Guess lower")

        else:
            print ("Guess higher")
