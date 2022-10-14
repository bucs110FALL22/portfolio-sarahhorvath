#import random

#positiveInfinity = float('inf')

#n = random.randrange(0, positiveInfinity, 1)

#def expression(n):
import pygame
pygame.init()
pygame.font.init()

display = pygame.display.set_mode()

display.fill((255,255,255))
pygame.display.flip()


upper_limit = 101
iters = {}

#n = 101

#print(n)
#print(count)
def threenp1(n):
  count = 0
  while n != 1:
    if n % 2 == 0:
      n = n // 2
      #print(n)
      count = count +1
    else: 
      n = 3*n + 1
      #print(n)
      count = count +1
  return(count)

max_so_far = 0 
for n in range (2, upper_limit+1):
  display.fill('white')
  iters[n*5]=threenp1(n)*5
  result = threenp1(n)*5
  
  print(max_so_far)
  items = list(iters.items())
  
  print(items)
  #print(iters.items())
  if len(items) > 1:
    val = pygame.draw.lines(display, "blue", False, items)
    display.blit(pygame.transform.flip(display, False, True), (0, 0) )
    
  if result>max_so_far:
    max_so_far = result
  else:
    max_so_far = max_so_far
  
  font = pygame.font.Font(None, 42)
  
  #pygame.display.flip()
  msg = font.render('Max so far'+str(max_so_far), True, "blue")
  #display.fill((255,255,255))

  display.blit(msg,(5,5))
  pygame.display.flip()
  pygame.time.wait(100)

print(iters)

