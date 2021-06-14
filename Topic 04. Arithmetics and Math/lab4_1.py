#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import math

a = float(input('\nВведіть перше число (a)  '))
b = float(input('Введіть друге число (b), яке не дорівнює нулю  '))

x = math.sqrt(a*b)/(math.pow(math.e, a)*b) + a * math.pow(math.e, (2*a/b))

print('\nВідповідь: x = ' + str(x))