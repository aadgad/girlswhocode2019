
# Update this text to match your story.

start = '''
You are in a rush to get to work. It's 8:00 AM and you must be at work at 8:30 AM.

'''
print(start)
print("""
    Do you want to grab breakfast on the way or make yourself a fruit salad? Enter 'grab breakfast' or 'make fruit salad'
    """) # Update to match your story.

user_input = input()

if user_input == "grab breakfast":

    print("""
        Your are now at a Starbucks drive through. You order a tall black coffee but the barista hands you a venti triple whip caramel frappucino.
        Do you want to drink it even though your lactose intolerant or go without coffee. Enter 'drink it'or 'do not drink it'
        """)

    user_input = input()
    if user_input == "drink it":
        print("""
        The extra sugar makes you really hyper for your presentation and your boss compliments you on positive attiude and gives you a raise.
        """)
        print("""
        Now it's time to go home! Do you head to the gym or go out to dinner with friends? Enter 'gym' or 'dinner'.
        """)
        user_input = input()
        if user_input == "gym":
            print("""
            You see Zac Efron at the gym! He gets you a supporting role in his upcoming movie. Congrats!
            """)
        else:
            print("""
            You get to the restaurant and discover that they are taping 'Kitchen Nightmares'!
            It turns out that the chicken you are eating is moldy and microwaved but you get to meet Gordon Ramsay!
            """)
    else:
        print("""
            Your falling asleep during your presentation and your boss decides to implement a company wide nap time. Everyone in the office loves you.
            After work, your coworkers invite you out to a party. Do you go to the party or go home to your cats? Enter 'party' or 'cats'.
            """)
        user_input = input()
        if user_input == 'party':
            print("""
            At the party, the DJ pulls you up on stage and you improvise an original song on the spot. It reaches #1 on the charts in 4 minutes.
            You are famous!
            """)
        else:
            print("""
            You come home to discover that one of your cats is pregnant. Through the lastest DNA testing technology, you find that the father of
            the kitten is Kim Kardashian's cat, Kat Kardashian. You are now a Kardashian!
            """)

elif user_input == "make fruit salad":
    print("""
    You spent 20 minutes cutting fruits. Now your stuck in traffic a mile from your office building.
    Do you ditch your car and try to make it to your meeting on time or stay in your car until teh traffic clears up.
    Enter 'stay' or 'ditch'
    """)
    user_input = input()
    if user_input == "stay":
        print("""
        You use the time in your car to add more slides for you presentation and practice it.
        At first your boss is really mad but after your presentation everyone is moved and you get a standing ovation.
        """)
        print("""
        On the way home, you get worried that there is no more cat food in your house.
        Do you stop at the grocery store on the way or risk it and go straight home? Enter 'risk it' or 'grocery store'
        """)
        user_input = input()
        if user_input == "risk it":
            print("""
            It turns out that robbers broke into your house and stole nothing except for all the cat food.
            You are unable to feed your cat so it gives you the silent treatment for a week.
            """)
        else:
            print("""
            You go to Costco and get the 144 pack of cat food.
            You get home and realize that your fridge is broken so you have to eat cat food for dinner to make sure that it will not spoil.
            """)

    else:
        print("""
        You arrive to your meeting on time and you are really sweaty.
        Your boss is unimpressed your hygiene skills but realizes that he needs to go to gym so he postpones the meeting
        """)
        print("""
        After you clock out, you walk back to your car and discover that it has been towed! Oh no!
        Do you call the tow companyor do you hitchhike home? Enter 'tow company' or 'hitchhike'
        """)
        user_input = input()
        if user_input == "tow company":
            print("""
            The tow company mislabeled your car and they sent it to the junkyard. To make up for it, they buy you a new Ferrari! You are cool now.
            """)
        else:
            print("""
            The car that picks you up is a limo on the way to a high school prom!
            You party the night away and slow dance with the captain of the football team.
            """)
