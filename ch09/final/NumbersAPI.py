import requests
import json
import HolidayAPI

class NumbersAPI:

    def __init__(self, month, day):
        self.url = f'http://numbersapi.com/{month}/{day}/date'
        
    def get(self):
        country = 'US'
        year = 2021
        hapi = HolidayAPI.HolidayAPI(country, year)

        r = requests.get(self.url)
        response = requests.get(self.url)
        data2 = response.text
        print(data2)
        print(hapi.dayOfMonth)
