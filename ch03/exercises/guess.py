import random

my_list = range(1, 11, 1)
print(list(my_list))

randomNumber = random.choice(my_list)
print(randomNumber)
#print ("You have three guesses to guess the number between 1-10, inclusive. What is the number?")

n = 3
for _ in range(n):
    print("What is the number?")
    numberGuessed = int(input())
    if numberGuessed == randomNumber:
        print("correct")
    elif numberGuessed > randomNumber:
        print("Too High")
    else:
        print("Too Low")

#Using nested if statements and a loop, give the user 3 chances to guess the number.
#If the guess is too low, print the message “Too Low”
#If the guess is too high, print the message “Too High”
#If the guess is right, print the message “correct!”
#What if the user guesses right on the first try? How can we stop the loop?
#There are many different approaches to this, most of which we have not yet covered in the course, so there is not a correct answer here. Any approach is valid.
