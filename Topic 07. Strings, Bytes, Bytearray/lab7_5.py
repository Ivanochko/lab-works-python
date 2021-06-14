def toLetters(string):
    symbols = ' .,!?/\\"\':;<>(){}[]-'
    for x in symbols:
        string = string.replace(x, '')
    return string


def numberVowels(string):
    string = string.lower()
    vovels_letters = 'aouiey'
    number = 0
    for i in string:
        if i in vovels_letters:
            number += 1
    return number


def numberConsonants(string):
    string = toLetters(string.lower())
    vovels_letters = 'aouiey'
    number = 0
    for i in string:
        if i not in vovels_letters:
            number += 1
    return number


string = input('Введіть текст для підрахунку кількості:   ')
print('   * Кількість голосних літер:', numberVowels(string))
print('   * Кількість приголосних літер:', numberConsonants(string))
