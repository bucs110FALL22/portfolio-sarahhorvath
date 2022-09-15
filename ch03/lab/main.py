import turtle #1. import modules
import random

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
#x = random.randrange (1,100)
#print(x)
#michelangelo.forward(x)
#michelangelo.goto(-100,20)
#y = random.randrange (1,100)
#print(y)
#leonardo.forward(y)
#leonardo.goto(-100,-20)

n = 10
for _ in range(n):
    x = random.randrange(0, 10)
    michelangelo.forward(x)
    michelangelo.goto(-100, 20)
    y = random.randrange(0, 10)
    leonardo.forward(7)
    leonardo.goto(-100, -20)


# PART B - complete part B here


window.exitonclick()
