import requests

class NumbersAPI:

    def __init__(self, month, day):
        self.url = f'http://numbersapi.com/{month}/{day}/date'
        
    def get(self):

        r = requests.get(self.url)
        response = requests.get(self.url)
        factOfDay = response.text
        print(f"Here's a fun fact about that day: {factOfDay}")
