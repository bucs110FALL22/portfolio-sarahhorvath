from Rectangle import Rectangle 
from Surface import Surface

def main():
  r = Rectangle(10, 10, 10, 10)
  assert((r.x, r.y, r.h, r.w) == (10,10,10,10))
  r = Rectangle(-1, 1, 1, 1)
  assert((r.x, r.y, r.h, r.w) == (0,1,1,1))
  r = Rectangle(1, -1, 1, 1)
  assert((r.x, r.y, r.h, r.w) == (1,0,1,1))
  r = Rectangle(1, 1, -1, 1)
  assert((r.x, r.y, r.h, r.w) == (1,1,0,1))
  r = Rectangle(1, 1, 1, -1)
  assert((r.x, r.y, r.h, r.w) == (1,1,1,0))

  s = Surface("myimage.png", 10, 10, 10, 10)
  assert((s.rect.x, s.rect.y, s.rect.h, s.rect.w) == (10,10,10,10))
  srect = s.getRect()
  assert(srect.x,  s.getRect().y, srect.h,  srect.w) == (10,10,10,10)
  assert s.image
  print("Test Complete!")

main()