import turtle 
import random
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_list = range(1, 100, 1)
my_turtle.goto(0,0)

randomNumber = random.choice(my_list)

n = 1
for _ in range(n):
    my_turtle.forward(randomNumber)
    my_turtle.left(randomNumber)
    my_turtle.forward(randomNumber)
    my_turtle.right(randomNumber)



Window = turtle.Screen ()
Window.exitonclick()