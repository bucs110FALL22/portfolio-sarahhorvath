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
    yCoordinate = -150
    coordinates = [-screenSize/2, yCoordinate, screenSize/2, yCoordinate]
    x_value_in_coordinates=0
    for i in coordinates: 
      myTurtle.penup()
      y_value_in_coordinates = x_value_in_coordinates + 1
      myTurtle.goto((coordinates[x_value_in_coordinates],coordinates[y_value_in_coordinates]))
      myTurtle.pendown()
      x_value_in_coordinates = x_value_in_coordinates + 2
      y_value_in_coordinates = y_value_in_coordinates+2
      myTurtle.goto((coordinates[x_value_in_coordinates],coordinates[y_value_in_coordinates]))
      x_value_in_coordinates = x_value_in_coordinates+2
      y_value_in_coordinates = y_value_in_coordinates+2
      yCoordinate = yCoordinate +20
      coordinates.extend([-screenSize/2, yCoordinate, screenSize/2, yCoordinate])
      if yCoordinate>screenSize/2:
        return
      if x_value_in_coordinates+1 > len(coordinates):
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

