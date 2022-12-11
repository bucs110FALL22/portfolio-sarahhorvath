import requests
import json

class HolidayAPI:

    def __init__(self, country, year):
        self.country = 'US'
        self.year = '2021'
        self.url = f'https://holidayapi.com/v1/holidays?pretty&key=87dfcd0a-8a1a-49a3-b38d-4ef7b4bfe99a&country={country}&year={year}'
        self.dayOfMonth = 0

    def get(self):
        
        requests.get(self.url)
        response = requests.get(self.url)
        data = response.text
        parse_json = json.loads(data)
        holidaysLength = int(len(parse_json['holidays']))
        holidayNumber = 1  
        print(self.dayOfMonth)
        while holidayNumber < holidaysLength:
          names = parse_json['holidays'][holidayNumber]['name']
          print(f"{holidayNumber}){names}")
          holidayNumber = holidayNumber +1
        userHolidayChoice = int(input("Enter the number of your favorite holiday: "))
        holidayNumber = 0  

        while holidayNumber < holidaysLength:
          if (holidayNumber == userHolidayChoice):
            print(parse_json['holidays'][holidayNumber]['name'])
            date = parse_json['holidays'][holidayNumber]['date']
            print(f'The date of your favorite holiday in 2021 is {date}.')
            my_month = parse_json['holidays'][holidayNumber]['date'][5:7]
            my_day = parse_json['holidays'][holidayNumber]['date'][8:10]
            # date2 = parse_json['holidays'][holidayNumber]['date'][6]
            # self.dayOfMonth = f'{date1}{date2}'
            # print(self.dayOfMonth)
            break;
          
          holidayNumber = holidayNumber+1
        
        january = '01'
        february = '02'
        march = '03'
        april = '04'
        may = '05'
        june = '06'
        july = '07'
        august = '08'
        september = '09'
        october = '10'
        november = '11'
        december = '12'
        monthes = [january, february, march, april, may, june, july, august, september, october, november, december]
        print('hello')
        for month in monthes:
          day = 1
          #print(month)
          while day < 31:
            if date == f"2021-{month}-{day}" or date == f"2021-{month}-0{day}":
              print(f"Your favorite month is the {month} of the year.")
              #print(month, day)
              #print('hello')
              #return month
              break
            day = day +1
        return (my_month, my_day)
        #return self.dayOfMonth
        #return self.dayOfMonth

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