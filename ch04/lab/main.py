import pygame
pygame.init()
window = pygame.display.set_mode()
pygame.display.get_window_size() 


WindowSize = [pygame.display.get_window_size()[0], pygame.display.get_window_size()[1]]
print (WindowSize)
window.fill((255,255,255))
pygame.display.flip()

x = pygame.display.get_window_size()[0]
print(x)
y = pygame.display.get_window_size()[1]
print(y)
color = (40,98,233)

pygame.draw.rect(window,color,(0,0,x,y))
pygame.display.flip()

pygame.draw.circle(window,'pink',(x/2,y/2), x/2)
pygame.display.flip()
pygame.draw.line(window,'black',(x/2,0),(y,x/2), width=2)
pygame.draw.line(window,'black',(0,y/2),(y,y/2), width=2)
pygame.display.flip()

pygame.time.wait(100000)

#rect(window, 'blue',[(x,y),])

