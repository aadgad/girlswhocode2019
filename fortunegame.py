
# Update this text to match your story.

start = '''
You are in a rush to get to work. It's 8:00 AM and you must be at work at 8:30 AM.

'''
print(start)
print("Do you want to grab breakfast on the way or make yourself a fruit salad? Enter 'grab breakfast' or 'make fruit salad'") # Update to match your story.

user_input = input()

if user_input == "grab breakfast":

    print("""Your are now at a Starbucks drive through. You order a tall black coffee but the barista hands you a venti triple whip caramel frappucino.
    Do you want to drink it even though your lactose intolerant or go without coffee. Enter 'drink it'or 'do not drink it'""")

    user_input = input()
    if user_input == "drink it":
        print("The extra sugar makes you really hyper for your presentation and your boss compliments you on positive attiude and gives you a raise.")
    else:
        print("Your falling asleep during your presentation and your boss decides to implement a company wide nap time. Everyone in the office loves you.")


elif user_input == "make fruit salad":
    print("""You spent 20 minutes cutting fruits. Now your stuck in traffic a mile from your office building.
    Do you ditch your car and try to make it to your meeting on time or stay in your car until teh traffic clears up.
    Enter 'stay' or 'ditch' """)
    user_input = input()
    if user_input == "stay":
        print(""" You use the time in your car to add more slides for you presentation and practice it.
        At first your boss is really mad but after your presentatin everyone is moved and you get a standing ovation.""")

    else:
        print("""You arrive to your meeting on time and you are really sweaty.
         Your boss is unimpressed your hygiene skills but realizes that he needs to go to gym so he postpones the meeting. """)
