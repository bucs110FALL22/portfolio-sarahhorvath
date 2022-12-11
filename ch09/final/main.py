import HolidayAPI 
import NumbersAPI

def main():
    '''imports the HolidaysAPI class and the Numbers API class and calls the get function for each'''
    hapi = HolidayAPI.HolidayAPI(country='US', year=2021)
    (month, day) = hapi.get()
  
    napi = NumbersAPI.NumbersAPI(month, day)
    napi.get()

main()