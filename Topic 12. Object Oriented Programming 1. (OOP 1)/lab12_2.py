import math
from sys import exit


def rotate_point(x, y, a):
    x_new = x * math.cos(a) + y * math.sin(a)
    y_new = y * math.cos(a) - x * math.sin(a)
    return (round(x_new), round(y_new))


def open_file(filename):
    try:
        file = open(filename, 'rt')
    except IOError:
        print('Помилка відкриття файлу!')
        exit()
    else:
        return file


def find_min(array):
    min_index = 0
    for i in range(1, len(array)):
        if array[i][2] < array[min_index][2]:
            min_index = i
        elif array[i][2] == array[min_index][2]\
                and array[i][1] < array[min_index][1]:
            min_index = i
    return min_index


def sorting(array):
    for i in range(len(array) - 1):
        min_index = find_min(array[i:]) + i
        array[i], array[min_index] = array[min_index], array[i]


def function():
    filename = 'stars.txt'
    filename_to_save = 'stars_save.txt'
    file = open_file(filename)
    # Ділимо файл по рядках
    data = file.read().split('\n')
    file.close()
    # В першому рядку перше значення - кількість зірок
    count_start = int(data[0].split(' ')[0])
    # Друге значення - кут повороту (від'ємне - проти годинникової стрілки)
    degree = -(int(data[0].split(' ')[1]) * math.pi) / 180
    list_stars = []
    # Проходимо файл по рядках (крім першого) одразу повертаючи координати
    for i in range(1, count_start + 1):
        name = data[i].split(' ')[0]
        x = int(data[i].split(' ')[1])
        y = int(data[i].split(' ')[2])
        x, y = rotate_point(x, y, degree)
        list_stars.append([name, x, y])
    # Сортуємо список з зірками
    sorting(list_stars)

    file = open(filename_to_save, 'wt')

    for i in list_stars:
        file.write(i[0] + ' ')

    file.close()


def main():
    function()
    print('Complete!')


if __name__ == '__main__':
    main()
