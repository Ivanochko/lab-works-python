#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import math
import decimal

doxid = decimal.Decimal(input('\nВведіть місячний дохід: '))

physPod = doxid * decimal.Decimal('0.18')
viyskPod = doxid * decimal.Decimal('0.015')

summ = decimal.Decimal(physPod) + decimal.Decimal(viyskPod)

print('\n Ваш місячний дохід:  ' + str(doxid))
print('З цього :     податок:  ' + str(physPod))
print('      військовий збір:  ' + str(viyskPod))
print('                 СУМА:  ' + str(summ))
print('                          Залишок:   ' + str(doxid-summ))
