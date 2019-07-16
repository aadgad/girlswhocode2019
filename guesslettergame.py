

import random

potential_words = ["nuclear", "fission", "fussion", "titrate", "reactions", "acid", "base"]
word = random.choice(potential_words)
print(word)
# Converts the word to lowercase
word = word.lower()
current_word = ["___", "___"]

# Make it a list of letters for someone to guess
numofletters=0
for letter in word:
    letters_word = letter
    print(letters_word)
    numofletters+=1

print(numofletters)

for i in range(numofletters-2):
    current_word.append('___')
print(current_word)
     # TIP: the number of letters should match the word
guesses = []
maxfails = numofletters +3
fails = 0
cguess =0
while fails < maxfails:
    guess = input("\n Guess a letter: ")
    guesses.append(guess)
    #print(guesses)

    itir = 0


    for let in word:
        if guess == let:
            current_word[itir]= guess
            cguess += 1
            print(cguess)
        itir+=1
    if cguess == len(word):
        print("Yay, you guessed the word!!")
        break
    #print(current_word)



	# check if the guess is valid: Is it one letter? Have they already guessed it?
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
    print(current_word)
    fails = fails+1
    print("You have " + str(maxfails - fails) + " tries left!")
