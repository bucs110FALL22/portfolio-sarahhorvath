#Write a function called, star_pyramid(), that asks the user for the number of rows and then prints the following pattern, with the number of rows corresponding to the input value. In other words, if the input is 5, print a star triangle with 5 rows, the last row containing 5 stars (as seen below). If the input is 6, the last row should contain 6 stars, etc.:
#hint: a for loop and str multiplication can make this a very simple algorithm

print ("How many stars?")
numberStars = int(input())
statement = "*"
y = 1
n = numberStars
for _ in range(n):
  print(statement*y)
  y = y + 1

print ("How many stars (backwards)?")
numberStars = int(input())
statement = "*"
n = numberStars
for _ in range(n):
  print(statement*numberStars)
  numberStars = numberStars - 1