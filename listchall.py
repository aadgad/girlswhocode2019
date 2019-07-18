#imports the ability to get a random number (we will learn more about this later!)

from random import *

#Create the list of words you want to choose from.

sides = ["baked potato", "garden salad", "fries", "mashed potatoes", "green brean", "roasted veggies", "asparaus", "dinner roll", "soup", "garlic bread"]
maincourse = ["steak", "pasta", "salmon fillet", "chicken parm", "avocado sandwich", "shrimp and broccoli stir fry", "garlic noodles", "spaghetti", "fajitas", "fish tacos"]
dessert = ["pizookie","creme brulee","chocolate mint bar","pecan pie","cheesecake ","chocolate cake","triple scoop sundae","lemon tart","vanilla pudding","cinnamon roll"]


#Generates a random integer.

randside = randint(0, len(sides)-1)
randmaincourse = randint(0, len(maincourse)-1)
randdessert = randint(0, len(dessert)-1)

make list of all teh ages
make a for loop that will go through the eter list and add teh numbers to an empty variable
take that variable and divide it by teh len of the list
