def toText(string):
    symbols = '(){}[]<>*/+-=:;^\\&|.,%'
    for i in string:
        if i in symbols:
            string = string.replace(i, ' ')
    return string


def findWords(string):
    string_ = toText(string)
    array = string_.split(' ')
    keys = ['print', 'if', 'in', 'input', 'for', 'while',
            'else', 'elif', 'def', 'return']

    # видалення ключових слів, порожніх елементів та чисел
    array = [i for i in array
             if i not in keys and i != '' and not i.isdigit()]
    # видалення дублікатів з масиву
    return list(set(array))


def toSnakeWord(string):
    temp = string.split('_')
    res = temp[0]
    for i in range(1, len(temp)):
        res += temp[i].capitalize()
    return res


def toSnakeString(string):
    array = findWords(string)
    array = [i for i in array if '_' in i]

    for i in range(len(array)):
        string = string.replace(array[i], toSnakeWord(array[i]))
    return string


def toCamelWord(string):
    res = ''
    for i, value in enumerate(string):
        if value.isupper() and i != 0:
            res = string[:i] + '_' + string[i].lower() + string[i + 1:]
    return res


def toCamelString(string):
    array = findWords(string)
    array = [i for i in array if '_' not in i]

    for i in range(len(array)):
        string = string.replace(array[i], toCamelWord(array[i]))
    return string


if __name__ == '__main__':
    string = ('print([res_square ** 2 for res_square'
              ' in input_array if res_square > 18 ])')

    print(' * * input:')
    print(string)
    string = toSnakeString(string)
    print('\n * * SnakeStyle: ')
    print(string)
    string = toCamelString(string)
    print('\n * * Camel_style: ')
    print(string)
