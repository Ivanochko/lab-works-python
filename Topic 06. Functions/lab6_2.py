import sys


def input_int(text="число", minVal=0):
    var = int(input("Введіть " + text + ": "))
    if var < minVal:
        sys.exit("Неправильне значення!")
    return var


def deposit(start_sum, one_year_proc, years_to_deposit):
    for i in range(0, years_to_deposit):
        start_sum += start_sum * (one_year_proc / 100)
    return start_sum


start_sum = input_int("початкову суму")
year_proc = input_int("річну відсоткову ставку (%)")
years = input_int("кількість років")

print("")
print("Сума після закінчення депозиту:", deposit(start_sum, year_proc, years))
