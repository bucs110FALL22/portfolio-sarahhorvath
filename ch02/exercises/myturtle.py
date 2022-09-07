import turtle 
my_turtle = turtle.Turtle()
#my_turtle.forward (50) 
my_turtle.shape("turtle")
my_turtle.color("purple")
num_sides = 4
length = 50 
angle = 360/num_sides

for i in [angle]*num_sides:
  my_turtle.forward(length)
  my_turtle.left(i)
print ("done")
my_turtle.color("red")
my_turtle.left(180)
my_turtle.penup ()
my_turtle.forward (length)
my_turtle.pendown ()

for i in [angle]*num_sides:
  my_turtle.forward(length)
  my_turtle.left(i)
print ("done")

Window = turtle.Screen ()
Window.exitonclick()