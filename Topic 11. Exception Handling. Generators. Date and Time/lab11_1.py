import sys


def get_byte(line):
    index_start = line.find(' ',
                            line.find('"', line.find('"', 40) + 1) + 2) + 1
    index_end = line.find(' ', index_start)

    return int(line[index_start: index_end])


def count(name_file):
    count_bytes = 0
    try:
        file = open(name_file, 'rt')
    except IOError:
        print('Проблеми з відкриттям файлу')
        sys.exit()
    else:
        lines = (line for line in file)
        while True:
            try:
                count_bytes += get_byte(next(lines))
            except StopIteration:
                return count_bytes
        file.close()
        return count_bytes


def main():
    name = '2017_05_07_nginx.txt'
    print('Загальна кількість байтів:', count(name))


if __name__ == '__main__':
    main()
