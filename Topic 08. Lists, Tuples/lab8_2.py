from random import randint
# import math


def find_min(array):
    min_index = 0
    for i in range(1, len(array)):
        min_index = i if array[i] < array[min_index] else min_index
    return min_index


def sorting(array):
    for i in range(len(array) - 1):
        min_index = find_min(array[i:]) + i
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp


if __name__ == '__main__':
    array = []
    for x in range(0, 20):
        array.append(randint(0, 9))
    print('Згенерований масив:\n', array)
    sorting(array)
    print('Відсортований масив: \n', array)
