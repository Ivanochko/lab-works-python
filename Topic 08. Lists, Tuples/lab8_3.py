from random import randint


def find_average(array):
    return sum(array) / len(array)


def find_mediana(array):
    a = list(sorted(array))
    return (a[int(len(a) / 2)]
            if len(a) % 2
            else (a[int(len(a) / 2)] + a[int((len(a) - 1) / 2)]) / 2)


if __name__ == '__main__':
    array = []
    for x in range(0, 10):
        array.append(randint(0, 9))
        # array.append(x)
    print('Згенерований масив:\n', array)
    print('Середнє значення:', find_average(array),
          '\nМедіана:', find_mediana(array))
