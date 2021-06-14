#! usr/bin/env python3
# -*- coding: utf-8 -*-
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to_point(self, point):
        _ = math.pow(point.x - self.x, 2) + math.pow(point.y - self.y, 2)
        return math.sqrt(_)

    def dist_to_coords(self, x, y):
        _ = math.pow(x - self.x, 2) + math.pow(y - self.y, 2)
        return math.sqrt(_)


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.a = Point(x1, y1)
        self.b = Point(x2, y2)
        self.c = Point(x3, y3)

    def is_exist_check(self):
        _a = self.a.dist_to_point(self.b) + self.a.dist_to_point(self.c)
        _b = self.b.dist_to_point(self.a) + self.b.dist_to_point(self.c)
        _c = self.c.dist_to_point(self.a) + self.c.dist_to_point(self.b)
        if _a > self.b.dist_to_point(self.c)\
           and _b > self.a.dist_to_point(self.c)\
           and _c > self.a.dist_to_point(self.b):
            return True
        else:
            return False

    def is_exist_print(self):
        print('\nЯ можу існувати!'
              if self.is_exist_check()
              else '\nЯ не можу існувати!')

    def find_perimetr(self):
        if self.is_exist_check():
            _a = self.a.dist_to_point(self.b)
            _b = self.b.dist_to_point(self.c)
            _c = self.c.dist_to_point(self.a)
            return _a + _b + _c
        else:
            return 0

    def find_area(self):
        if self.is_exist_check():
            x1 = self.a.x
            x2 = self.b.x
            x3 = self.c.x
            y1 = self.a.y
            y2 = self.b.y
            y3 = self.c.y
            _ = ((y1 + y3) / 2) * (x3 - x1)
            _ += ((y3 + y2) / 2) * (x2 - x3)
            _ -= ((y1 + y2) / 2) * (x2 - x1)
            return _
        else:
            return 0


def check_input():
    while True:
        try:
            inp = int(input())
        except ValueError:
            print('Це повинно бути числом!')
            print('Повторіть! ')
            continue
        else:
            return inp


def input_coords():
    print('Введіть координату х1: ')
    x1 = check_input()
    print('Введіть координату y1: ')
    y1 = check_input()
    print('Введіть координату х2: ')
    x2 = check_input()
    print('Введіть координату y2: ')
    y2 = check_input()
    print('Введіть координату х3: ')
    x3 = check_input()
    print('Введіть координату y3: ')
    y3 = check_input()
    return (x1, y1, x2, y2, x3, y3)


def main():
    c = input_coords()
    t = Triangle(c[0], c[1], c[2], c[3], c[4], c[5])
    t.is_exist_print()
    print('Периметр: ', round(t.find_perimetr(), 5))
    print('   Площа: ', round(t.find_area(), 5))


if __name__ == '__main__':
    main()
