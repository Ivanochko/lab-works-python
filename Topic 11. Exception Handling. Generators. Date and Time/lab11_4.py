#! usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
amount_days_in_month = {1: 31, 2: 28, 3: 31, 4: 30,
                        5: 31, 6: 30, 7: 31, 8: 31,
                        9: 30, 10: 31, 11: 30, 12: 31}
names_month = {1: 'Січень', 2: 'Лютий', 3: 'Березень',
               4: 'Квітень', 5: 'Травень', 6: 'Червень',
               7: 'Липень', 8: 'Серпень', 9: 'Вересень',
               10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'}
names_days = {1: 'Понеділок', 2: 'Вівторок', 3: 'Середа',
              4: 'Четвер', 5: "П'ятниця", 6: 'Субота',
              7: 'Неділя'}


def check_input(max_value, min_value):
    good_input = False
    while not good_input:
        try:
            inp = int(input())
        except ValueError:
            print('Це повинно бути числом!')
            print('Повторіть! ')
            continue
        else:
            if inp > max_value:
                print('Число завелике!')
                continue
            elif inp < min_value:
                print('Число замале!')
                continue
            return inp


def input_first():
    print('Введіть місяць першої дати: ')
    print(' Січень - 1, Грудень - 12')
    month_first = check_input(12, 1)
    print('Введіть число першої дати: ')
    date_first = check_input(amount_days_in_month[month_first], 1)
    print('Введіть день тижня першої дати: ')
    print(' Понеділок - 1, Неділя - 7')
    day_first = check_input(7, 1)
    return [month_first, date_first, day_first]


def input_second():
    print('Введіть місяць другої дати:')
    print(' Січень - 1, Грудень - 12')
    month_second = check_input(12, 1)
    print('Введіть число другої дати:')
    date_second = check_input(amount_days_in_month[month_second], 1)
    return [month_second, date_second]


def get_second_day():
    first_dates = input_first()
    second_dates = input_second()

    current_day = first_dates[2]

    first_date = datetime.date(2002, first_dates[0], first_dates[1])
    second_date = datetime.date(2002, second_dates[0], second_dates[1])
    if first_date < second_date:

        while first_date != second_date:
            current_day += 1
            if current_day == 8:
                current_day = 1

            if first_dates[1] == amount_days_in_month[first_dates[0]]:
                first_dates[1] = 1
                first_dates[0] += 1
            else:
                first_dates[1] += 1

            first_date = datetime.date(2002, first_dates[0], first_dates[1])

    elif second_date < first_date:

        while first_date != second_date:
            current_day -= 1
            if current_day == 0:
                current_day = 7

            if first_dates[1] == 1:
                first_dates[0] -= 1
                first_dates[1] = amount_days_in_month[first_dates[0]]
            else:
                first_dates[1] -= 1

            first_date = datetime.date(2002, first_dates[0], first_dates[1])
    else:
        print('Дати однакові')
    return names_days[current_day]


def main():
    print('\nДень тижня вказаної другої дати:', get_second_day())


if __name__ == '__main__':
    main()
