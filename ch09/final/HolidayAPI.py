import requests
import json

class HolidayAPI:

    def __init__(self, country, year):
        '''loads the url for the holiday API'''
        self.url = f'https://holidayapi.com/v1/holidays?pretty&key=87dfcd0a-8a1a-49a3-b38d-4ef7b4bfe99a&country={country}&year={year}'

    def get(self):
        
        requests.get(self.url)
        response = requests.get(self.url)
        data = response.text
        self.parse_json = json.loads(data)
        self.holidaysLength = int(len(self.parse_json['holidays']))
        self.holidayNumber = 1  
        print("Here is a list of holidays during the year. Read through them and type the number of your favorite holiday!")
        while self.holidayNumber < self.holidaysLength:
          names = self.parse_json['holidays'][self.holidayNumber]['name']
          print(f"{self.holidayNumber}){names}")
          self.holidayNumber = self.holidayNumber +1
        self.userHolidayChoice = int(input("Enter the number of your favorite holiday: "))
        self.holidayNumber = 0  
      
    def returns_holiday_and_date(self):
        while self.holidayNumber < self.holidaysLength:
          if (self.holidayNumber == self.userHolidayChoice):
            print(f"Your favorite holiday is {self.parse_json['holidays'][self.holidayNumber]['name']}.")
            self.date = self.parse_json['holidays'][self.holidayNumber]['date']
            print(f'The date of your favorite holiday in 2021 is {self.date}.')
            self.my_month = self.parse_json['holidays'][self.holidayNumber]['date'][5:7]
            self.my_day = self.parse_json['holidays'][self.holidayNumber]['date'][8:10]
            break;
          
          self.holidayNumber = self.holidayNumber+1
        return (self.my_month, self.my_day)
    def returns_favorite_month(self):
        monthes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        for month in monthes:
          day = 1
          while day < 31:
            if self.date == f"2021-{month}-{day}" or self.date == f"2021-{month}-0{day}":
              monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Septemeber', 'October', 'November', 'December']
              for monthNumber in range(0, len(monthNames)): 
                if month == monthes[monthNumber]:
                  month = monthNames[monthNumber]
              print(f"Your favorite month is {month}.")
              break
            day = day +1
        