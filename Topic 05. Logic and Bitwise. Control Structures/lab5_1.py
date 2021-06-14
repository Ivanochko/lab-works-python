#! /usr/bin/env python3
# -*- coding:utf-8 -*-

number = int(input('\n Введіть число, яке хочете перевірити:   '))
if number <= 0:
    print('\nЧисло введено неправильно!!!')
else:
    if (((number) & (number-1)) == 0):
    	print('\nЧисло ' + str(number) + ' є степенем двійки!')
    	i = 0
    	while (2**i) < (number+1):
    		if (2**i) == number:
    			print('Ця степінь: ' + str(i))
    		i += 1;
    else:
    	print('\nЧисло ' + str(number) + ' не є степенем двійки!')
