import turtle 
import random
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_list = range(1, 100, 1)
my_turtle.goto(0,0)
my_turtle.speed(0)
window = turtle.Screen ()

distance = 10
angle = 90
is_in_screen = True

colors = ["green", "blue", "purple"]

while is_in_screen: 
    coin = random.randrange(0, 2)
    if coin == 0:           # heads
        my_turtle.left(angle)
    else:                      # tails
        my_turtle.right(angle)
    my_turtle.forward(distance)

    turtleX = my_turtle.xcor()
    turtleY = my_turtle.ycor()

    x_range = window.window_width()/2
    y_range = window.window_height()/2
    
    my_turtle.color(colors[0])
    colors.append(colors.pop(0))
    if abs(turtleX) > x_range or abs(turtleY) > y_range:
        is_in_screen = False



window.exitonclick()



  

