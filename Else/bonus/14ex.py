from datetime import datetime

date1 = list(map(int, input("""Введіть першу дату
    (в форматі yyyy, mm, dd)    """).split(', ')))
if date1[0] < 2000:
    print("Неправильно введений рік! ")
    quit()
if date1[1] < 1 or date1[1] > 12:
    print("Неправильно введений місяць! ")
    quit()
if date1[2] < 1 or date1[2] > 31:
    print("Неправильно введений день")
date2 = list(map(int, input("""Введіть другу дату
    (в форматі yyyy, mm, dd)    """).split(', ')))
if date2[0] < 2000:
    print("Неправильно введений рік! ")
    quit()
if date2[1] < 1 or date2[1] > 12:
    print("Неправильно введений місяць! ")
    quit()
if date2[2] < 1 or date2[2] > 31:
    print("Неправильно введений день")

riznucya = date2[2] - date1[2] + (date2[1] - date1[1]) * 30\
 + (date2[0] - date1[0]) * 365

print("Різниця введених дат " + str(riznucya) + " днів")
