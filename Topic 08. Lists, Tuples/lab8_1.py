def killAllOnStep(peoples, step):
    count = 0
    while len(peoples) != 1:
        i = 0
        while i < len(peoples):
            count += 1
            if count == step:
                count = 0
                del(peoples[i])
                i -= 1
            i += 1
    # Результат повернення інкрементується оскільки ми працювали з
    # Індексами, а потрібно повернути номер людини ( нумерація з 1 )
    return peoples[0] + 1


if __name__ == '__main__':
    peoples = [i for i in range(0, int(input('Введіть кількість людей: ')))]
    step = int(input('Введіть крок вбивання: '))
    print('Номер людини, якій доведеться зробити самогубство: ',
          killAllOnStep(peoples, step))
