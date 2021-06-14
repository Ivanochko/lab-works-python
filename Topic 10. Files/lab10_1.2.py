import cv2
# import numpy
# import types


def toBin(text):
    if type(text) == str:
        if len(text) > 140:
            raise ValueError('Введено текст більше 140 символів')
        return ''.join([format(ord(i), '08b') for i in text])
    elif type(text) == bytes:
        return [format(i, '08b') for i in text]
    elif type(text) == int:
        return format(text, '08b')


def coding(image, text):
    # number_bytes = image.shape[0] * image.shape[1] * 3 // 8

    text += '==stop=='

    text_index = 0

    binary_text = toBin(text)

    text_lenght = len(binary_text)

    for values in image:
        for pixel in values:
            r, g, b = toBin(pixel)
            if text_index < text_lenght:
                pixel[0] = int(r[:-1] + binary_text[text_index], 2)
                text_index += 1
            if text_index < text_lenght:
                pixel[1] = int(g[:-1] + binary_text[text_index], 2)
                text_index += 1
            if text_index < text_lenght:
                pixel[2] = int(b[:-1] + binary_text[text_index], 2)
                text_index += 1
            if text_index >= text_lenght:
                break

    return image


def coding_text():
    image_name = input('Ім\'я зображення для читання(з форматом): ')
    image = cv2.imread(image_name)

    text = input('Введіть текст який потрібно зашифрувати: ')
    if len(text == 0):
        raise ValueError(' Порожній ввід!')

    image_save_name = input('Ім\'я збереженого зображення(з форматом)')
    cv2.imwrite(image_save_name, coding(image, text))


def main():
    print('\n * (1) - закодувати текст в зображенні',
          '\n * (2) - Розкодувати текст з зображення')
    choose = int(input())

    if choose == 1:
        coding_text()
    elif choose == 2:
        pass
    else:
        raise ValueError('Неправильний ввід!')


if __name__ == '__main__':
    main()
