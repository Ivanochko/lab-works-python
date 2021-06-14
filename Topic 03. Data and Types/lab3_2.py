#! usr/bin/env python3
# -*- coding: utf-8 -*-

print("\n     1 - з Цельсію в Фаренгейт")
print("     2 - з Фаренгейта в Цельсій")

choose = int(input(" Виберіть перевід: "))
if choose == 1:
    temp = input("Введіть значення градусів: ")
    temp_perevid = int(temp) * 1.8 + 32
    print("\n  "+temp+"°C = "+str(round(temp_perevid, 3))+"°F")
elif choose == 2:
    temp = input("Введіть значення градусів: ")
    temp_perevid = (int(temp) - 32) / 1.8
    print("\n  "+temp+"°F = "+str(round(temp_perevid, 3))+"°C")
else:
    print("Значення введено неправильно!")
