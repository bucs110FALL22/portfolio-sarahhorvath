#import random

#positiveInfinity = float('inf')

#n = random.randrange(0, positiveInfinity, 1)

#def expression(n):
upper_limit = 20
iters = []

count = 0
n = 101

print(n)
print(count)

numbers = range (2, upper_limit)
for number in numbers:
  while n != 1:
    if n % 2 == 0:
      n = n // 2
      print(n)
      count = count +1
    else: 
      n = 3*n + 1
      print(n)
      count = count +1
  iters.append(n)
  iters.append(":")
  iters.append(count)


  print(iters)
#he wrote 42 lines of code