import calendar

date_str = input("Please enter a date in this format [dd/mm/yyyy] please: ")
day = int(date_str[:2])
month = int(date_str[3:5])
year = int(date_str[6:])

day_num = calendar.weekday(year, month, day)
day_name = calendar.day_name[day_num]

print(day_name)