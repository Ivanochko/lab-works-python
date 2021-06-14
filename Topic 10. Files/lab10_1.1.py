from PIL import Image, ImageDraw
# image = Image.open('photo.jpg')
# # img.show()
# r, g, b = image.split()
# # print(r)
# histogram = image.histogram()
# # print(histogram)
# exif = image._getexif()
# print(exif)
def coding(image, text):

    def getPart(number):
        return (int(number / 3), int(number / 3),
                int(number - int(number / 3) * 2))

    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
    width = image.size[0]  # Определяем ширину
    height = image.size[1]  # Определяем высоту
    pix = image.load()  # Выгружаем значения пикселей

    i = 0

    index = 0
    maxIndex = len(text) - 1
    stop = False
    for x in range(width):
        if stop:
            break
        for y in range(height):
            r = pix[x, y][0]  # узнаём значение красного цвета пикселя
            g = pix[x, y][1]  # зелёного
            b = pix[x, y][2]  # синего
            # sr = (r + g + b) // 3  # среднее значение
            if i == 1900:
                letter1 = ord(text[index])
                points = getPart(ord(text[index]))

                index += 1
                draw.point((x, y), (letter1, g, b))

                # if index > maxIndex:
                #     draw.point((x, y), (ord(letter1) + r, g, b))
                # else:
                #     letter2 = text[index]
                #     index += 1
                #     if index > maxIndex:
                #         draw.point((x, y),
                #                    (ord(letter1) + r,
                #                     ord(letter2) + g, b))
                #     else:
                #         letter3 = text[index]
                #         index += 1
                #         draw.line([(x, y), (x, y)],
                #                   (ord(letter1) + r,
                #                    ord(letter2) + g,
                #                    ord(letter3) + b))
                #         draw.point((x, y),
                #                    (ord(letter1) + r,
                #                     ord(letter2) + g,
                #                     ord(letter3) + b))
                #         draw.point((x, y), (ord(r), ord(g), ord(b)))
                i = 0
            else:
                draw.point((x, y), (r, g, b))  # рисуем пиксель
            # draw.point((x, y), (r, g, b))  # рисуем пиксель
            if index > maxIndex:
                # print(x, y)
                x += 200
                # y += 200
                # print(x, y)
                draw.point((x, y), (0, 0, 0))
                break
            i += 1
            # index += 1

    image.show()
    # image.save('out.png', 'JPEG')
    del draw


def main():
    image = Image.open('photo3.jpg')
    text = 'Simple string to input in image'
    coding(image, text)
    image.close()


if __name__ == '__main__':
    main()
