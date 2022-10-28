import turtle 
#import random
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")

window = turtle.Screen ()
screenSize = 300
turtle.setup(screenSize,screenSize)
myTurtle.hideturtle()

def main():
    xCoordinate = -150
    coordinates = [xCoordinate, -screenSize, xCoordinate, screenSize]
                   #, -screenSize/2, yCoordinate, screenSize/2, yCoordinate]
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
      coordinates.extend([xCoordinate, -screenSize, xCoordinate, screenSize])
      if xCoordinate>screenSize/2:
        return
      if x+1 > len(coordinates):
        return
      
main()

def coloring(bgcolor,fillcolor): 
  window.bgcolor(bgcolor)
  turtle.fillcolor(fillcolor)
coloring("light blue", "green")

def writing(message):
  turtle.write(message, move=False, align='left', font=('Arial', 8, 'normal'))
writing("This is my lined paper!")


window.exitonclick()

