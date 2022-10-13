import turtle 
Window = turtle.Screen ()


def drawEqShape(num_sides,length):
  my_turtle = turtle.Turtle()
  my_turtle.shape("turtle")
  my_turtle.color("green")

  print ("What is the number of sides?")
  num_sides = int(input())
  print ("What is the length of each side?")
  length = int(input())

  angle = 360/num_sides
  




  for i in [angle]*num_sides:
      my_turtle.forward(length)
      my_turtle.left(i)
  print ("done")

Window.exitonclick()