import math
import sys


def input_int_check(text, minVal=0):
    var = int(input("Введіть число " + text + ": "))
    if var < minVal:
        sys.exit("Неправильне значення!")
    return var


def check_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        sys.exit("Такий трикутник не може існувати!")


def area_tringle(a, b, c):
    half = (a + b + c) / 2
    return math.sqrt(half * (half - a) * (half - b) * (half - c))


a = input_int_check("a", 1)
b = input_int_check("b", 1)
c = input_int_check("b", 1)

check_triangle(a, b, c)

print("Площа трикутника:", area_tringle(a, b, c))
