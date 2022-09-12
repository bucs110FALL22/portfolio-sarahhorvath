import turtle 

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
print ("What is the number of sides?")
num_sides = int(input())
print ("What is the length of each side?")
length = int(input())

angle = 360/num_sides
colors = ["red"]
for c in colors:
  my_turtle.color(c)
  for i in [angle]*num_sides:
    my_turtle.forward(length)
    my_turtle.left(i)
  print ("done")

Window = turtle.Screen ()
Window.exitonclick()