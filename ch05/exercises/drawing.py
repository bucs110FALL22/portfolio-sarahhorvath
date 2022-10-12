import turtle 
import pygame 
pygame.init()

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")
window = turtle.Screen ()

color = "green"
coords = [(0,0), (4,3)]
pygame.draw.polygon(window, color, coords)
pygame.display.flip()

window.exitonclick()