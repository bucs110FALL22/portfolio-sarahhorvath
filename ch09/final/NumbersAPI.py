import requests

class NumbersAPI:

    def __init__(self, month, day):
        '''loads the url for the Numbers API'''
        self.url = f'http://numbersapi.com/{month}/{day}/date'
        
    def get(self):
        '''loads and prints the data from the Numbers API (which is a fun fact about the day of the holiday the user chose)'''
        #r = requests.get(self.url)
        response = requests.get(self.url)
        factOfDay = response.text
        print(f"Here's a fun fact about that day: {factOfDay}")
