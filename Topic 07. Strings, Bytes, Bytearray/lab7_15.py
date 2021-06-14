from random import randint

required = 'abcdefghijklmnopqrstuvwxyz123456789' +\
           '0ABCDEFGHIJKLMNOPQRSTUVWXYZ.-_@#&*()'
password = ''
while True:
    while True:
        password += required[randint(0, len(required) - 1)]
        if len(password) > 8 and randint(0, 1) or len(password) == 17:
            break
    print(password)
    input('\nНатисніть ENTER, щоб згенерувати інший пароль\n')
    password = ''
