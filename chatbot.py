
from random import *
import random

def intro(name):
    print("Hi, " +name+ " I am chatbot!")
    #name = input("What is your name? ")
    print("Would you like to play a game of guess the word or guess the number?")

def process_input(ans):
    if ans == "guess the number":
        guessthenumbergame()
    elif ans == "guess the word":
        guesstheletter()

def guesstheletter():
    potential_words = ["hydrogen", "atom", "solution", "chemical", "reactions", "acid", "base"]
    word = random.choice(potential_words)
    #print(word)
    # Converts the word to lowercase
    word = word.lower()
    current_word = ["___", "___"]
    # Make it a list of letters for someone to guess
    numofletters=0
    for letter in word:
        letters_word = letter
        print(letters_word)
        numofletters+=1
    #print(numofletters)
    for i in range(numofletters-2):
        current_word.append('___')
    print(current_word)
         # TIP: the number of letters should match the word
    guesses = []
    maxfails = numofletters +3
    fails = 0
    cguess =0
    while fails < maxfails:
        guess = input("\n Guess a letter: *Hint...the words are chemistry")
        guesses.append(guess)
        #print(guesses)
        itir = 0

        for let in word:
            if guess == let:
                current_word[itir]= guess
                cguess += 1
            itir+=1
        if cguess == len(word):
            print("YAY YOU GOT IT!!!")
            break
        if not guess.isalpha():
            print("This is not a letter. Guess again!")
        #elif guess.length
    	# check if the guess is valid: Is it one letter? Have they already guessed it?
    	# check if the guess is correct: Is it in the word? If so, reveal the letters!
        print(current_word)
        fails = fails+1
        print("You have " + str(maxfails - fails) + " tries left!")
def guessthenumbergame():
    aRandomNumber = randint(1, 20)
    #print(aRandomNumber)
    trys=3
    while trys>0:
        guess = int(input("Guess a number between 1 and 20 (inclusive):   you only get THREE trys"))
        if guess !=  aRandomNumber:
             trys-=1
             if(guess>aRandomNumber):
                 print("Guess lower")
             else:
                 print ("Guess higher")
        elif guess == aRandomNumber:
            trys =0
            print("That is the correct answer")

def main():
    while True:
        name = input("What is your name?")
        intro(name)
        ans = input ("Enter: 'guess the number' or 'guess the word' ")
        process_input(ans)

if __name__ == "__main__":
    main()
