from PIL import Image, ImageDraw
from time import sleep
import sys


def textToBin(text):
    if type(text) == str:
        if len(text) > 160:
            raise ValueError('Введено текст більше 160 символів')
        # Перетворюємо обов'язково в восьмибітний набір для коректного
        # переведення назад в текст
        return ''.join([format(ord(i), '08b') for i in text])


def openImage(image_name):
    try:
        image = Image.open(image_name)
    except IOError:
        print('Проблеми з відкриттям файлу')
        sys.exit()
    else:
        return image


def coding(image, text):
    # Додаємо до тексту "стоп" строку
    text += '##stop##'
    # Створюємо інструмент для малювання
    draw = ImageDraw.Draw(image)
    # Завантажуємо значення пікселів
    pix = image.load()
    # Перетворюємо весь текст в бінарний вигляд
    text_bin = textToBin(text)
    index = 0
    stop = False
    # Цикл який проходить по пікселях зображення по ширині
    for x in range(image.size[0]):
        if stop:
            break
        # Цикл який проходить по пікселях зображення по довжині
        for y in range(image.size[1]):
            # Дізнаємось значення пікселів в RGB
            r = image.getpixel((x, y))[0]
            g = image.getpixel((x, y))[1]
            b = image.getpixel((x, y))[2]
            # Переводимо ці значення в бінарний вигляд
            r_bin = format(r, '08b')
            g_bin = format(g, '08b')
            b_bin = format(b, '08b')
            # Перевіряємо для кожного кольору
            # чи ще не весь текст зашифровано
            # та поетапно вставляємо в останній біт
            # восьмибітного коду числа поточний біт тексту
            if index < len(text_bin):
                r_bin = r_bin[:-1] + text_bin[index]
                index += 1
            if index < len(text_bin):
                g_bin = g_bin[:-1] + text_bin[index]
                index += 1
            if index < len(text_bin):
                b_bin = b_bin[:-1] + text_bin[index]
                index += 1

            image.putpixel((x, y), (int(r_bin, 2),
                                    int(r_bin, 2),
                                    int(r_bin, 2)))
            # image.putpixel((x + 1, y), (0,
            #                             0,
            # #                             0))
            # r = image.getpixel((x, y))[0]
            # g = image.getpixel((x, y))[1]
            # b = image.getpixel((x, y))[2]

            r_bin = format(r, '08b')
            g_bin = format(g, '08b')
            b_bin = format(b, '08b')

            if index >= len(text_bin):
                stop = True
                break
    del draw

    return image


def decoding(image):
    # Завантажуємо значення пікселів
    # pix = image.load()
    binary_text = ''
    stop = False
    index = 0
    for x in range(image.size[0]):
        if stop:
            break
        # Цикл який проходить по пікселях зображення по довжині
        for y in range(image.size[1]):
            # Дізнаємось значення пікселів в RGB
            r = image.getpixel((x, y))[0]
            g = image.getpixel((x, y))[1]
            b = image.getpixel((x, y))[2]

            # Переводимо ці значення в бінарний вигляд
            r_bin = format(r, '08b')
            g_bin = format(g, '08b')
            b_bin = format(b, '08b')
            # Витягуємо значення з пікселів
            binary_text += r_bin[-1]
            binary_text += g_bin[-1]
            binary_text += b_bin[-1]
            index += 1
            if index > 160:
                stop = True
                break
    # Ділимо бінарний код на восьмибітні значення
    all_bytes = [binary_text[i: i + 8]
                 for i in range(0, len(binary_text), 8)]
    # Переводимо бінарний код в текст
    decoded_text = ''
    for byt in all_bytes:
        decoded_text += chr(int(byt, 2))
        # Перевіряємо на "стоп" строку
        if decoded_text[-8:] == '##stop##':
            break
    print(decoded_text)


def toCodeImage():
    image_name = input('image_name: ')
    image_name += '.bmp'
    image = openImage(image_name)
    text = input('text : ')
    image = coding(image, text)
    image_name = input('save image name: ')
    image.save(image_name, 'BMP')
    print('3131')

def toDecodeImage():
    image_name = input('image_name: ')
    image_name += '.bmp'
    image = openImage(image_name)
    decoding(image)


def main():
    print('\n * (1) - закодувати текст в зображенні',
          '\n * (2) - Розкодувати текст з зображення')
    try:
        choose = int(input())
    except ValueError:
        print('Неправильний ввід')
    else:
        if choose == 1:
            toCodeImage()
        elif choose == 2:
            toDecodeImage()
        else:
            raise ValueError('Неправильний ввід!')


if __name__ == '__main__':
    main()
