print (10 * 5, 10 ** 2, 15 / 10, 15 // 10, -15 // 10, 15 % 10, 10 % 15, 10 % 10, 0 % 10, 10 / 15)
# Mathematically, 10/15 is an infinite number. The code writes 0.6666666666666666, meaning that it ends after the 16 6's after the decimal point. 
# At some point, the computer is going to have to round. Python rounds down. 

print ("What is the current exchange rate for the Euro to Dollar?")
rate = int(input())
# use float(input()) - float instead 
print ("What is the amount of currency to exchange?")
amount = int(input())
# # use float(amount) - float instead 
total = amount * rate 
result = total - 3
#print (result)
print ("You recieved $", result, "back.")
# interupt the line of text to put variable 