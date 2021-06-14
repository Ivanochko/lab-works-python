def toBrackets(string):
    symbols = '(){}[]<>'
    for i in string:
        if i not in symbols:
            string = string.replace(i, '')
    return string


def isGoodBrakcets(string):
    string = toBrackets(string)
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    res_str = ''
    for i in string:
        if i in brackets:
            res_str += i
            continue
        if len(res_str) > 0 and brackets[res_str[len(res_str) - 1]] == i:
            res_str = res_str[:len(res_str) - 1]
        else:
            return False
    return True if len(res_str) == 0 else False


print(isGoodBrakcets(input("Введіть текст який потрібно перевірити: ")))
