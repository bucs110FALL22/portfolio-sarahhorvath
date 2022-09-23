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
    michelangelo.goto(-100, 20)
    y = random.randrange(0, 10)
    leonardo.forward(y)
    leonardo.goto(-100, -20)
    

window.exitonclick()

# PART B - complete part B here


pygame.init()
screen = pygame.display.set_mode()
screen.fill((255,255,255))
color = (0,255,0)

coords = []
side_length = 20
offset = 100
#equilateral triangle
num_sides = 3
m = num_sides
for i in range(m):
  theta = (2.0* math.pi * i) / (num_sides)
  x2 = side_length * math.cos(theta) + offset  
  y2 = side_length * math.sin(theta) + offset
  coords.append ((x2,y2))

pygame.draw.polygon(screen, color, coords)
pygame.display.flip()
pygame.time.wait(1000)
screen.fill((255,255,255))
pygame.display.flip()

#square (4 sides)
coords = []
num_sides = 4
m = num_sides
for i in range(m):
  theta = (2.0* math.pi * i) / (num_sides)
  x2 = side_length * math.cos(theta) + offset  
  y2 = side_length * math.sin(theta) + offset
  coords.append ((x2,y2))
  
pygame.draw.polygon(screen, color, coords)
pygame.display.flip()
pygame.time.wait(1000)
screen.fill((255,255,255))
pygame.display.flip()

#hexacon (6 sides)
coords = []
num_sides = 6
m = num_sides
for i in range(m):
  theta = (2.0* math.pi * i) / (num_sides)
  x2 = side_length * math.cos(theta) + offset  
  y2 = side_length * math.sin(theta) + offset
  coords.append ((x2,y2))

pygame.draw.polygon(screen, color, coords)
pygame.display.flip()
pygame.time.wait(1000)
screen.fill((255,255,255))
pygame.display.flip()

#nonagon (9 sides)
coords = []
num_sides = 9
m = num_sides
for i in range(m):
  theta = (2.0* math.pi * i) / (num_sides)
  x2 = side_length * math.cos(theta) + offset  
  y2 = side_length * math.sin(theta) + offset
  coords.append ((x2,y2))

pygame.draw.polygon(screen, color, coords)
pygame.display.flip()
pygame.time.wait(1000)
screen.fill((255,255,255))
pygame.display.flip()

#Circle -ish (360 sides)
coords = []
num_sides = 360
m = num_sides
for i in range(m):
  theta = (2.0* math.pi * i) / (num_sides)
  x2 = side_length * math.cos(theta) + offset  
  y2 = side_length * math.sin(theta) + offset
  coords.append ((x2,y2))

pygame.draw.polygon(screen, color, coords)
pygame.display.flip()
pygame.time.wait(1000)



