class Rectangle:
    def __init__(self, x, y, h, w):
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
        result_str = f"x:{self.x}, y:{self.y}, h:{self.h}, w:{self.w}"
        return result_str
