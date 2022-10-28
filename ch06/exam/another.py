import turtle 
#import random
window = turtle.Screen ()


def coloring(bgcolor,fillcolor): 
  window.bgcolor(bgcolor)
  turtle.fillcolor(fillcolor)

def writing(message):
  turtle.write(message, move=False, align='left', font=('Arial', 8, 'normal'))

def get_spacing(screenSize, number_of_lines):
  return screenSize/number_of_lines

def main():
  myTurtle = turtle.Turtle()
  myTurtle.shape("turtle")

  screenSize = 300
  turtle.setup(screenSize,screenSize)
  myTurtle.hideturtle()
  xCoordinate = -150
  yCoordinate = -150
  coordinates = [-screenSize/2, yCoordinate, screenSize/2, yCoordinate]
  x_value_in_coordinates=0
  space = get_spacing(screenSize,10)
  print(space)
  for i in coordinates: 
    #move before pen down - put in loop 
    myTurtle.penup()
    y_value_in_coordinates = x_value_in_coordinates + 1
    myTurtle.goto((coordinates[x_value_in_coordinates],coordinates[y_value_in_coordinates]))
    myTurtle.pendown()
    x_value_in_coordinates = x_value_in_coordinates + 2
    y_value_in_coordinates = y_value_in_coordinates+2
    myTurtle.goto((coordinates[x_value_in_coordinates],coordinates[y_value_in_coordinates]))
    x_value_in_coordinates = x_value_in_coordinates+2
    y_value_in_coordinates = y_value_in_coordinates+2
    yCoordinate = yCoordinate +space
    coordinates.extend([-screenSize/2, yCoordinate, screenSize/2, yCoordinate])
    
    if yCoordinate>screenSize/2:
      break
    if x_value_in_coordinates+1 > len(coordinates):
      break
  coloring("light blue", "green")
  writing("This is my lined paper!")

main()


window.exitonclick()

# 