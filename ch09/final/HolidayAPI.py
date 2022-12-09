import requests
import json

class HolidayAPI:

    def __init__(self, country='US', year=2021):
        self.url = f'https://holidayapi.com/v1/holidays?pretty&key=87dfcd0a-8a1a-49a3-b38d-4ef7b4bfe99a&country={country}&year={year}'
        
    def get(self):
        r = requests.get(self.url)
        response = requests.get(self.url)
        data = response.text
        parse_json = json.loads(data)
        holidaysLength = int(len(parse_json['holidays']))
        i = 1  
        while i < holidaysLength:
          names = parse_json['holidays'][i]['name']
          print(f"{i}){names}")
          i = i +1
        j = int(input("Enter number: "))
        i = 0  
        while i < holidaysLength:
          if (i == j):
            print(parse_json['holidays'][i]['name'])
            date = parse_json['holidays'][i]['date']
            print(date)
            #return date
            break;
          i = i+1
        
        february = '02'
        january = '01'
        march = '03'
        monthes = [january, february, march]
      
        for month in monthes:
          i = 1
          #print(month)
          while i < 31:
            if date == f"2021-{month}-{i}" or date == f"2021-{month}-0{i}":
              print(f"Your favorite month is the {month} of the year.")

              break
            i = i +1
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