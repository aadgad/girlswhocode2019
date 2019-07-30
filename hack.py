#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:

f = open("dictionary.txt","r")



print("Can your password survive a dictionary attack?")



#Take input from the keyboard, storing in the variable test_password

#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords

test_password = input("Type in a trial password: ")
newpass = test_password.strip()
newpass2 = newpass.lower()

for item in f:
    newitem = item.strip()
    if newitem == newpass2:
        print("You're password is too weak.")

turnoff = False

f = open("dictionary.txt","r")
for w1 in f:
    strip_w1 = w1.strip()
    f = open("dictionary.txt","r")
    for w2 in f:
        strip_w2 = w2.strip()
        compd = strip_w1 + strip_w2
        #print(compd)
        if newpass2 == compd:
            print("You're password is too weak")
            turnoff = True
            break
    if turnoff:
        break





#Write logic to see if the password is in the dictionary file below here:
