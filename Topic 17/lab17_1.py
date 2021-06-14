#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest
from lab9_1 import toCountScore

"""
Юніт тест до лабораторної номер 9.1
Перевід номіналу карт для гри BlackJack
"""

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(toCountScore('TK'), 20)

    def test_2(self):
        self.assertEqual(toCountScore('A35'), 18)

    def test_3(self):
        self.assertEqual(toCountScore('QJ'), 20)

    def test_4(self):
        self.assertEqual(toCountScore('44322'), 15)

    def test_5(self):
        self.assertEqual(toCountScore('Q562'), 23)

    def test_6(self):
        self.assertEqual(toCountScore('TTTT'), 40)

    def test_7(self):
        self.assertEqual(toCountScore('AKQJT98765432'), 94)

    def test_8(self):
        self.assertEqual(toCountScore('2'), 2)

    def test_9(self):
        self.assertEqual(toCountScore('3'), 3)

    def test_10(self):
        self.assertEqual(toCountScore('4'), 4)

    def test_11(self):
        self.assertEqual(toCountScore('5'), 5)

    def test_12(self):
        self.assertEqual(toCountScore('6'), 6)

    def test_13(self):
        self.assertEqual(toCountScore('7'), 7)

    def test_14(self):
        self.assertEqual(toCountScore('8'), 8)

    def test_15(self):
        self.assertEqual(toCountScore('9'), 9)

    def test_16(self):
        self.assertEqual(toCountScore('A'), 10)

    def test_17(self):
        self.assertEqual(toCountScore('K'), 10)

    def test_18(self):
        self.assertEqual(toCountScore('Q'), 10)

    def test_19(self):
        self.assertEqual(toCountScore('J'), 10)

    def test_20(self):
        self.assertEqual(toCountScore('TA'), 20)


if __name__ == '__main__':
    unittest.main()
