import turtle #1. import modules
import random
import pygame
import math


#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
michelangelo.speed(1)
leonardo.speed(1)

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
x = random.randrange (1,100)
print(x)
michelangelo.forward(x)
y = random.randrange (1,100)
print(y)
leonardo.forward(y)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

n = 10
for _ in range(n):
    x = random.randrange(0, 10)
    michelangelo.forward(x)
    y = random.randrange(0, 10)
    leonardo.forward(7)
    
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
window.exitonclick()

# PART B - complete part B here


pygame.init()
screen = pygame.display.set_mode()
screen.fill((255,255,255))
color = (0,255,0)

coords = []
num_sides = 4
side_length = 20
offset = 100
m = num_sides
for _ in range(m):
  theta = (2.0* math.pi * m) / (num_sides)
  print (theta)
  x2 = side_length * math.cos(theta) + offset  
  y2 = side_length * math.sin(theta) + offset
  #print (x2,y2)
  coords.append ((x2,y2))
  print (coords)

#pygame.draw.polygon(screen, color,((10,20),(90,20),(50,80)))
pygame.draw.polygon(screen, color, coords)
pygame.display.flip()
pygame.time.wait(1000)
#screen.fill((255,255,255))
#color = "blue"
#pygame.draw.polygon(screen, color,((40,20),(90,20),(50,80), (40,40)))
#pygame.display.flip()
#pygame.time.wait(1000)


#equilateral triangle
#square (4 sides)
#hexacon (6 sides)
#nonagon (9 sides)
#Circle -ish (360 sides)