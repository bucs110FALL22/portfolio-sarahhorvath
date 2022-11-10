class StringUtility:
  def __init__(self, string):
    self.string = string
  def __str__(self):
    return str(self.string)
  def vowels(self):
    count = 0 
    vowels = 'aeiouAEIOU'
    for eachChar in self.string: 
      if eachChar in vowels: 
        count = count +1
      if count >= 5: 
        return "many"
      else: 
        return str(count)

def bothEnds(self): 
  if len(self.string) <= 2: 
    return " "
  else: 
    return str(self.string[:2] + self.string[-2:])
def fixStart(self):
    if len (self.string) <= 1: 
      return self.string 
    else: 
      firstletter = self.string[0]
      newstring = self.string.replace(firstletter, "*")
      newstring = firstletter + newstring[1:]
      return newstring 
def asciiSum(self):
  sum = 0 
  for eachChar in self.string: 
    eachChar = ord(eachChar)
    sum = sum + eachChar
  return int(sum)

def cipher(self): 
  num = len(self.string)
  newstring = ''
  for i in range(len(self.string)):
    letter = self.string[i]
    if letter.isupper():
      newstring = newstring + chr((ord(letter) + num -65) % 26 + 65)
    elif letter.islower():
      newstring = newstring +chr((ord(letter)+ num -97) % 26 +97)
    else: 
      newstring = newstring + ' '
  return newstring
  