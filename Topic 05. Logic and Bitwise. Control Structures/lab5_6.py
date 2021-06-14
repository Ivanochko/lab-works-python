#! /usr/bin/env python3
# -*- coding:utf-8 -*-

error = '\nТаке значення неможливе в трикутнику!'

a = float(input('\nВведіть значення a: '))
if a <= 0:
    print(error)
    quit()
b = float(input('Введіть значення b: '))
if b <= 0:
    print(error)
    quit()
c = float(input('Введіть значення c: '))
if c <= 0:
    print(error)
    quit()

if ((a + b) > c) and ((b + c) > a) and ((c + a) > b):
    print('\nТрикутник з такими сторонами може існувати!')
else:
    print('\nІснування трикутника з такими сторонами неможливе!')
