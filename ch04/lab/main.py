import pygame
import random
import math
pygame.init()

screen_width=380
screen_height=380
screen=pygame.display.set_mode([screen_width, screen_height])

screen.fill((255,255,255))
pygame.display.flip()

x=screen_width
y=screen_height

color = (40,98,233)

pygame.draw.rect(screen,color,(0,0,x,y))
pygame.display.flip()

pygame.draw.circle(screen,'pink',(x/2,y/2), x/2)
pygame.display.flip()
pygame.draw.line(screen,'black',(x/2,0),(x/2,y), width=2)
pygame.display.flip()
pygame.draw.line(screen,'black',(0,y/2),(x,y/2), width=2)
pygame.display.flip()



n = 10
for _ in range(n):
  valueX = random.randrange(0, screen_width, 1)
  valueY = random.randrange(0, screen_height, 1)
  pygame.draw.circle(screen,'black',(valueX,valueY), 7)
  pygame.display.flip()
  distance_from_center = math.hypot(x/2-valueX, y/2-valueY) #the distance formula
  if distance_from_center <= ((screen_width)/2):
      pygame.draw.circle(screen,'green',(valueX,valueY), 7)
      pygame.display.flip()
pygame.time.wait(1000)

screen.fill((255,255,255))
pygame.display.flip()

color = (40,98,233)

pygame.draw.rect(screen,color,(0,0,x,y))
pygame.display.flip()

pygame.draw.circle(screen,'pink',(x/2,y/2), x/2)
pygame.display.flip()
pygame.draw.line(screen,'black',(x/2,0),(x/2,y), width=2)
pygame.display.flip()
pygame.draw.line(screen,'black',(0,y/2),(x,y/2), width=2)
pygame.display.flip()

redX = 350
redY = 10
redSize = 30
pygame.draw.rect(screen,"red",(redX,redY,redSize,redSize))
pygame.display.flip()
blueX = 0
blueY = 10
blueSize = 30
pygame.draw.rect(screen,"blue",(blueX,blueY,blueSize,blueSize))
pygame.display.flip()




#input("Please choose either the red or blue box to select which player will win the game of darts.")

#distance_from_redBox = math.hypot(redX-pygame.mouse.get_pos()[0], redY- pygame.mouse.get_pos()[1]) #the distance formula
#if distance_from_redBox <= (redSize):
    #print("You chooe: red box")

#distance_from_blueBox = math.hypot(blueX-pygame.mouse.get_pos()[0], blueY- pygame.mouse.get_pos()[1]) #the distance formula
#if distance_from_blueBox <= (blueSize):
   # print("You chose: blue box")



pygame.event.get()
#print (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

# a > redBox.x[0] & a < redBox.x[1] & b  

team = 0 # 0 not chosen, 1 is player1, 2

while (team == 0):
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      mouseX = pygame.mouse.get_pos()[0]
      mouseY = pygame.mouse.get_pos()[1]
     # print(mouseX, mouseY)
     # if mouseX >= redX & mouseX < (redX + redSize) & mouseY < redY+redSize:
      #  teamChosen = 1
      #  break
     # if mouseX>= blueX & mouseX< (blueX + blueSize) & mouseY > blueY: 
      #  teamChosen = 2
      #  break
      if mouseX > 350:
        team = 1
        break
      if mouseX < 40:
        
        team = 2
       
        break

#print(team)



n = 10
redScore = 0
blueScore = 0
for _ in range(n):
  valueX = random.randrange(0, screen_width, 1)
  valueY = random.randrange(0, screen_height, 1)
  pygame.draw.circle(screen,(255,139,139),(valueX,valueY), 7)
  pygame.display.flip()
  distance_from_center = math.hypot(x/2-valueX, y/2-valueY) #the distance formula
  if distance_from_center <= ((screen_width)/2):
      pygame.draw.circle(screen,'red',(valueX,valueY), 7)
      pygame.display.flip()
      redScore = redScore + 1
  pygame.time.wait(1000)
  valueX = random.randrange(0, screen_width, 1)
  valueY = random.randrange(0, screen_height, 1)
  pygame.draw.circle(screen,(0,247,255),(valueX,valueY), 7)
  pygame.display.flip()
  distance_from_center = math.hypot(x/2-valueX, y/2-valueY) #the distance formula
  if distance_from_center <= ((screen_width)/2):
      pygame.draw.circle(screen,'blue',(valueX,valueY), 7)
      pygame.display.flip()
      blueScore = blueScore + 1

#print(redScore)
#print(blueScore)
if blueScore>redScore: 
  print("Blue wins!")
if redScore>blueScore: 
  print("Red wins!")
if redScore==blueScore: 
  print("Tie!")

if (redScore>blueScore) & (team == 1): 
  print("you guessed right!")
if (blueScore>redScore) &(team == 2): 
  print("you guessed right!")

if (redScore>blueScore) & (team == 2): 
  print("you guessed wrong.")
if (blueScore>redScore) &(team == 1): 
  print("you guessed wrong.")
  
pygame.time.wait(1000)
pygame.time.wait(1000)
