def toMorseCode(string):
    morseCode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..', ' ': '  '}
    result = ''
    for i in string.upper():
        if i in morseCode:
            result += morseCode[i] + ' '
        else:
            return 'Error'
    return result


def main():
    string = input('Введіть речення яке потрібно перекласти: ')
    print(toMorseCode(string))


if __name__ == '__main__':
    main()
