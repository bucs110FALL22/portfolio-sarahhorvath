import HolidayAPI 
import NumbersAPI

def main():
    '''imports the HolidaysAPI class and the Numbers API class and calls and prints the function for each'''
    hapi = HolidayAPI.HolidayAPI(country='US', year=2021)
    HolidayAPI.HolidayAPI(country='US', year=2021)
    hapi.get()
    (month, day) = hapi.returns_holiday_and_date()
    hapi.returns_favorite_month()
    print(hapi)
    napi = NumbersAPI.NumbersAPI(month, day)
    napi.get()
    print(napi)

main()