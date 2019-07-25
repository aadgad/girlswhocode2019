import json
#create an empty dictionary
#create a list of survey questions
#loop throught ist of questions and take user inut for repsonses
#print the dictionary
allusers = []
questions = ["what is your name?", "what is your age?", "what is your favorite food?", "do you like coding?", "what is you favorite subject?"]
keys = [ "name", "age", "food", "code", "subj"]
temp = []
ans = "yes"
totalage = 0
while ans == "yes":
        user_answers = {}
        user = 1
        for q in range(len(questions)):
            if q == 0:
                name = input("what is your name?  ")
                user_answers['name'] = name
            elif q == 1:
                age = input("what is your age?  ")
                user_answers['age'] = age
                int_age = int(age)
                totalage+=int_age
            elif q == 2:
                food = input("what is your favorite food?  ")
                user_answers['favfood'] = food
            elif q == 3:
                code = input("do you like coding?  ")
                user_answers['coding'] = code
            elif q == 4:
                subj = input("what is your favorite subject?  ")
                user_answers['favsubject'] = subj
        user+=2
        allusers.append(user_answers)
        ans = input("do you want to continue playing? Enter: yes or no  ")

print (allusers)

with open("survey.json") as f:
    try:
        oldata = json.load(f)
    except ValueError:
        oldata=[]
allusers.extend(oldata)
f.close()

f = open("survey.json","w" )
json.dump(allusers, f)
f.close()

averageage = 0
averageage = totalage/user
print("the average age is :  ")
print(averageage)
