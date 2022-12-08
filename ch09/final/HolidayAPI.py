import requests
import json

class HolidayAPI:

    def __init__(self, country='US', year=2021):
        self.url = f'https://holidayapi.com/v1/holidays?pretty&key=87dfcd0a-8a1a-49a3-b38d-4ef7b4bfe99a&country={country}&year={year}'
        response = requests.get(self.url)
        data = response.text
        parse_json = json.loads(data)
        names = parse_json['holidays'][0]['name']
        print(len(parse_json['holidays']))
        
        print(names)
        #names2 = parse_json(['holidays']['name'])
        #print(names['name'])
      
    def get(self):
        r = requests.get(self.url)
      
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



        #response = r.json()
        #check to make sure I got a question, i.e. results
        #if response.get('results'):
         #   return response['results']
       # else:
           # return None

   # def change_category(self, category):
      #  pass
        #self.url = #...

# key = '87dfcd0a-8a1a-49a3-b38d-4ef7b4bfe99a'
# hapi = holidayapi.v1(key)
# holidays = hapi.holidays({
#   'country': 'US',
#   'year': '2021',
# })