#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import datetime

class Event:

    def __init__(self, name, to_do, date_time, category, is_ready=False):
        self.name = name
        self.to_do = to_do
        self.date_time = str(date_time)
        self.category = category
        self.is_ready = is_ready

    def create():
        print('\n Введіть ім\'я події(до 10 символів)')

        name = input()
        if len(name) > 10:
            name = name[:10]
            print('\n Ви вийшли за діапазон, записано не весь текст')

        print('\n Введіть що потрібно зробити (до 35 символів)')
        to_do = input()
        if len(to_do) > 35:
            to_do = to_do[:35]
            print('\n Ви вийшли за діапазон, записано не весь текст')
        date = str(Event.input_date())[:-3]

        print('\n Введіть категорію ')
        category = input()

        return Event(name, to_do, date, category)

    def set_ready(self):
        self.is_ready = True

    def display(self):
        print(self.name.ljust(10), self.to_do.ljust(35), self.date_time,
              self.category.ljust(11), '*' if self.is_ready else ' ',
              sep='    ')

    def modify(self, event):
        print('\nЗнайдіть подію яку хочете модифікувати:')
        event = self.search()
        if event is None:
            return

        while True:
            print('\n Виберіть який параметр хочете змінити: ')
            print('* 1 - Ім\'я')
            print('* 2 - Опис')
            print('* 3 - Дата')
            print('* 4 - Категорія')
            try:
                choose = int(input())
            except(ValueError):
                print('\n Це не число, спробуйте ще раз!')
                continue
            else:
                if choose < 1 and choose > 4:
                    print('\n Неправильно введене число, спробуйте ще раз!')

        if choose == 1:
            print('\n Введіть нове ім\'я(до 10 символів)')
            name = input()
            if len(name) > 10:
                name = name[:10]
                print('\n Ви вийшли за діапазон, записано не весь текст')
            event.name = name

        elif choose == 2:
            print('\n Введіть новий опис (до 35 символів)')
            new = input()
            if len(new) > 35:
                new = new[:35]
                print('\n Ви вийшли за діапазон, записано не весь текст!')
            event.to_do = new

        elif choose == 3:
            event.date_time = Event.input_date()

        elif choose == 4:
            print('\n Введіть нову категорію:')
            new = input()
            event.category = new
            EventBook.categories.add(new)

    @staticmethod
    def input_date():
        while True:
            print('\n Введіть дату дедлайна, формат',
                  '("YYYY-MM-DD Hour:Minute")')
            date, time = input().split(' ')
            date = list(map(int, date.split('-')))
            time = list(map(int, time.split(':')))
            try:
                result = datetime.datetime(date[0], date[1], date[2],
                                           time[0], time[1])
            except(ValueError):
                print('\n Неправильно вказані елементи дати та часу!')
                print('Будь ласка, повторіть!')
                continue
            break

        return result


class EventBook:
    def __init__(self):
        self.list_events = list()
        self.read_file('events.txt')

    def read_file(self, filename):
        f = open(filename, encoding='utf-8')
        for i in f:
            i = i[:-1]
            _ = i.split('    ')
            if len(_[0]) > 10:
                _[0] = _[0][:10]
            if len(_[1]) > 35:
                _[1] = _[1][:35]
            event = Event(_[0], _[1], _[2], _[3],
                          True if len(_) == 5 else False)
            self.list_events.append(event)
        f.close()
        print('\n Запис завершено!')

    def write_file(self, filename):
        f = open(filename, 'wt', encoding='utf-8')
        for i in self.list_events[:-1]:
            f.write(i.name, i.to_do, i.date_time,
                    i.category + '    *\n' if self.is_ready else '\n',
                    sep='    ')
        i = self.list_events[-1]
        f.write(i.name, i.to_do, i.date_time,
                i.category + '    *' if self.is_ready else '',
                sep='    ')
        print('\n Файл записано!')

    def add(self):
        self.list_events.append(Event.create())
        print('\n Подію додано!')

    def remove(self):
        print('\n Знайдіть подію, яку потрібно видалити:')
        event = self.search()
        if event is None:
            return
        self.list_events.remove(event)
        print('\n Подію видалено!')

    def search(self):
        print('\n Введіть повністю ім\'я за яким буде виконано пошук: ')
        search_name = input()[:10]
        for i in self.list_events:
            if i.name == search_name:
                return i
        print('\n Таку подію не знайдено, будь ласка,',
              'перевірте правильність введення')
        return None

    def display(self, type=0):
        if type == 1:
            print('\nВведіть категорію, події з якої потрібно вводити:')
            category = input()

        elif type == 2:
            print('* 1 - Вивід по року:')
            print('* 2 - Вивід по точному дню:')

            try:
                choose = int(input())
            except(ValueError):
                print('\n Це не число!')
            else:
                if choose < 1 and choose > 3:
                    print('\n Неправильно введене число!')
                    return

            if choose == 1:
                year = input('Введіть рік:  ')
            elif choose == 2:
                date_time = str(Event.input_date())

        print('\nName'.ljust(14),
              'Description'.ljust(38),
              'Due date'.ljust(19),
              'Category'.ljust(12), 'Is ready')
        for i in range(94):
            print('-', end='')
        print()

        # Загальний вивід
        if type == 0:
            for i in self.list_events:
                i.display()

        # Вивід по категорії
        elif type == 1:
            for i in self.list_events:
                if i.category == category:
                    i.display()

        # Вивід по даті

        elif type == 2:
            if choose == 1:
                for i in self.list_events:
                    if i.date_time[:4] == year:
                        i.display()
            elif choose == 2:
                for i in self.list_events:
                    if i.date_time == date_time:
                        i.display()

        for i in range(94):
            print('-', end='')
        print()

    def modify(self):
        print('\n Знайдіть подію, яку потрібно змінити:')
        event = self.search()
        if event is None:
            return
        event.modify()


def main():
    eb = EventBook()

    while True:
        print('\n         < МЕНЮЮЮЮЮ: >')
        print('----------------------------------')
        print('* 1 - Вивід всіх записів')
        print('* 2 - Вивід записів за категорією')
        print('* 3 - Вивід записів за датою')
        print('* 4 - Додавання нового запису')
        print('* 5 - Видалення запису')
        print('* 6 - Модифікування запису')
        print('* 7 - Завершення роботи')
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
                eb.display()
            elif choose == 2:
                eb.display(1)
            elif choose == 3:
                eb.display(2)
            elif choose == 4:
                eb.add()
            elif choose == 5:
                eb.remove()
            elif choose == 6:
                eb.modify()
            elif choose == 7:
                eb.write_file('events.txt')
                print('\nРобота завершена!')


if __name__ == '__main__':
    main()
