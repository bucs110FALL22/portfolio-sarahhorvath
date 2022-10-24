
class Player:
	def __init__(self):
    self.speed = 10
    self.outfits = 3 #change costumes
    self.is_moving = True  

class Background:
  def __init__(back):
      back.color = "blue"
      back.day = 3 # background color can change depending on what time of day it is 
      back.numberofclouds = 2 # how many clouds the background creats

class Bricks:
  def __init__(brick):
      brick.on = False
      brick.rect = pygame.Rect(0, 0, 25, 25)
      brick.position = (0,0)