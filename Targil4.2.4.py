import calendar

date = input('Enter a date: ')
day = date[-10:-8]
mounth = date[-7:-5]
year = date[-4:]
print(year)
print(mounth)
print(day)
day = calendar.weekday(int(year),int(mounth),int(day))
day_week = calendar.day_name[day]
print(day_week)