from Rectangle import Rectangle 

class Surface:
  
  def __init__(self, filename, x, y, h, w):
    self.rect = Rectangle(x,y,w,h)
    self.image = filename 
    
  def getRect(self):
    
    return self.rect
