#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import math

print('\nВигляд квадратного рівняння a*x^2 + b*x + c = 0')

a = float(input('\nВведіть значення a: '))
b = float(input('Введіть значення b: '))
c = float(input('Введіть значення c: '))

D = b**2 - 4 * a * c

if D == 0:
    x = -b / (2 * a)
    print('\n D = 0, розв\'язок тільки 1: x = ' + str(x))
elif D < 0:
    x1 = (-b + (math.sqrt(-D) * 1j)) / (2 * a)
    x2 = (-b - (math.sqrt(-D) * 1j)) / (2 * a)
    print('\n D < 0, в такому випадку коренями є 2 комплексні числа:')
    print('             x1 = ' + str(x1))
    print('             x2 = ' + str(x2))
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('\n D > 0, розв\'язки: '  \
          + '\n          x1 = ' + str(x1) \
          + '\n          x2 = ' + str(x2))

# Інформація про знаходження коренів рівняння:
# http://ua.onlinemschool.com/math/library/equation_quadratic/
