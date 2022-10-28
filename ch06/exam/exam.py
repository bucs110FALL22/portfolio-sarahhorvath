#mood during the day 
#if below a certain level - color changes from red to green depending on where you are in the grpah 

import turtle 
#import random
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")

window = turtle.Screen ()
screenSize = 300
turtle.setup(screenSize,screenSize)

# def setup():
#   coordinates = [(-100, -300), (-100, 300), (-150, 0), (150, 0)]
#   x=0
#   for i in coordinates: 
    
#     myTurtle.hideturtle()
#     myTurtle.penup()
#     myTurtle.goto(coordinates[x])
#     x = x + 1
#     myTurtle.pendown()
#     myTurtle.goto(coordinates[x])
#     x = x + 1
#     myTurtle.penup()
#     if x+1 > len(coordinates):
#       return
#     coordinates.append(coordinates[x]*10)
#     print (coordinates)
# setup()
def set_up():
  coordinates = [-100, -300, -100, 300, -150, 0, 150, 0, -1]
  x=0
 # y = 0 
  for i in coordinates: 
    myTurtle.penup()
    myTurtle.hideturtle()
    x=0
    y = x + 1
    myTurtle.goto((coordinates[0],coordinates[1]))
    print(coordinates[x],coordinates[y])
    myTurtle.pendown()
    x = x + 2
    y = y+2
    myTurtle.goto((coordinates[2],coordinates[3]))
    myTurtle.pendown()

    #myTurtle.penup()
    if x+1 > len(coordinates):
      return
    #print(x)
    #coordinates.append(coordinates[x]+10)
    #print (coordinates)
set_up()
#myTurtle.goto(0,0)
#myTurtle.speed(0)
def foo(a, b, c, d):  
    print("Choose one:",a,b,c,d)

foo("Great","Good","Meh", "Bad")


# def mood():
  # result = input("How was your day?")
  # print(result)
  # if result == "Great" or result == "great":
  #   print("yessss")
  #   for i in range (0, screenSize):
  #     myTurtle.goto(-100, 10)
  #     myTurtle.pendown()
  #     myTurtle.goto(-100,50)
  #     myTurtle.penup()
  # elif result == "Good" or result == "good":
  #   print("yessss")
  # elif result == "Meh" or result == "meh":
  #   print("yessss")
  # elif result == "Bad" or result == "bad":
  #   print("hi")
#
 
    




# mood()




window.exitonclick()
