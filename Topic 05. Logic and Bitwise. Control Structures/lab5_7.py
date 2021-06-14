#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import time

error = '\n Таке неможливо!'
os.system('cls||clear')

print('\n* * * Загадкове пограбування * * *')

print('\nДетектив вирушив на виклик незрозумілого пограбування...')
time.sleep(2)
print('\nЗустрів першого свідка і розпитав його все, про що він знає:')

# Показання першого свідка в форматі від h1:m1 до h2:m2
h1 = int(input('\nВведіть початкову годину, яку сказав перший свідок (h1) '))
if h1 > 23 or h1 < 0:
    print(error)
    quit()
m1 = int(input('Введіть початкову хвилину, яку сказав перший свідок (m1) '))
if m1 > 59 or m1 < 0:
    print(error)
    quit()

# Перетворення показання першого свідка в формат числа
# Утворюється формат h1.m1, з плаваючою кнопною
# Так допустимо час 11:40 = числу 11.4, що дуже легко в порівняннях
time1 = h1 + m1/100

# Перетворення показань першого для виводу по формату
time1clock = str(h1) + ':' + str(m1)

h2 = int(input('Введіть кінцеву годину, яку сказав перший свідок (h2) '))
if h2 > 23 or h2 < 0:
    print(error)
    quit()
m2 = int(input('Введіть кінцеву хвилину, яку сказав перший свідок (m2) '))
if m2 > 59 or m2 < 0:
    print(error)
    quit()

time2 = h2 + m2/100
time2clock = str(h2) + ':' + str(m2)

# Якщо введене показання другого часу є меншим за перше, то міняємо їх
# Оскільки всі дії відбувались в межах одного дня
if time2 < time1:
    temp = time2
    time2 = time1
    time1 = temp
    temp = time1clock 
    time1clock = time2clock
    time2clock = temp

print('\n Детектив обробляє дані...')
time.sleep(2)

print('\n Пішов він шукати інших свідків...')
time.sleep(2)
print('\n Зустрів другого свідка, розпитав і того все, про що він знає:')

# Показання другого свідка в форматі від h3:m3 до h4:m4
h3 = int(input('\nВведіть початкову годину, яку сказав другий свідок (h3) '))
if h3 > 23 or h3 < 0:
    print(error)
    quit()
m3 = int(input('Введіть початкову хвилину, яку сказав другий свідок (m3) '))
if m3 > 59 or m3 < 0:
    print(error)
    quit()

time3 = h3 + m3/100
time3clock = str(h3) + ':' + str(m3)

h4 = int(input('Введіть кінцеву годину, яку сказав другий свідок (h4) '))
if h4 > 23 or h4 < 0:
    print(error)
    quit()
m4 = int(input('Введіть кінцеву хвилину, яку сказав другий свідок (m4) '))
if m4 > 59 or m4 < 0:
    print(error)
    quit()

time4 = h4 + m4/100
time4clock = str(h4) + ':' + str(m4)

if time4 < time3:
    temp = time4
    time4 = time3
    time3 = temp
    temp = time3clock 
    time3clock = time4clock
    time4clock = temp

# Після всіх цих перетворень получається формат показань свідків 
#                від time1 до time2 або від time3 до time4

# Формування готового виразу для виводу
timeFirstOut = ' між ' + time1clock + ' та ' + time2clock
timeSecOut = ' між ' + time3clock + ' та ' + time4clock

os.system('cls||clear')

print('\n Перший свідок стверджує, що пограбування відбулось' + timeFirstOut)
print('\n Перший свідок стверджує, що пограбування відбулось' + timeSecOut)

print('\n Детектив в роздумах...')
time.sleep(3)

if (time2 < time3) or (time4 < time1):
    print(error + ' Показання сильно розходяться в годинах!')
elif time4 == time2 and time1 == time3:
    print('\n Вони кажуть однаковий час, можливо це дійсно так,'\
        +' а може змова?')
elif time3 == time2 or time1 == time4:
    print('\n Таке можливо тільки в один і той самий момент!')
elif time1 < time3 and time2 > time4:
    print('\n Ймовірніше це сталось в той час, про який казав другий свідок:'\
        + timeSecOut)
elif time1 > time3 and time2 < time4:
    print('\n Ймовірніше це сталось в той час, про який казав перший свідок:'\
        + timeFirstOut)
elif time1 < time3 and time2 < time4:
    print('\n Найімовірніше це сталось в період між ' + time3clock + ' та '\
        + time2clock)
elif time1 > time3 and time2 > time4:
     print('\n Найімовірніше це сталось в період між ' + time1clock + ' та '\
        + time4clock)

print('\n Детектив зробив висновки, але все ж довіряти тільки 2 випадковим'\
    +' свідкам він не може!')
