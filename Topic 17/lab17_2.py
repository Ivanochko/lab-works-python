#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import timeit
import math
import operator


def stage_shift(number):
    return number << 1


def stage_stars(number):
    return number ** 2


def stage_power(number):
    return pow(number, 2)


def stage_math(number):
    return math.pow(number, 2)


def stage_magic(number):
    return operator.__pow__(number, 2)


def reverse_str(string):
    return string[::-1]


def for_use(list_of_strs):
    for i in range(len(list_of_strs)):
        list_of_strs[i] = reverse_str(list_of_strs[i])


def map_use(list_of_strs):
    return map(reverse_str, list_of_strs)


def compr_use(list_of_strs):
    return [reverse_str(i) for i in list_of_strs]


if __name__ == '__main__':
    print('\n--------------FIRST----------------')

    print('  *   Shift:')
    print(min(timeit.repeat('stage_shift(2)',
                            setup='from __main__ import stage_shift',
                            repeat=3, number=1000)))

    print('  *   Stars:')
    print(min(timeit.repeat('stage_stars(2)',
                            setup='from __main__ import stage_stars',
                            repeat=3, number=1000)))

    print('  *   pow:')
    print(min(timeit.repeat('stage_power(2)',
                            setup='from __main__ import stage_power',
                            repeat=3, number=1000)))

    print('  *   math.pow:')
    print(min(timeit.repeat('stage_math(2)',
                            setup='from __main__ import stage_math',
                            repeat=3, number=1000)))

    print('  *   operator:')
    print(min(timeit.repeat('stage_magic(2)',
                            setup='from __main__ import stage_magic',
                            repeat=3, number=1000)))

    print('\n--------------SECOND---------------')

    print('  *   for loop:')
    print(min(timeit.repeat("for_use(['qwerty', 'abcdef', '123', 'python'])",
                            setup='from __main__ import for_use',
                            repeat=3, number=1000)))

    print('  *   map:')
    print(min(timeit.repeat("map_use(['qwerty', 'abcdef', '123', 'python'])",
                            setup='from __main__ import map_use',
                            repeat=3, number=1000)))

    print('  *   list coprehension:')
    print(min(timeit.repeat("compr_use(['qwerty', 'abcdef', '123', 'python'])",
                            setup='from __main__ import compr_use',
                            repeat=3, number=1000)))
