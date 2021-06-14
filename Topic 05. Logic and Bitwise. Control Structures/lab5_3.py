#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from random import randint
import os

values = ['Камінь', 'Ножиці', 'Папір']

games, wins, draws, stop, loses = 0, 0, 0, 0, 0

while True:
    while True:
        os.system('cls||clear')
        print('\n////// РАУНД ' + str(games + 1) + ' \\\\\\\\\\\\')
        print('\n  * 1 - Камінь\n  * 2 - Ножиці\n  * 3 - Папір')
        choise = int(input('\nЗробіть ваш вибір: ')) - 1

        if choise > -1 and choise < 3:
            break

    print('\n Ви вибрали ' + values[choise])

    req = randint(0, 2)

    print('\n Комп\'ютер вибрав ' + values[req])

    print('\n    ' + values[choise] + ' VS ' + values[req])

    if (choise == 0 and req == 1) or (choise == 1 and req == 2) or \
        (choise == 2 and req == 0):
        print('* * * ВИ ВИГРАЛИ! * * *')
        wins += 1
    elif (choise == 1 and req == 0) or (choise == 2 and req == 1) or \
        (choise == 0 and req == 2):
        print('* * * ВИ ПРОГРАЛИ! * * *')
        loses += 1
    else:
        print('   * * * НІЧИЯ! * * *')
        draws += 1

    games += 1

    while True:
        print('\n 1 - Закінчити гру\n 2 - Дізнатись статистику\n' \
            + ' (Інше число) - Продовжити ')
        stop = int(input('\nЗробіть ваш вибір: '))
        if stop == 1:
            os.system('cls||clear')
            print('\n Дякую за гру!')
            quit()
        elif stop == 2:
            os.system('cls||clear')
            print('\n Ваша статистика:\n ' \
            + '\n  - Всього зіграно ігор: ' + str(games) \
            + '\n  - Перемог: ' + str(wins) \
            + '\n  - Нічиїх: ' + str(draws) \
            + '\n  - Поразок: ' + str(loses))
        else:
            break
