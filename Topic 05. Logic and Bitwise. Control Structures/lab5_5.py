#! /usr/bin/env python3
# -*- coding:utf-8 -*-

number = int(input('\nВведіть число, яке треба перевірити: '))

i = 1

while i < number:
    if number % i == 0 and not(i == 1) and not(i == number):
        print('\nЦе число не є простим! ')
        break
    i += 1
else:
    print('\nЦе просте число! ')
