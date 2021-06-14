#! /usr/bin/env python3
# -*- coding:utf-8 -*-

class Worker:
    workers = []

    def __init__(self, name, id_code):
        self.name = name
        self.id_code = id_code
        Worker.workers.append(self)

    def calc_m_salary(self):
        pass

    def calc_taxes(self):
        pass

    def calc_m_salary_without_taxes(self):
        pass

    @classmethod
    def sort_workers(cls):

        def find_min(workers):
            min_index = 0
            for i in range(1, len(workers)):
                if workers[i].m_salary > workers[min_index].m_salary:
                    min_index = i
                elif workers[i].m_salary == workers[min_index].m_salary\
                        and workers[i].name < workers[min_index].name:
                    min_index = i
            return min_index

        for i in range(len(cls.workers) - 1):
            min_index = find_min(cls.workers[i:]) + i
            (cls.workers[i],
                cls.workers[min_index]) = (cls.workers[min_index],
                                           cls.workers[i])

    @classmethod
    def out_workers(cls):

        def print_line(lenght, symb='-'):
            for i in range(lenght):
                print(symb, end='')
            print()

        print_line(74, '_')

        print('|', 'id_code'.rjust(8),
              '|', 'name'.ljust(15),
              '|', 'salary'.rjust(10),
              '|', 'taxes'.rjust(10),
              '|', 'salary - taxes'.rjust(15), '|')

        print_line(74)

        for i in cls.workers:
            print('|', str(i.id_code).rjust(8),
                  '|', str(i.name).ljust(15),
                  '|', str(i.m_salary).rjust(10),
                  '|', str(i.calc_taxes()).rjust(10),
                  '|', str(i.calc_m_salary_without_taxes()).rjust(15), '|')

        print_line(74)


class HourlyWorker(Worker):
    def __init__(self, name, id_code, hour_salary, this_month_hours):
        super().__init__(name, id_code)
        self.hour_salary = hour_salary
        self.this_month_hours = this_month_hours
        self.m_salary = self.calc_m_salary()

    def calc_m_salary(self):
        return self.this_month_hours * self.hour_salary

    def calc_taxes(self):
        month = self.calc_m_salary()
        return month * 0.18 + month * 0.015

    def calc_m_salary_without_taxes(self):
        return self.calc_m_salary() - self.calc_taxes()


class FixedWorker(Worker):
    def __init__(self, name, id_code, salary):
        super().__init__(name, id_code)
        self.salary = salary
        self.m_salary = self.calc_m_salary()

    def calc_m_salary(self):
        return self.salary

    def calc_taxes(self):
        month = self.calc_m_salary()
        return month * 0.18 + month * 0.015

    def calc_m_salary_without_taxes(self):
        return self.calc_m_salary() - self.calc_taxes()


class HourlyFOPWorker(Worker):
    def __init__(self, name, id_code, hour_salary, this_month_hours):
        super().__init__(name, id_code)
        self.hour_salary = hour_salary
        self.this_month_hours = this_month_hours
        self.m_salary = self.calc_m_salary()

    def calc_m_salary(self):
        return self.this_month_hours * self.hour_salary * 1.1

    def calc_taxes(self):
        month = self.calc_m_salary()
        return month * 0.05 + 704

    def calc_m_salary_without_taxes(self):
        return self.calc_m_salary() - self.calc_taxes()


class FreeWorker(Worker):
    def __init__(self, name, id_code, price_for_line, this_month_lines):
        super().__init__(name, id_code)
        self.price_for_line = price_for_line
        self.this_month_lines = this_month_lines
        self.m_salary = self.calc_m_salary()

    def calc_m_salary(self):
        return self.price_for_line * self.this_month_lines

    def calc_taxes(self):
        month = self.calc_m_salary()
        return month * 0.18 + month * 0.015 + 704

    def calc_m_salary_without_taxes(self):
        return self.calc_m_salary() - self.calc_taxes()


def main():
    HourlyWorker('Yulia', 12548, 350, 160)
    FixedWorker('Mykola', 12865, 16500)
    HourlyFOPWorker('Carlo', 13540, 250, 140)
    FreeWorker('Vasya', 12455, 3.7, 12500)
    HourlyWorker('Pavlo', 12196, 300, 120)
    FreeWorker('Marta', 14976, 4, 10000)
    HourlyFOPWorker('Oleksander', 12348, 200, 160)

    Worker.sort_workers()
    Worker.out_workers()


if __name__ == '__main__':
    main()
