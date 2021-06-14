min_lenght = 128
for i in input('Введіть речення на перевірку: ').split(' '):
    if min_lenght > len(i):
        min_lenght = len(i)
print('Довжина найкоротшого слова:', min_lenght)
