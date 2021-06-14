#! usr/bin/env python3
# -*- coding: utf-8 -*-
def is_even(number):
    return number % 2 == 0


def main():
    stop = False
    while not stop:
        try:
            number = int(input(' * *  Введіть число: '))
        except ValueError:
            print('Це мусить бути числом!')
            print('Спробуйте знову!')
        else:
            print('Yes!' if is_even(number) else 'No!')
        finally:
            print("\nНатисніть Enter, щоб перевірити ще раз")
            print('або будь-який символ, щоб завершити роботу!')
            stop = input()
    print("\nДякую за роботу!")


if __name__ == '__main__':
    main()
