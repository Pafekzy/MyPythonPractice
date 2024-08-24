import datetime

date_str = input("Enter a date (YYYY-MM-DD): ")
year, month, day = map(int, date_str.split('-'))
date = datetime.date(year, month, day)
print("Day of the week:", date.strftime("%A"))


#Day of the Week for a Given Date
