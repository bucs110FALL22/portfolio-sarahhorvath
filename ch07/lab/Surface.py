from Rectangle import Rectangle 

class Surface:
  
  def __init__(self, filename, x, y, h, w):
    '''filename string saves to instance variables and creates rectangle objects'''
    self.rect = Rectangle(x,y,w,h)
    self.image = filename 
    
  def getRect(self):
    '''returns the rectangle object'''
    return self.rect
