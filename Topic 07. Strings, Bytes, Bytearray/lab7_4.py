def coding(string):
    string_out = ''
    for index, value in enumerate(string):
        string_out += chr(ord(value) + 1)
    return string_out


def decoding(string):
    string_out = ''
    for index, value in enumerate(string):
        string_out += chr(ord(value) - 1)
    return string_out


thing = int(input(
    'Що бажаєте зробити?'
    '\n (1) - закодувати текст'
    '\n (2) - розкодувати текст \n'))

if thing == 1:
    print('Результат: \n', coding(input('Введіть текст для кодування: ')))
elif thing == 2:
    print('Результат: \n', decoding(input('Введіть текст для кодування: ')))
else:
    print('Неправильний ввід!')
