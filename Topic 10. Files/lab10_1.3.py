from PIL import Image, ImageDraw
from time import sleep
import sys


def textToBin(text):
    if type(text) == str:
        if len(text) > 140:
            raise ValueError('Введено текст більше 140 символів')
        # Перетворюємо обов'язково в восьмибітний набір для коректного
        # переведення назад в текст
        return ''.join([format(ord(i), '08b') for i in text])


# def addJPG(image_name):
#     if not image_name.endswith('.jpg'):
#         return image_name + '.jpg'


def openImage(image_name):
    # image_name = addJPG(image_name)
    try:
        image = Image.open(image_name)
    # except OSError:
    #     raise ValueError('Файл не знайдено!')
    except IOError:
        print('Проблеми з відкриттям файлу')
        sys.exit()
        # raise SystemExit
        # print('Проблеми з відкриттям файла!')
        # raise IOError('Проблеми з відкриттям файла!')
        # quit()
    else:
        # text = input('Введіть текст який потрібно зашифрувати: ')
        # if len(text) == 0:
        #     raise ValueError(' Порожній ввід!')

        # coding(image, text)
        # print('Закодовую інформацію...')
        # sleep(2)
        # print('  Закодовано!')
        # image.save(input('Ім\'я збереженого зображення: '), "JPEG")
        # print('Зберігаю...')
        # sleep(2)
        # print('  Збережено!')
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
    # print(text_bin)
    # print('================')
    stop = False
    # Цикл який проходить по пікселях зображення по ширині
    for x in range(image.size[0]):
        if stop:
            break
        # Цикл який проходить по пікселях зображення по довжині
        for y in range(image.size[1]):
            # Дізнаємось значення пікселів в RGB
            # r = pix[x, y][0]
            # g = pix[x, y][1]
            # b = pix[x, y][2]
            r = image.getpixel((x, y))[0]
            g = image.getpixel((x, y))[1]
            b = image.getpixel((x, y))[2]
            # print(r,g,b)
            # Переводимо ці значення в бінарний вигляд
            r_bin = format(r, '08b')
            g_bin = format(g, '08b')
            b_bin = format(b, '08b')
            # print(r_bin,g_bin,b_bin)
            # print(r_bin)
            # print(g_bin)
            # print(b_bin)
            # print('=-09315909=-')
            # Перевіряємо для кожного кольору
            # чи ще не весь текст зашифровано
            # та поетапно вставляємо в останній біт
            # восьмибітного коду числа поточний біт тексту
            # print(text_bin[index: index + 3])
            if index < len(text_bin):
                # print(text_bin[index], end='')
                # print(index, ' : r: ', r, 'r_bin: ', r_bin)
                r_bin = r_bin[:-1] + text_bin[index]
                # print(index, ' : r: ', int(r_bin, 2), 'r_bin: ', r_bin)
                index += 1
            if index < len(text_bin):
                # print(text_bin[index], end='')
                # print(index, ' : g: ', g, 'g_bin: ', g_bin)
                g_bin = g_bin[:-1] + text_bin[index]
                # print(index, ' : g: ', int(g_bin, 2), 'g_bin: ', g_bin)
                index += 1
            if index < len(text_bin):
                # print(text_bin[index], end='')
                # print(index, ' : b: ', b, 'b_bin: ', b_bin)
                b_bin = b_bin[:-1] + text_bin[index]
                # print(index, ' : b: ', int(b_bin, 2), 'b_bin: ', b_bin)
                index += 1
            # print(r_bin)
            # print(g_bin)
            # print(b_bin)
            # print('-==-=-=-=-=-=-=-=-')
            # print(r_bin,g_bin,b_bin)
            # print('*/*//*/***//**/*/')
            # print()
            # print(r_bin)

            # Малюємо точку з згенерованими значеннями
            # draw.point((x, y), (int(r_bin, 2),
            #                     int(g_bin, 2),
            #                     int(b_bin, 2)))
            # draw.point((x, y), (0,
            #                     0,
            #                     0))
            # image.putpixel((x, y), (int(r_bin, 2),
            #                         int(g_bin, 2),
            #                         int(b_bin, 2)))

            image.putpixel((x, y), (0,
                                    0,
                                    0))
            image.putpixel((x + 1, y), (0,
                                        0,
                                        0))
            r = image.getpixel((x, y))[0]
            g = image.getpixel((x, y))[1]
            b = image.getpixel((x, y))[2]
            # print(r,g,b)
            r_bin = format(r, '08b')
            g_bin = format(g, '08b')
            b_bin = format(b, '08b')
            print(r_bin, g_bin, b_bin)

            if index >= len(text_bin):
                stop = True
                break
    del draw
    # print('return')
    return image


def decoding(image):
    # Завантажуємо значення пікселів
    pix = image.load()
    binary_text = ''
    stop = False
    for x in range(image.size[0]):
        if stop:
            break
        # Цикл який проходить по пікселях зображення по довжині
        for y in range(image.size[1]):
            # Дізнаємось значення пікселів в RGB
            r = image.getpixel((x, y))[0]
            g = image.getpixel((x, y))[1]
            # g = pix[x, y][1]
            b = image.getpixel((x, y))[2]
            # b = pix[x, y][2]
            print(r, g, b)
            print('-0-0')
            # Переводимо ці значення в бінарний вигляд
            r_bin = format(r, '08b')
            g_bin = format(g, '08b')
            b_bin = format(b, '08b')
            print(r_bin)
            print(g_bin)
            print(b_bin)
            print('-==-=-=-=-=-=-=-=-')
            # Витягуємо значення з пікселів
            binary_text += r_bin[-1]
            binary_text += g_bin[-1]
            binary_text += b_bin[-1]
            # print(binary_text[y: y + 3])
    # Ділимо бінарний код на восьмибітні значення
    all_bytes = [binary_text[i: i + 8]
                 for i in range(0, len(binary_text), 8)]
    # Переводимо бінарний код в текст
    decoded_text = ''
    for byt in all_bytes:
        # print(byt)
        decoded_text += chr(int(byt, 2))
        # Перевіряємо на "стоп" строку
        if decoded_text[-8:] == '##stop##':
            break
    # sleep
    # print(decoded_text)
    # for x in range(48):
    #     if not x % 8:
    #         print()
    #     print(binary_text[x], end='')
    # print('--=-=-=-=-=-=-=-')
    # print(all_bytes)
    # print(decoded_text)


def toCodeImage():
    image_name = input('Ім\'я зображення для читання(з форматом jpg): ')

    # try:
    #     image = Image.open(image_name)
    # # except OSError:
    # #     raise ValueError('Файл не знайдено!')
    # except IOError:
    #     print('Проблеми з відкриттям файла!')
    #     quit()
    # else:
    image_name = image_name + '.jpg'
    image = openImage(image_name)
    text = input('Введіть текст який потрібно зашифрувати: ')
    if len(text) == 0:
        print(' Порожній ввід!')
        sys.exit()

    image = coding(image, text)
    image.show()

    print('Закодовую інформацію...')
    sleep(2)
    print('  Закодовано!')
    image_name = input('Ім\'я збереженого зображення: ')
    # image_name = addJPG(image_name)
    image_name = image_name + '.jpg'

    image.save(image_name, "JPEG", quality=100)
    print('Зберігаю...')
    sleep(2)
    print('  Збережено!')
    image.close()


def toDecodeImage():
    image_name = input('Ім\'я зображення для читання(з форматом jpg): ')
    # if not image_name.endswith('.jpg'):
    #     image_name += '.jpg'
    image_name = image_name + '.jpg'
    image = openImage(image_name)
    print(image_name)
    input()
    decoding(image)
    image.close()


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
            # toDecodeImage()
        elif choose == 2:
            toDecodeImage()
        else:
            raise ValueError('Неправильний ввід!')


if __name__ == '__main__':
    main()
