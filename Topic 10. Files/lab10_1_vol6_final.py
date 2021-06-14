#! usr/bin/env python3
# -*- coding: utf-8 -*-
'''
             *   Стеганографія    *

    Програма для зашифровування тексту в зображенні
    Містить 3 функції
        1 - openImage(image_name) - Відкриття мультимедійного файлу
        2 - coding() - Зашифровування тексту в зображенні
              * при вводі імені зображення обов'язково не
                вказувати формат файлу при вводі
              * підтримує файли тільки .bmp формату
              * Резульат успішної роботи:
                - збережене зображення в поточній папці з зашифрованим текстом
                  (формат .bmp)
                - повідомлення про успішне збереження
        3 - decoding() - Розгифровування тексту з зображення
              * найімовірніше буде розшифровуватись тільки те зображення яке
                зашифроване саме в цій програмі
              * при вводі імені зображення обов'язково не
                вказувати формат файлу при вводі
              * підтримує файли тільки .bmp формату
              * Результат успішної роботи:
                - виводить на екран розшифрований текст
                - повертає цей текст в функцію звідки викликано

    ! Для роботи програми обо'язково встановити модуль Pillow !
        (pip install Pillow)
        Resourse: https://pypi.org/project/Pillow/

    ! Працює тільки з Англійською мовою цифами і стандартними символами!
        ( символи з таблиці ascii з значенням до 255 включно )

    ! Найкраще виконувати в консолі Windows або терміналі Linux !
'''
from PIL import Image
import sys


def openImage(image_name):
    try:
        image = Image.open(image_name)
    except IOError:
        print('Проблеми з відкриттям файлу')
        sys.exit()
    else:
        return image


def coding():
    print('\n (Формат файлу вводити не потрібно!)')
    print(' (наприклад image_with_shifr)')
    image_name = input('Ім\'я зображення для читання(з форматом bmp): ')
    # Відкриваємо файл і дописуємо формат
    image = openImage(image_name + '.bmp')
    # Отримуємо текст який потрібно заширфувати і додаємо "стоп" строку "####"
    text = input('Введіть текст який потрібно зашифрувати:\n') + '####'
    if len(text) == 0:
        print(' Порожній ввід!')
        sys.exit()
    # Переводимо строку в бінарний восьмибітний код посимвольно
    bin_text = ''.join([format(ord(i), '08b') for i in text])
    # Загружаємо значення пікселів
    pix = image.load()
    # Допоміжні змінні
    index, stop = 0, 0
    # Проходимо по кожному пікселі зображення
    for x in range(image.size[0]):
        if stop:
            break
        for y in range(image.size[1]):
            # Отримуємо значення поточного пікселя
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            # Перетворюємо значення пікселів в бінрний восьмибітний код
            r_bin = format(r, '08b')
            g_bin = format(g, '08b')
            b_bin = format(b, '08b')
            '''
            Поступово додаємо біти тексту в останній біт бінарного коду
            значення насиченості кожного пікселя
            з поступовою перевіркою на закінчення тексту
            '''
            if index < len(bin_text):
                r_bin = r_bin[:-1] + bin_text[index]
                index += 1
            if index < len(bin_text):
                g_bin = g_bin[:-1] + bin_text[index]
                index += 1
            if index < len(bin_text):
                b_bin = b_bin[:-1] + bin_text[index]
                index += 1
            # Повертаємо перетворені пікселі назад в зображення
            image.putpixel((x, y), (int(r_bin, 2),
                                    int(g_bin, 2),
                                    int(b_bin, 2)))
            # Передчасне зупинення запису тексту
            if index >= len(bin_text):
                stop = True
                break
    # Зберігаємо зображення
    print('\n (Формат файлу вводити не потрібно!)')
    print(' (наприклад save)')
    image_save_name = input('Ім\'я зображення для зберігання: ') + '.bmp'
    print('\n    ', 'Збережено!')
    image.save(image_save_name, 'BMP')
    image.close()


def decoding():
    print('\n (Формат файлу вводити не потрібно!)')
    print(' (наприклад save)')
    image_name = input('Ім\'я зображення для читання(з форматом bmp): ')
    # Відкриваємо файл і дописуємо формат
    image = openImage(image_name + '.bmp')
    # Загружаємо значення пікселів
    pix = image.load()
    # Змінна для накопичення бітів
    bin_text = ''
    # Змінна для накопичення тексту
    decoded_text = ''
    stop = False
    # Проходимо по кожному пікселі зображення
    for x in range(image.size[0]):
        if stop:
            break
        for y in range(image.size[1]):
            # Отримуємо значення поточного пікселя
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            # Перетворюємо значення пікселів в бінрний восьмибітний код
            r_bin = format(r, '08b')
            g_bin = format(g, '08b')
            b_bin = format(b, '08b')
            # Отримуємо останній біт з кожного файла
            bin_text += r_bin[-1]
            bin_text += g_bin[-1]
            bin_text += b_bin[-1]
            # Якщо це можливо - витягуємо з бінарного коду букву
            if len(bin_text) >= 8:
                decoded_text += chr(int(bin_text[:8], 2))
                # Видаляємо код витягнутої букви з загального коду
                bin_text = bin_text[8:]
                # Перевірка на "стоп" строку
                if decoded_text[-4:] == '####':
                    stop = True
                    break
    image.close()
    if decoded_text[-4:] != '####':
        print('Зображення не має зашифрованого послання,',
              'або зашифроване не в цій програмі')
        return ''
    print('\nЗашифрований текст з зображення:')
    print(decoded_text[:-4])
    # Повертаємо текст без "стоп" строки
    return decoded_text[:-4]


def main():
    print('\n * (1) - закодувати текст в зображенні',
          '\n * (2) - Розкодувати текст з зображення')
    try:
        choose = int(input())
    except ValueError:
        print('Неправильний ввід')
    else:
        if choose == 1:
            coding()
        elif choose == 2:
            decoding()
        else:
            print('Неправильний ввід!')


if __name__ == '__main__':
    main()
