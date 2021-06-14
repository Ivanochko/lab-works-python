#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import math

x = float(input('\nВведіть перше число '))
nyu = float(input('Введіть друге число '))
sigma = float(input('Введіть третє число , яке не дорівнює нулю  '))

f = (1/(sigma * math.sqrt(2 * math.pi)))\
    *math.exp(-1*(math.pow((x-nyu),2))/2*math.pow(sigma,2))

print('\nВідповідь: f = ' + str(f))
