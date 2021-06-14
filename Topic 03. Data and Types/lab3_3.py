#! usr/bin/env python3
# -*- coding: utf-8 -*-

rist = input('\nВведіть ваш зріст ( в метрах ): ')
mass = input('\nВведіть вашу вагу ( в кілограмах ): ')

# Якщо введений ріст не в метрах, а в сантиметрах
if float(rist) > 3:
    rist = float(rist) / 100.0

index = float(mass) / (float(rist)**2)

print ('\n Індекс маси вашого тіла: ' + str(round(index, 2)))
