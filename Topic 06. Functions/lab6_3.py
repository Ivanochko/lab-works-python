import sys


def input_float(text="число", minVal=0):
    var = float(input("Введіть " + text + ": "))
    if var < minVal:
        sys.exit("Неправильне значення!")
    return var


def deposit(start_sum, one_year_proc, final_sum):
    years = 0
    while (start_sum < final_sum):
        start_sum += start_sum * (one_year_proc / 100)
        years += 1
    return years


start_sum = input_float("початкову суму")
final_sum = input_float("кінцеву суму")
year_proc = input_float("річну відсоткову ставку (%)")

years = deposit(start_sum, year_proc, final_sum)

print("")
print("Потрібно:", years, "years для отримання потрібної суми")
