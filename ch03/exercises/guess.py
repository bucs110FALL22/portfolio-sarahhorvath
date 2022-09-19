import random

my_list = range(1, 11, 1)
print(list(my_list))

randomNumber = random.choice(my_list)
print(randomNumber)
num_guesses = 0
correctGuess = False 
#print ("You have three guesses to guess the number between 1-10, inclusive. What is the number?")

n = 3
for i in range(n):
  if not correctGuess:
    print("What is the number?")
    numberGuessed = int(input())
    num_guesses = num_guesses +1
    if numberGuessed < randomNumber:
        print("Too Low")
    elif numberGuessed > randomNumber:
        print("Too High")
    else:
        print("correct!")
        correctGuess = True
        print ("Took you", num_guesses, "guesses to get it right.")
     

#Using nested if statements and a loop, give the user 3 chances to guess the number.
#If the guess is too low, print the message “Too Low”
#If the guess is too high, print the message “Too High”
#If the guess is right, print the message “correct!”
#What if the user guesses right on the first try? How can we stop the loop?
#There are many different approaches to this, most of which we have not yet covered in the course, so there is not a correct answer here. Any approach is valid.
