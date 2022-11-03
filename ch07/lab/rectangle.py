class Rectangle:
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w

    def __str__(self):
        result_str = f"x:{self.x}, y:{self.y}, h:{self.h}, w:{self.w}"
        return result_str

# def main():
#     rectanlgeProperties = Rectangle(2,3,4,5)

#     print(rectanlgeProperties)
# main()