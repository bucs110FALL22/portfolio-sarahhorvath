import requests
import json
import HolidayAPI

class NumbersAPI:

    def __init__(self, month, day):
        self.url = f'http://numbersapi.com/{month}/{day}/date'
        
    def get(self):
        hapi = HolidayAPI.HolidayAPI(year=2021)
        #data = hapi.get(date)
        r = requests.get(self.url)
        response = requests.get(self.url)
        data2 = response.text
        print(data2)
       # print(hapi.dayOfMonth)
        #parse_json = json.loads(data)
       # holidaysLength = int(len(parse_json['holidays']))
        
        #response is just a json dictonary of values after .json() call
       # holidays = r.json()
        #check to make sure I got a question, i.e. results
        #print(r.text)
        #if response.get('results'):
         #   return response['results']
        #else:
          #  return None
        #r = requests.get(self.url)
        #print(self.url)
        #response is just a json dictonary of values after .json() call
       # print(r.text)
      
        # holidays = hapi.holidays({
        #   'country': 'US',
        #   'year': '2021',
        # })
        # print(holidays)
