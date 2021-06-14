from sys import exit


def generate(seed):
    while seed:
        seed_new = seed[3:] + seed[:3]
        seed = str(int(seed) * int(seed_new))
        while len(seed) != 12:
            seed = '0' + seed
        seed = seed[3:9]
        yield seed


def main():
    work = True
    while work:
        seed_str = input('Введіть початкове число: ')
        if len(seed_str) == 6:
            try:
                int(seed_str)
            except ValueError:
                print('Введіть число!')
                continue
            else:
                _ = '\n Enter - наступне число\n будь який ввід - зупинитись!'
                generator = generate(seed_str)
                while not input(_):
                    print('\n   *  ', int(next(generator)), '  *')
                else:
                    work = False
        else:
            print('Повинно бути число з 6 цифр!')
            continue


if __name__ == '__main__':
    main()
