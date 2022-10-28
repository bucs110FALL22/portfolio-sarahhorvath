#mood during the day 
#if below a certain level - color changes from red to green depending on where you are in the grpah 

import turtle 
#import random
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")

window = turtle.Screen ()
screenSize = 300
turtle.setup(screenSize,screenSize)
myTurtle.hideturtle()

def set_up():
    xCoordinate = -150
    yCoordinate = 0
    coordinates = [xCoordinate, -screenSize, xCoordinate, screenSize, -screenSize/2, yCoordinate, screenSize/2, yCoordinate]
    x=0
    for i in coordinates: 
      myTurtle.penup()
      y = x + 1
      myTurtle.goto((coordinates[x],coordinates[y]))
      myTurtle.pendown()
      x = x + 2
      y = y+2
      myTurtle.goto((coordinates[x],coordinates[y]))
      x = x+2
      y = y+2
      xCoordinate = xCoordinate +20
      def foo(xCoordinate, screenSize, xCoordinate, screenSize):  
        print("Choose one:",xCoordinate, -screenSize, xCoordinate, screenSize)

      #coordinates.append(xCoordinate)
      #coordinates.append(-screenSize)
      #coordinates.append(xCoordinate)
      #coordinates.append(screenSize)
      #if xCoordinate>screenSize/2:
       # return

      print(coordinates)

      if x+1 > len(coordinates):
        return
      
set_up()
window.exitonclick()

