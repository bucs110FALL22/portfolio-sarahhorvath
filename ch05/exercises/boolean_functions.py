
score = 100
def percentage_to_letter(score):
  if(score >= 90):
    return "A"
  elif(80 < score < 90):
    return "B"
  elif(70 < score < 80):
    return "C"
  elif(60 < score < 70):
    return "D"
  elif(score < 60):
    return "F"


def main():
  result = percentage_to_letter(85);
  print(result)

main()
def is_passing(letter): 
  if (letter == "A"):
    return True
  elif (letter == "B"):
    return True  
  elif (letter == "C"):
    return True  
  elif (letter == "D"):
    return False  
  elif (letter == "F"):
    return False  

