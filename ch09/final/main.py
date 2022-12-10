import HolidayAPI 
import NumbersAPI

def main():
    #Proxy Class
    hapi = HolidayAPI.HolidayAPI(country='US', year=2021)
    hapi.get()
  
    napi = NumbersAPI.NumbersAPI(month='01', day='02')
    napi.get()

    #print(data)

    #for name in data['holidays']:
    #  print(holidays['name'])
        #combine the incorrect and corrects into a single array
       # answers = trivia['incorrect_answers'] + [trivia['correct_answer']]
        #shuffle the array for random order
        #random.shuffle(answers)
  #  for trivia in holidays:
   #   print(holidays['name'])
    #print(hapi)
    # results = hapi.get()
    # for trivia in results:
    #     #combine the incorrect and corrects into a single array
    #     answers = trivia['incorrect_answers'] + [trivia['correct_answer']]
    #     #shuffle the array for random order
    #     random.shuffle(answers)
        
    #     print(f"{trivia['question']} \n-- Please select the correct answer:\n===")
        
        #enumerate(): returns a tuple of the index and the value for each list item
        #display all possible answers
        # for i, a in enumerate(answers):
        #     print(f"{i}){a}")

        # #ask the user for their choice
        # choice = int(input(":"))
        # if answers[choice] == trivia['correct_answer']:
        #     print("correct, I guess.")
        # else:
        #     print(f"Actually, {trivia['correct_answer']}")

main()