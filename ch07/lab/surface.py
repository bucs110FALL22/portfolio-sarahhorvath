from Rectangle import Rectangle 

class Surface:
  #self.rect = Rectangle(x,y,w,h)
  #self.image = None
    
  
  def __init__(self, filename, x, y, h, w):
    self.rect = Rectangle(x,y,w,h)
    self.image = filename
    # self.x = x 
    # self.y = y
    # self.h = h
    # self.w = w
    # self.image = filename
    # self.rect = Rectangle(x,y,w,h)
  def getRect(self):
    return self.rect

        

# def main():
#   rectanlgeProperties = Rectangle(2,3,4,5)

#   print(rectanlgeProperties)
# main()