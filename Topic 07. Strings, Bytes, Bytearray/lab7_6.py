string = input('Введіть текст: ')
lenght_stars = len(string) + 4

for i in range(lenght_stars):
    print('*', end='')
print('\n*', string, '*')
for i in range(lenght_stars):
    print('*', end='')
