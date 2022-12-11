import requests

class NumbersAPI:

    def __init__(self, month, day):
        '''loads the url for the Numbers API'''
        self.url = f'http://numbersapi.com/{month}/{day}/date'
        
    def get(self):
        '''loads the data from the Numbers API (which is a fun fact about the day of the holiday the user chose)'''
        response = requests.get(self.url)
        self.factOfDay = response.text
        
    def __str__(self):
      '''returns the string of the fun fact'''
      information_str = f"Here's a fun fact about that day: {self.factOfDay}"
      return information_str