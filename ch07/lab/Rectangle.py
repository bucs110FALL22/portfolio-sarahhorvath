class Rectangle:
    def __init__(self, x, y, h, w):
      '''takes x and y coordinates, height, width, and saves them as instance variables'''
      self.x = x
      self.y = y
      self.h = h
      self.w = w
      if self.x < 0: 
        self.x = 0
      elif self.y <0: 
        self.y = 0 
      elif self.h <0: 
        self.h = 0 
      elif self.w <0: 
        self.w = 0 

    def __str__(self):
      '''returns a string containing the x, y, width, and height of rectangle'''
      result_str = f"x:{self.x}, y:{self.y}, h:{self.h}, w:{self.w}"
      return result_str
