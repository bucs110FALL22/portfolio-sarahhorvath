import pygame
import random
import math
pygame.init()
#window = pygame.display.set_mode()
#set_mode(size=(400, 400)
#pygame.display.get_window_size() 
screen_width=380
screen_height=380
screen=pygame.display.set_mode([screen_width, screen_height])


#WindowSize = [pygame.display.get_window_size()[0], pygame.display.get_window_size()[1]]
#print (WindowSize)
screen.fill((255,255,255))
pygame.display.flip()

x=screen_width
y=screen_height
#x = pygame.display.get_window_size()[0]
#print(x)
#y = pygame.display.get_window_size()[1]
#print(y)
color = (40,98,233)

pygame.draw.rect(screen,color,(0,0,x,y))
pygame.display.flip()

pygame.draw.circle(screen,'pink',(x/2,y/2), x/2)
pygame.display.flip()
pygame.draw.line(screen,'black',(x/2,0),(x/2,y), width=2)
pygame.display.flip()
pygame.draw.line(screen,'black',(0,y/2),(x,y/2), width=2)
pygame.display.flip()



n = 1
for _ in range(n):
  valueX = random.randrange(0, screen_width, 1)
  valueY = random.randrange(0, screen_height, 1)
  pygame.draw.circle(screen,'black',(valueX,valueY), 7)
  pygame.display.flip()
  distance_from_center = math.hypot(x-valueX, y-valueY) #the distance formula
  if distance_from_center <= screen_width/2:
    print("in the circle")





    
pygame.time.wait(10000)

#rect(window, 'blue',[(x,y),])

