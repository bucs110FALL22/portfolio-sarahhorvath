# #mood during the day 
# #if below a certain level - color changes from red to green depending on where you are in the grpah 

import turtle 
# #import random
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")

window = turtle.Screen ()
print(turtle.screensize())

#screenSize = 300

# # def setup():
# #   coordinates = [(-100, -300), (-100, 300), (-150, 0), (150, 0)]
# #   x=0
# #   for i in coordinates: 
    
# #     myTurtle.hideturtle()
# #     myTurtle.penup()
# #     myTurtle.goto(coordinates[x])
# #     x = x + 1
# #     myTurtle.pendown()
# #     myTurtle.goto(coordinates[x])
# #     x = x + 1
# #     myTurtle.penup()
# #     if x+1 > len(coordinates):
# #       return
# #     coordinates.append(coordinates[x]*10)
# #     print (coordinates)
# # setup()
# def setup():
#   coordinates = [-100, -300, -100, 300, -150, 0, 150, 0]
#   x=0
#   for i in coordinates: 
    
#     myTurtle.hideturtle()
#     myTurtle.penup()
#     y = x + 1
#     myTurtle.goto(coordinates[x],coordinates[y])
#     print(coordinates[x],coordinates[y])
#     myTurtle.pendown()
#     x = x + 1
#     y = y+1
#     myTurtle.goto(coordinates[x],coordinates[y])
#     myTurtle.penup()
#    # if x+1 > len(coordinates):
#     #  return
#     #print(x)
#     #coordinates.append(coordinates[x]+10)
#     #print (coordinates)
# setup()


# coordinates = [-100, -300, -100, 300, -150, 0, 150, 0]
# x=0
# myTurtle.hideturtle()
# myTurtle.penup()
# y = x + 1
# myTurtle.goto((coordinates[x],coordinates[y]))
# myTurtle.pendown()
# x = x + 1
# y = y+1
# myTurtle.goto((coordinates[x],coordinates[y]))
# myTurtle.penup()
myTurtle.goto(0,0)
myTurtle.forward(200)

window.exitonclick()
