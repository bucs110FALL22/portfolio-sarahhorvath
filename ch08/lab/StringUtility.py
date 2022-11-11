class StringUtility:
  def __init__(self, string):
    '''takes string as a parameter'''
    self.string = string
  def __str__(self):
    '''returns the internal string itself, unchanged'''
    return str(self.string)
  def vowels(self):
    '''counts the number of vowels in the string and returns the count as a string'''
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
    '''returns a string that includes the first and last two characters of the original string'''
    if len(self.string) <= 2: 
      return ''
    else: 
      return str(self.string[:2] + self.string[-2:])
  def fixStart(self):
    '''returns a string where all occurences of its first character is changed to * excpet for the first character'''
    if len (self.string) <= 1: 
      return self.string 
    else: 
      firstletter = self.string[0]
      newstring = self.string.replace(firstletter, "*")
      newstring = firstletter + newstring[1:]
      return newstring 
  def asciiSum(self):
    '''returns an integer that is the sum of all the ascii values in the string'''
    sum = 0 
    for eachChar in self.string: 
      eachChar = ord(eachChar)
      sum = sum + eachChar
    return int(sum)

  def cipher(self): 
    '''returns a string where each character is shifted by the length of the string and depending on whether it is uppercase or lowercase'''
    num = len(self.string)
    newstring = ''
    for i in range(len(self.string)):
      letter = self.string[i]
      if letter.isupper():
        #print("Got")
        newstring = newstring + chr((ord(letter) + num - 65)% 26 +65)
      elif letter.islower():
        newstring = newstring +chr((ord(letter)+ num - 97) % 26 +97)
      else: 
        newstring = newstring + ' '
    return newstring
  