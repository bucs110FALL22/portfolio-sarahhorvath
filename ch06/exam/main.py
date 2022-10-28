import turtle 
window = turtle.Screen ()
myTurtle = turtle.Turtle()
SCREEN_SIZE = 300

def coloring(bgcolor,fillcolor): 
  window.bgcolor(bgcolor)
  turtle.fillcolor(fillcolor)

def writing(message):
  turtle.write(message, move=False, align='left', font=('Arial', 8, 'normal'))

def get_spacing(SCREEN_SIZE, number_of_lines):
  return SCREEN_SIZE/number_of_lines
def drawing_lines(yCoordinate):
    coordinates = [-SCREEN_SIZE/2, yCoordinate, SCREEN_SIZE/2, yCoordinate]
    x_value_in_coordinates=0
    space = get_spacing(SCREEN_SIZE,10)
    for i in coordinates: 
      myTurtle.penup()
      for i in (0,SCREEN_SIZE/2):
        y_value_in_coordinates = x_value_in_coordinates + 1
        myTurtle.goto((coordinates[x_value_in_coordinates],coordinates[y_value_in_coordinates]))
        myTurtle.pendown()
        x_value_in_coordinates = x_value_in_coordinates + 2
        y_value_in_coordinates = y_value_in_coordinates+2
      yCoordinate = yCoordinate +space
      coordinates.extend([-SCREEN_SIZE/2, yCoordinate, SCREEN_SIZE/2, yCoordinate])
      if yCoordinate>SCREEN_SIZE/2:
        break
      if x_value_in_coordinates+1 > len(coordinates):
        break
def main():
  turtle.setup(SCREEN_SIZE,SCREEN_SIZE)
  myTurtle.shape("turtle")
  myTurtle.hideturtle()
  drawing_lines(-150)
  coloring("light blue", "green")
  writing("This is my lined paper!")
main()


window.exitonclick()