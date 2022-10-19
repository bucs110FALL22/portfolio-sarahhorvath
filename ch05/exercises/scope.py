# Write the following functions:
# Write a function that multiplies two numbers together using a loop and accumulator (no multiplication) and return the resulting value


# Write a function that takes a number and exponent as parameters and raises the number to the exponent and return the resulting value (no exponentiation)


# Write another function, called square, that takes a single parameter and squares it by only calling your multiplication function and return the resulting value
# Test your code by calling each function with whatever value you choose, then printing their results, i.e. the return value.

def multiply(num2):
  result = 3            
  result = result*num2
  return result
  
def exponent(num1):
  result = 2            
  result = result**num1
  return result
  
def square(num):
  result = 0            
  for i in range(num):
    result = result + num
  return result

def main():
  print(multiply(3))
  print(exponent(3))
  print(square(5))
main()