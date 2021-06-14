def toCountScore(cards):
    coloda = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'T': 10, 'K': 10, 'Q': 10, 'J': 10, 'A': 10}
    score, tuzes = 0, 0
    for i in cards:
        if i.upper() in coloda:
            score += coloda[i.upper()]
        elif i.upper() == 'A':
            tuzes += 1
        else:
            return -1
    for i in range(tuzes):
        if score + 11 + (tuzes - (i + 1)) > 21:
            score += 1
        else:
            score += 11
    return score


def blackjack(cards):
    if toCountScore(cards) == -1:
        print('Карти введені неправильно!')
    elif toCountScore(cards) > 21:
        print('\'Bust\', очок більше 21!')
    elif toCountScore(cards) == 21:
        print('У вас 21, ви виграли!')
    else:
        print('Ваші очки:', toCountScore(cards))


if __name__ == '__main__':
    cards = input('Введіть ваші карти (через пробіл): ').strip().split(' ')
    blackjack(cards)
