def translateToRome(number):
    romeNumbers = {1: 'I', 5: 'V', 10: 'X',
                   50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    if number <= 0 or number > 3999:
        return 'Bad value'
    result = ''
    while number != 0:
        if number >= 900:
            if number >= 1000:
                result += romeNumbers[1000]
                number -= 1000
            elif number >= 998:
                result += romeNumbers[1]
                number += 1
            elif number >= 995:
                result += romeNumbers[5]
                number += 5
            elif number >= 980:
                result += romeNumbers[10]
                number += 10
            elif number >= 950:
                result += romeNumbers[50]
                number += 50
            else:
                result += romeNumbers[100]
                number += 100
        elif number >= 400:
            if number >= 500:
                result += romeNumbers[500]
                number -= 500
            elif number >= 498:
                result += romeNumbers[1]
                number += 1
            elif number >= 495:
                result += romeNumbers[5]
                number += 5
            elif number >= 480:
                result += romeNumbers[10]
                number += 10
            elif number >= 450:
                result += romeNumbers[50]
                number += 50
            else:
                result += romeNumbers[100]
                number += 100
        elif number >= 90:
            if number >= 100:
                result += romeNumbers[100]
                number -= 100
            elif number >= 98:
                result += romeNumbers[1]
                number += 1
            elif number >= 95:
                result += romeNumbers[5]
                number += 5
            else:
                result += romeNumbers[10]
                number += 10
        elif number >= 40:
            if number >= 50:
                result += romeNumbers[50]
                number -= 50
            elif number >= 48:
                result += romeNumbers[1]
                number += 1
            elif number >= 45:
                result += romeNumbers[5]
                number += 5
            else:
                result += romeNumbers[10]
                number += 10
        elif number >= 9:
            if number >= 10:
                result += romeNumbers[10]
                number -= 10
            else:
                result += romeNumbers[1]
                number += 1
        elif number >= 4:
            if number >= 5:
                result += romeNumbers[5]
                number -= 5
            else:
                result += romeNumbers[1]
                number += 1
        else:
            while number != 0:
                result += romeNumbers[1]
                number -= 1
    else:
        return result


def translateToArabian(string):
    romeString = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result, temp, count = 0, 0, 0
    if len(string) == 1:
        return romeString[string[0]]
    if string[0] > string[1]:
        result += romeString[string[0]]
    else:
        count += 1
        temp += romeString[string[0]]
    for i in range(1, len(string) - 1):
        if romeString[string[i]] > romeString[string[i + 1]]:
            result += romeString[string[i]]
            if temp != 0:
                if romeString[string[i]] > romeString[string[i - 1]]:
                    result -= temp
                elif romeString[string[i]] <= romeString[string[i - 1]]:
                    result += temp
                temp, count = 0, 0
        else:
            count += 1
            if count > 2:
                return -1
            temp += romeString[string[i]]
    if temp != 0:
        if romeString[string[-1]] > romeString[string[-2]]:
            return result - temp + romeString[string[-1]]
        else:
            return result + temp + romeString[string[-1]]
    else:
        return result + romeString[string[-1]]


def main():
    choose = 1
    while choose == 1 or choose == 2:
        print('\n(1) - перевести в римську систему числення')
        print('(2) - перевести в арабську систему числення')
        choose = int(input())
        if choose == 1:
            print('Введіть арабське число яке потрібно перевести в римьске:')
            print('    * ', translateToRome(int(input('       '))), ' *')
        elif choose == 2:
            print('Введіть римьске число яке треба перевести в арабське:')
            print('    * ', translateToArabian(input('     ').upper()), ' *')


if __name__ == '__main__':
    main()
