#! /usr/bin/env python3
# -*- coding:utf-8 -*-

class PhoneBook:
    # Власник телефонної книги
    def __init__(self):
        self.list_numbers = list()

    def add(self):
        name = PhoneBook.input_name()
        number = PhoneBook.input_number()
        self.list_numbers.append(People(name[0], number, name[1]))

    def remove(self):
        finded = self.search()
        if len(finded) == 0:
            print('\nТаких елементів не знайдено!')
            return
        else:
            if len(finded) == 1:
                print('\nЗнайдено один елемент')
                finded[0].display()
                index = 0
            else:
                print('\nЗнайдено такі елементи:')
                for i in finded:
                    i.display()
                print('Введіть номер елементу(за порядком)',
                      'який потрібно видалити: (0 - всі)')
                index = PhoneBook.input_int(len(finded), 0)

            if index == 0:
                for i in finded:
                    self.list_numbers.remove(i)
                print('Всі вибрані записи видалено!')
                return

            self.list_numbers.remove(finded[index - 1])
            print('Запис видалено!')

    def search(self):
        print('Виберіть критерій пошуку:')
        print('* 1 - Ім\'я та прізвище')
        print('* 2 - Ім\'я')
        print('* 3 - Прізвище')
        print('* 4 - Номер телефону')

        result_list = list()

        choose = PhoneBook.input_int(4, 1)
        if choose == 1:
            full_name = PhoneBook.input_name()
            for i in self.list_numbers:
                if i.first_name == full_name[0]\
                        and i.last_name == full_name[1]:
                    result_list.append(i)
        elif choose == 2:
            name = PhoneBook.input_name(1)[0]
            for i in self.list_numbers:
                if i.first_name == name:
                    result_list.append(i)
        elif choose == 3:
            last_name = PhoneBook.input_name(2)[1]
            for i in self.list_numbers:
                if i.last_name == last_name:
                    result_list.append(i)
        elif choose == 4:
            number = PhoneBook.input_number()
            for i in self.list_numbers:
                if i.number == number:
                    result_list.append(i)

        return result_list

    def display(self):
        for i in self.list_numbers:
            i.display()

    def display_search(self):
        finded = self.search()
        for i in finded:
            i.display()

    @staticmethod
    def input_name(operation=0):
        # operation - тип операції
        # тип 0 - ввід імені та прізвища
        # тип 1 - ввід тільки імені
        # тип 2 - ввід тільки прізвища
        name, last_name = '', ''
        if operation == 0 or operation == 1:
            print('Введіть ім\'я(не більше 20 символів):')
            name = input()
            if len(name) > 20:
                name = name[:20]
                print('Ви вийшли за діапазон, записано не всю інформацію')
        if operation == 0 or operation == 2:
            print('Введіть прізвище(не більше 20 символів):')
            if operation != 2:
                print('(Не обов\'язково, щоб пропустити Enter)')
            last_name = input()
            if len(last_name) > 20:
                last_name = last_name[:20]
                print('Ви вийшли за діапазон, записано не всю інформацію')
        return name, last_name

    @staticmethod
    def input_number():
        while True:
            print('Введіть номер телефону(не більше 15 символів):')
            number = input()
            if len(number) > 15:
                number = number[:15]
                print('Ви вийшли за діапазон, записано не всю інформацію')
            if number.startswith('+'):
                temp_number = number[1:]
            else:
                temp_number = number
            try:
                int(temp_number)
            except ValueError:
                print('В числі не може бути нічого іншого крім цифр!')

                _ = '* 1 - Спробувати ще раз!\n* 2 - Вийти!'
                choose = PhoneBook.input_int(2, 1, _)
                if choose == 2:
                    return
                elif choose == 1:
                    continue
            else:
                return number

    @staticmethod
    def input_int(hight, lower=1, string=''):
        while True:
            try:
                print(string)
                choose = int(input())
            except ValueError:
                print('Введіть число!')
            else:
                if choose > hight or choose < lower:
                    print('Ви вийшли за діапазон, повторіть!')
                else:
                    return choose


class People:
    # Людина, один з записів
    def __init__(self, first_name, number, last_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number

    def display(self):
        print(self.number.ljust(15), self.first_name.ljust(20),
              self.last_name.ljust(20), sep='    ')


class Data:
    def __init__(self, filename, pb):
        self.filename = filename
        self.pb = pb

    def read(self):
        f = open(self.filename, encoding='utf-8')
        for i in f:
            i = i[:-1]
            _ = i.split('    ')
            if len(_[0]) > 15:
                _[0] = _[0][:15]
            if len(_[1]) > 20:
                _[1] = _[1][:20]
            if len(_) > 2:
                if len(_[2]) > 20:
                    _[2] = _[2][:20]
            people = People(_[1], _[0], _[2] if len(_) == 3 else '')
            self.pb.list_numbers.append(people)
        f.close()
        print('\n Зчитування завершено!')

    def write(self):
        f = open(self.filename, 'wt', encoding='utf-8')
        for i in self.pb.list_numbers:
            _ = i.number + "    " + i.first_name + "    " + i.last_name + '\n'
            f.write(_)
        # if len(self.pb.list_numbers) > 0:
            # i = self.pb.list_numbers[-1]
        # f.write(i.number + "    " + i.first_name + "    " + i.last_name)
        print('\n Файл записано!')
        f.close()


def main():
    pb = PhoneBook()
    data = Data('phones.txt', pb)
    data.read()
    while True:
        print('\n         < МЕНЮЮЮЮЮ: >')
        print('----------------------------------')
        print('* 1 - Вивід всіх записів')
        print('* 2 - Вивід записів за пошуком')
        print('* 3 - Додавання нового запису')
        print('* 4 - Видалення запису')
        print('* 5 - Зберегти')
        print('* 6 - Завершення роботи')
        print('----------------------------------')
        try:
            choose = int(input())
        except(ValueError):
            print('Введіть число!!')
            continue
        else:
            if choose < 0 or choose > 7:
                print('Це число не входить в діапазон!')
                continue
            elif choose == 1:
                pb.display()
                data.write()
            elif choose == 2:
                pb.display_search()
                data.write()
            elif choose == 3:
                pb.add()
                data.write()
            elif choose == 4:
                pb.remove()
                data.write()
            elif choose == 5:
                data.write()
            else:
                data.write()
                print('\nРобота завершена!')
                break


if __name__ == '__main__':
    main()
