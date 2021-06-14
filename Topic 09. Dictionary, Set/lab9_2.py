def toNumber(number, type=1):
    ofWords = {0: '', 1: 'один', 2: 'два', 3: 'три',
               4: 'чотири', 5: 'п\'ять', 6: 'шість',
               7: 'сім', 8: 'вісім', 9: 'дев\'ять'}
    ofWordsWithValue = {0: '', 1: 'одна гривня', 2: 'дві гривні',
                        3: 'три гривні', 4: 'чотири гривні',
                        5: 'п\'ять гривень', 6: 'шість гривень',
                        7: 'сім гривень', 8: 'вісім гривень',
                        9: 'дев\'ять гривень'}
    if type == 1:
        return ofWords[int(number)]
    elif type == 2:
        return ofWordsWithValue[int(number)]


def toDecade(number, type=1):
    ofDecade = {0: '', 1: 'десять', 2: 'двадцять', 3: 'тридцять',
                4: 'сорок', 5: 'п\'ятдесят', 6: 'шістдесят',
                7: 'сімдесят', 8: 'вісімдесят', 9: 'дев\'яносто'}

    ofTen = {0: '', 1: 'одинадцять', 2: 'дванадцять', 3: 'тринадцять',
             4: 'чотирнадцять', 5: 'п\'ятнадцять', 6: 'шістнадцять',
             7: 'сімнадцять', 8: 'вісімнадцять', 9: 'дев\'ятнадцять'}
    if type == 1:
        return (ofTen[int(number - 10)]
                if int(number / 10) < 2 and number != 10
                else ofDecade[int(number / 10)])
    elif type == 2:
        return (ofTen[int(number - 10)]
                if int(number / 10) < 2 and number != 10
                else ofDecade[int(number / 10)]) + ' гривень'
    elif type == 3:
        return (ofTen[int(number - 10)]
                if int(number / 10) < 2 and number != 10
                else ofDecade[int(number / 10)]) + ' тисяч'


def toHundreds(number, type=1):
    if number == 0:
        return ''
    ofHundreds = {0: '', 1: 'сто', 2: 'двісті', 3: 'триста',
                  4: 'чотириста', 5: 'п\'ятсот', 6: 'шістсот',
                  7: 'сімсот', 8: 'вісімсот', 9: 'дев\'ятсот'}
    if type == 1:
        return ofHundreds[int(number / 100)]
    elif type == 2:
        return ofHundreds[int(number / 100)] + ' гривень'
    elif type == 3:
        return ofHundreds[int(number / 100)] + ' тисяч'


def toThousands(number):
    ofThousands = {0: '', 1: 'одна тисяча', 2: 'дві тисячі', 3: 'три тисячі',
                   4: 'чотири тисячі', 5: 'п\'ять тисяч', 6: 'шість тисяч',
                   7: 'сім тисяч', 8: 'вісім тисяч', 9: 'дев\'ять тисяч'}
    result = ''
    isTrue = True
    if number >= 100000:
        if int(number / 100000) == number / 100000:
            return toHundreds(int(number / 1000), 3)
        result += toHundreds(int(number / 1000)) + ' '
        number -= int(number / 100000) * 100000

    if number >= 10000:
        if int(number / 10000) < 2:
            result += toDecade(int(number / 1000), 3) + ' '

            number -= int(number / 10000) * 10000
        else:
            result += toDecade(int(number / 1000)) + ' '
            number -= int(number / 10000) * 10000
            result += ofThousands[(int(number / 1000))] + ' '
        isTrue = False
    if number >= 1000 and isTrue:
        result += ofThousands[int(number / 1000)] + ' '
    return result


def toCents(number):
    ofCents = {0: 'копійок', 1: 'копійка', 2: 'копійки',
               3: 'копійки', 4: 'копійки', 5: 'копійок',
               6: 'копійок', 7: 'копійок',
               8: 'копійок', 9: 'копійок'}
    cents = str(int(round(number - int(number), 2) * 100)) + ' '

    return cents + ofCents[int(str(number)[-1])]


def toTranslateNumber(number):
    if number >= 1000000:
        return ''
    cents = toCents(number)

    number = int(number)
    result = ''
    result += toThousands(number)
    number -= int(number / 100000) * 100000
    number -= int(number / 10000) * 10000
    number -= int(number / 1000) * 1000
    if number >= 100:
        if int(number / 100) == int(number) / 100:
            result += toHundreds(number, 2) + ' '
            return result + cents
        else:
            result += toHundreds(number) + ' '
            number -= int(number / 100) * 100
    if int(number) < 10:
        result += toNumber(number, 2) + ' '
    elif int(number / 10) < 2:
        result += toDecade(number, 2) + ' '
    else:
        if int(number / 10) == number / 10:
            result += toDecade(number, 2) + ' '
        else:
            result += toDecade(number) + ' '
            number -= int(number / 10) * 10
            result += toNumber(number, 2) + ' '
    return result + cents


def main():
    while True:
        number = float(input('Введіть число : '))
        print(toTranslateNumber(number).capitalize())


if __name__ == '__main__':
    main()
