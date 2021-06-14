from random import randint
import lab9_1
import os

coloda = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'T': 10, 'K': 10, 'Q': 10, 'J': 10, 'A': 10}
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'K', 'Q', 'J', 'A']


def getRandomCard():
    return cards[randint(0, len(cards) - 1)]


def outCards(cards):
    string = ''
    for i in cards:
        string += i + ' '
    return string


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    input('\nНатисніть Enter, щоб почати')
    os.system('cls' if os.name == 'nt' else 'clear')
    myCards = []
    isGetCard = 0

    while not isGetCard:
        if lab9_1.toCountScore(myCards) > 21:
            print('Bust, ви програли!')
            break
        print('\n(0) - витягнути карту\n'
              '(будь-яке інше число) - зупинитись')
        isGetCard = int(input())

        if not isGetCard:
            os.system('cls' if os.name == 'nt' else 'clear')
            myCards.append(getRandomCard())
            print('\nВам випала карта', myCards[len(myCards) - 1])
            myScore = lab9_1.toCountScore(myCards)
            print('\nТепер ваші карти:', outCards(myCards))
            print('Тепер ваші очки:', myScore)
    else:
        lab9_1.blackjack(myCards)


if __name__ == '__main__':
    main()
