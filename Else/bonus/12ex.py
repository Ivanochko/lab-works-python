import calendar

year = int(input("Введіть потрібний рік:( >2000 )  "))
if year < 2000:
    print("Неправильний ввід!")
    quit()
month = int(input("Введіть потрібний місяць: "))
if month < 1 or month > 12:
    print("Неправильний ввід!")
    quit()

cal = calendar.TextCalendar(calendar.MONDAY)
str = cal.formatmonth(year, month)
print("\n" + str)
