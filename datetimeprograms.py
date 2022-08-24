# from datetime import date, timedelta
# dt = date.today() - timedelta(5)
# print(timedelta(5))
# print('current date :',date.today())
# print('5 days before current date:',dt)
#
# import datetime
# today = datetime.date.today()
# yesterday = today - datetime.timedelta(days = 1)
# tomorrow = today + datetime.timedelta(days = 1)
# print('yesterday : ',today)
# print('today : ',today)
# print('tomorrow : ',tomorrow)
# from datetime import date, timedelta
# def all_sundays(year):
#     dt = date(year,1,1)
#     dt += timedelta(days=6 - dt.weekday())
#     while dt.year == year:
#         yield dt
#         dt += timedelta(days=7)
#
# for s in all_sundays(2020):
#     print(s)

from datetime import date
a = date(2000,2,28)
b = date(2001,2,28)
print(b-a)