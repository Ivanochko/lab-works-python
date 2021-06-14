#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# Розміри дверей
dWidth = 60
dHeight = 200

# Масив для збереження розмірів коробки
boxInset = [False, False]

print('\nРозмір дверей: ' + str(dHeight) + 'x' + str(dWidth))
A = float(input('\nВведіть висоту коробки (в см):  '))
if A <= 0:
    print('Дані введено неправильно!')
    quit()
elif A < dWidth:
    boxInset[0] = True
elif A < dHeight:
    boxInset[1] = True

B = float(input('\nВведіть ширину коробки (в см):  '))
if B <= 0:
    print('Дані введено неправильно!')
    quit()
elif B < dWidth and not(boxInset[0]):
    boxInset[0] = True
elif B < dHeight:
    boxInset[1] = True

C = float(input('\nВведіть довжину коробки (в см):  '))
if C <= 0:
    print('Дані введено неправильно!')
    quit()
elif C < dWidth and not(boxInset[0]):
    boxInset[0] = True
elif C < dHeight:
    boxInset[1] = True

if boxInset[0] and boxInset[1]:
    print('\nКоробка влізеться в двері розміром ' + str(dHeight)\
          + 'x' + str(dWidth) + ' см')
else:
    print('\nКоробка не влізеться в двері розміром ' + str(dHeight)\
          + 'x' + str(dWidth) + ' см')
