import requests
import json

class HolidayAPI:

    def __init__(self, country, year):
        self.url = f'https://holidayapi.com/v1/holidays?pretty&key=87dfcd0a-8a1a-49a3-b38d-4ef7b4bfe99a&country={country}&year={year}'

    def get(self):
        
        requests.get(self.url)
        response = requests.get(self.url)
        data = response.text
        parse_json = json.loads(data)
        holidaysLength = int(len(parse_json['holidays']))
        holidayNumber = 1  
        print("Here is a list of holidays during the year. Read through them and type the number of your favorite holiday!")
        while holidayNumber < holidaysLength:
          names = parse_json['holidays'][holidayNumber]['name']
          print(f"{holidayNumber}){names}")
          holidayNumber = holidayNumber +1
        userHolidayChoice = int(input("Enter the number of your favorite holiday: "))
        holidayNumber = 0  

        while holidayNumber < holidaysLength:
          if (holidayNumber == userHolidayChoice):
            print(f"Your favorite holiday is {parse_json['holidays'][holidayNumber]['name']}.")
            date = parse_json['holidays'][holidayNumber]['date']
            print(f'The date of your favorite holiday in 2021 is {date}.')
            my_month = parse_json['holidays'][holidayNumber]['date'][5:7]
            my_day = parse_json['holidays'][holidayNumber]['date'][8:10]
            break;
          
          holidayNumber = holidayNumber+1

        monthes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        for month in monthes:
          day = 1
          while day < 31:
            if date == f"2021-{month}-{day}" or date == f"2021-{month}-0{day}":
              monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Septemeber', 'October', 'November', 'December']
              for monthNumber in range(0, len(monthNames)): 
                if month == monthes[monthNumber]:
                  month = monthNames[monthNumber]
              print(f"Your favorite month is {month}.")
              break
            day = day +1
        return (my_month, my_day)