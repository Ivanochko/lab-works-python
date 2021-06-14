def removeLetter(string, letter):
    index = string.index(letter)
    return string[:index] + string[index + 1:] if index != len(string) else ''


def isInclude(text1, text2):
    for i in text1:
        if i in text2:
            text2 = removeLetter(text2, i)
        else:
            return False
    return True


if __name__ == '__main__':

    inp_one = input('Введіть перше речення: ')
    inp_two = input('Введіть друге речення: ')
    if inp_one == inp_two:
        print('Ці речення однакові!')
    elif isInclude(inp_one, inp_two):
        print('Перше речення входить в друге!')
    elif isInclude(inp_two, inp_one):
        print('Друге речення входить в перше!')
    else:
        print('Речення не входять одне в одне!')
