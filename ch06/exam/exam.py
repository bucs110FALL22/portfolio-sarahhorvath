#mood during the day 
#if below a certain level - color changes from red to green depending on where you are in the grpah 
# 

import turtle 


myTurtle = turtle.Turtle()
myTurtle.shape("turtle")

window = turtle.Screen ()
turtle.setup(300,300)

coordinates = [(-100, -300), (-100, 300), (-150,-300), (-150,0)]
x=0
for i in coordinates: 
  myTurtle.hideturtle()
  myTurtle.penup()
  myTurtle.goto(coordinates[x])
  x = x + 1
  myTurtle.pendown()
  myTurtle.goto(coordinates[x])
  

#def setup():

  # make list with coordinates 
#  coordinates 
 # x = (-100, -300)
 # y = (-100, 300)




#myTurtle.goto(0,0)
#myTurtle.speed(0)
#setup()
def foo(a, b, c, d):  
    print(a,b,c,d)

foo("Great","Good","Meh", "Bad")


def mood():
  result = input("How was your day?")
  print(result)
  if result == "Great" or result == "great":
    print("yessss")
  elif result == "Good" or result == "good":
    print("yessss")
  elif result == "Meh" or result == "meh":
    print("yessss")
  elif result == "Bad" or result == "bad":
    print("hi")
mood()
window.exitonclick()
