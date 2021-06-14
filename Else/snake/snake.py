import sys
import random
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, NW


class Cons:
    BOARD_WIDTH = 500
    BOARD_HEIGHT = 500
    DELAY = 100
    DOT_SIZE = 10
    MAX_RAND_POS = 27


class Board(Canvas):
    def __init__(self):
        super().__init__(
            width=Cons.BOARD_WIDTH, height=Cons.BOARD_HEIGHT,
            background="lightblue", highlightthickness=0
        )
        self.initGame()
        self.pack()

    def initGame(self):
        self.inGame = True
        self.dots = 3
        self.score = 0
        self.moveX = Cons.DOT_SIZE
        self.moveY = 0
        self.appleCoords = [(x1, y1), (x2, y2), (x3, y3)]
        # self.appleX = 100
        # self.appleY = 190
        self.loadImages()
        self.createObjects(self.input_number_of_apples())
        self.locateApple() #----------------------------------------------------- передати змінну
        self.bind_all("<Key>", self.onKeyPressed)
        self.after(Cons.DELAY, self.onTimer)

    def loadImages(self):
        try:
            self.idot = Image.open("dot.png")
            self.dot = ImageTk.PhotoImage(self.idot)
            self.ihead = Image.open("head.png")
            self.head = ImageTk.PhotoImage(self.ihead)
            self.iapple = Image.open("apple.png")
            self.apple = ImageTk.PhotoImage(self.iapple)
        except IOError as e:
            print(e)
            sys.exit(1)

    def createObjects(self, number_apples):
        self.create_text(30, 10, text="Счет: {0}".format(self.score),
                         tag="score", fill="white")
        for x in range(number_apples):
            x, y = self.random_coords()
            self.create_image(
                x, y,
                image=self.apple, anchor=NW, tag="apple" + str(x)
            )
            self.appleCoords.append((x, y))
        self.create_image(50, 50, image=self.head, anchor=NW, tag="head")
        self.create_image(30, 50, image=self.dot, anchor=NW, tag="dot")
        self.create_image(40, 50, image=self.dot, anchor=NW, tag="dot")

    def checkAppleCollision(self):
        temp = 0
        for x in self.appleCoords:
            apple = self.find_withtag("apple" + str(x))
            head = self.find_withtag("head")
            x1, y1, x2, y2 = self.bbox(head)
            overlap = self.find_overlapping(x1, y1, x2, y2)
            for ovr in overlap:
                if apple[0] == ovr:
                    self.score += 1
                    # x, y = self.coords(apple, x)
                    x, y = self.random_coords()
                    self.create_image(x, y,
                                      image=self.dot,
                                      anchor=NW,
                                      tag="dot")
                    self.appleCoords.append((x, y))
                    self.locateApple(temp)
            temp += 1

    def moveSnake(self):
        dots = self.find_withtag("dot")
        head = self.find_withtag("head")
        items = dots + head
        z = 0
        while z < len(items) - 1:
            c1 = self.coords(items[z])
            c2 = self.coords(items[z + 1])
            self.move(items[z], c2[0] - c1[0], c2[1] - c1[1])
            z += 1
        self.move(head, self.moveX, self.moveY)

    def checkCollisions(self):
        dots = self.find_withtag("dot")
        head = self.find_withtag("head")
        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)
        for dot in dots:
            for over in overlap:
                if over == dot:
                    self.inGame = False
        if x1 < 0:
            self.inGame = False
        if x1 > Cons.BOARD_WIDTH - Cons.DOT_SIZE:
            self.inGame = False
        if y1 < 0:
            self.inGame = False
        if y1 > Cons.BOARD_HEIGHT - Cons.DOT_SIZE:
            self.inGame = False

    def locateApple(self, number):
        apple = self.find_withtag("apple" + str(number))
        self.appleCoords.remove(apple[0]) # ----------------------------------------------- out of range
        x, y = coords(apple[0])
        self.delete(apple[0])

        rx = random.randint(0, Cons.MAX_RAND_POS)
        ry = random.randint(0, Cons.MAX_RAND_POS)
        self.appleCoords.append((rx, ry))
        # self.appleX = r * Cons.DOT_SIZE
        # self.appleY = r * Cons.DOT_SIZE
        self.create_image(
            self.appleX, self.appleY, anchor=NW,
            image=self.apple, tag="apple" + str(self.score + 2))

    def onKeyPressed(self, e):
        key = e.keysym
        LEFT_CURSOR_KEY = "Left"
        if key == LEFT_CURSOR_KEY and self.moveX <= 0:
            self.moveX = -Cons.DOT_SIZE
            self.moveY = 0
        RIGHT_CURSOR_KEY = "Right"
        if key == RIGHT_CURSOR_KEY and self.moveX >= 0:
            self.moveX = Cons.DOT_SIZE
            self.moveY = 0
        RIGHT_CURSOR_KEY = "Up"
        if key == RIGHT_CURSOR_KEY and self.moveY <= 0:
            self.moveX = 0
            self.moveY = -Cons.DOT_SIZE
        DOWN_CURSOR_KEY = "Down"
        if key == DOWN_CURSOR_KEY and self.moveY >= 0:
            self.moveX = 0
            self.moveY = Cons.DOT_SIZE

    def onTimer(self):
        self.drawScore()
        self.checkCollisions()
        if self.inGame:
            self.checkAppleCollision()
            self.moveSnake()
            self.after(Cons.DELAY, self.onTimer)
        else:
            self.gameOver()

    def drawScore(self):
        score = self.find_withtag("score")
        self.itemconfigure(score, text="Рахунок: {0}".format(self.score))

    def gameOver(self):
        self.delete(ALL)
        _ = "Гра закінчилась з рахунком"
        self.create_text(self.winfo_width() / 2,
                         self.winfo_height() / 2,
                         text=_ + " {0}".format(self.score),
                         fill="white")

    def input_number_of_apples(self):
        LIMIT = 10
        while True:
            try:
                _ = '\n * Введіть кількість яблук(не більше '
                _ += str(LIMIT) + '): '
                number = int(input(_))
            except ValueError:
                print('\n !  Введено не число  ! ')
                continue
            else:
                if number < 1:
                    print('\n !  Не може бути', number, ' яблук  !')
                elif number > LIMIT:
                    print('\n !  Введене число більше ліміту  !')
                else:
                    break
        return number

    def random_coords(self):
        rx = random.randint(0, Cons.MAX_RAND_POS)
        ry = random.randint(0, Cons.MAX_RAND_POS)
        return rx, ry


class Snake(Frame):
    def __init__(self):
        super().__init__()
        self.master.title('Змійка')
        self.board = Board()
        self.pack()


def main():
    root = Tk()
    nib = Snake()
    root.mainloop()


if __name__ == '__main__':
    main()
