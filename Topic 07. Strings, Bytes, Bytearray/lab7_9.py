def isHappy(inp):
    left = inp[:int(len(inp) / 2)]
    right = inp[-1:-int(len(inp) / 2) - 1:-1]
    left_sum, right_sum = 0
    for i in range(len(left)):
        left_sum += int(left[i])
        right_sum += int(right[i])
    return left_sum == right_sum


if __name__ == '__main__':
    inp = input('Введіть номер вашого квитка: ')
    if isHappy:
        print('Ваш квиток щасливий, можете загадати бажання та з\'їсти його')
    else:
        print('Ваш квиток не є щасливим!')
