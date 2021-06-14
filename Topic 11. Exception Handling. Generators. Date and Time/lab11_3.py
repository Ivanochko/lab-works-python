import os
import sys
from time import sleep


class Game:
    def __init__(self, regime):
        self.field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Той хто ходить перший кладе ><
        self.regime = regime
        if regime == 'two players':
            self.first_player = Player('X')
            self.second_player = Player('O')
        elif regime == 'player':
            self.player = Player('X')
            self.computer = Computer('O')
        else:
            self.computer = Computer('X')
            self.player = Player('O')
        self.count_wins = 0
        self.count_loses = 0
        self.count_draws = 0

    def print_scene(self):
        index = 1
        print('\n\n    ')
        for i in self.field:
            if not index % 3:
                print('', self.field[index - 1], end='')
                print('')
                if index != 9:
                    print('   -----------')
                print('   ', end='')
            else:
                if index == 1:
                    print('   ', self.field[index - 1], '|', end='')
                else:
                    print('', self.field[index - 1], '|', end='')
            index += 1
        print('\n')

    def is_end(self, value1, value2, value3, symb):
        if value1 == symb and value2 == symb\
           and value3 == symb:
            return True
        else:
            return False

    def is_horisontal(self, symb):
        for i in range(0, 7, 3):
            _ = self.is_end(self.field[i], self.field[i + 1],
                            self.field[i + 2], symb)
            if _:
                return True

    def is_vertical(self, symb):
        for i in range(3):
            _ = self.is_end(self.field[i], self.field[i + 3],
                            self.field[i + 6], symb)
            if _:
                return True

    def is_diagonal(self, symb):
        for i in range(0, 4, 2):
            _ = self.is_end(self.field[i], self.field[4],
                            self.field[8 - i], symb)

    def is_draw(self):
        for i in range(1, 10):
            if i in self.field:
                return False
        self.count_draws += 1
        return True

    def isGameOver(self, symb):
        if self.is_horisontal(symb) or self.is_vertical(symb)\
           or self.is_diagonal(symb):
            return True
        else:
            return False

    def is_start_new(self):
        if self.regime != 'two players':
            print('\n Кількість перемог: ', self.count_wins)
            print('\n Кількість поразок: ', self.count_loses)
            print('\n Кількість  нічиїх: ', self.count_draws)
        else:
            print('\n Рахунок першого гравця: ', self.count_wins)
            print('\n Рахунок другого гравця: ', self.count_loses)
            print('\n Кількість  нічиїх: ', self.count_draws)
        print('\n Почати нову?\n   * (1) - Так\n   * (2) - Ні')
        while True:
            pass
            try:
                choose = int(input())
            except ValueError:
                print('Введіть число!')
            else:
                if choose == 1:
                    self.field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    self.play()
                elif choose == 2:
                    print('До зустрічі!')
                    sys.exit()
                else:
                    print('Введіть число правильно!')

    def is_win(self, player):
        if self.isGameOver(self.first_player.move_symb):
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print_scene()
            print('   Перший гравець виграв!   ')
            return
        elif self.is_draw():
            self.print_scene()
            print('   Нічия!')

    def play(self):
        if self.regime == 'two players':
            while not self.isGameOver('X') or not self.isGameOver('O')\
                    or self.is_draw():
                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_scene()
                print('\n\\  *  \\  * Перший гравець *  /  *  /')
                self.first_player.move(self)
                if self.isGameOver(self.first_player.move_symb):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.print_scene()
                    print('   Перший гравець виграв!   ')
                    self.count_wins += 1
                    self.is_start_new()
                elif self.is_draw():
                    self.print_scene()
                    print('   Нічия!')
                    self.is_start_new()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_scene()
                print('\n\\  *  \\  * Другий гравець *  /  *  /')
                self.second_player.move(self)
                if self.isGameOver(self.second_player.move_symb):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.print_scene()
                    print('   Другий гравець виграв!   ')
                    self.count_loses += 1
                    self.is_start_new()
                elif self.is_draw():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.print_scene()
                    print('   Нічия!')
                    self.count_draws += 1
                    self.is_start_new()

        elif self.regime == 'player':
            while not self.isGameOver('X') or not self.isGameOver('O')\
                    or self.is_draw():
                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_scene()
                # print('\n\\  *  \\  * Ваш хід *  /  *  /')
                self.player.move(self)
                if self.isGameOver(self.player.move_symb):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.print_scene()
                    print('   Гравець виграв!   ')
                    self.count_wins += 1
                    self.is_start_new()
                elif self.is_draw():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.print_scene()
                    print('   Нічия!')
                    self.is_start_new()
                os.system('cls' if os.name == 'nt' else 'clear')
                # print('\n\\  *  \\  * Хід комп\'ютера *  /  *  /')
                self.print_scene()
                self.computer.move(self)
                if self.isGameOver(self.computer.move_symb):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.print_scene()
                    print('   Комп\'ютер виграв!   ')
                    self.count_loses += 1
                    self.is_start_new()
                elif self.is_draw():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.print_scene()
                    self.count_draws += 1
                    print('   Нічия!')
                    self.is_start_new()
                sleep(2)
        elif self.regime == 'computer':
            while not self.isGameOver('X') or not self.isGameOver('O')\
                    or self.is_draw():
                os.system('cls' if os.name == 'nt' else 'clear')
                # print('\n\\  *  \\  * Хід комп\'ютера *  /  *  /')
                self.print_scene()
                self.computer.move(self)
                if self.isGameOver(self.computer.move_symb):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.print_scene()
                    print('   Комп\'ютер виграв!   ')
                    self.count_loses += 1
                    self.is_start_new()
                elif self.is_draw():
                    self.print_scene()
                    self.count_draws += 1
                    print('   Нічия!')
                    self.is_start_new()
                sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_scene()
                # print('\n\\  *  \\  * Ваш хід *  /  *  /')
                self.player.move(self)
                if self.isGameOver(self.player.move_symb):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.print_scene()
                    print('   Гравець виграв!   ')
                    self.count_wins += 1
                    self.is_start_new()
                elif self.is_draw():
                    self.print_scene()
                    print('   Нічия!')
                    self.is_start_new()


class Player:
    def __init__(self, move_symb):
        self.move_symb = move_symb

    def move(self, game):
        while True:
            print('\n  *  *  *    Ваш хід!   *  *  * ')
            print('Введіть координату куди походити    ')
            try:
                coord = int(input()) - 1
            except ValueError:
                print('Введіть число!')
            else:
                if coord > 8 or coord < 0:
                    print('Введіть правильне число!')
                if game.field[coord] != coord + 1:
                    print('Поле заняте')
                else:
                    game.field[coord] = self.move_symb
                    break


class Computer:
    def __init__(self, move_symb):
        self.move_symb = move_symb
        if move_symb == 'O':
            self.opponent_symb = 'X'
        else:
            self.opponent_symb = 'O'

    def is_can_win(self, value1, value2, value3, symb):
        if value1 == symb and value2 == symb\
           and value3 != self.move_symb and value3 != self.opponent_symb:
            return value3
        elif value2 == symb and value3 == symb\
                and value1 != self.move_symb and value1 != self.opponent_symb:
            return value1
        elif value1 == symb and value3 == symb\
                and value2 != self.move_symb and value2 != self.opponent_symb:
            return value2
        else:
            return False

    def sub_check(self, game, symb):
        for i in range(0, 9, 3):
            _ = self.is_can_win(game.field[i],
                                game.field[i + 1],
                                game.field[i + 2],
                                symb)
            if _:
                game.field[_ - 1] = self.move_symb
                return True
        for i in range(3):
            _ = self.is_can_win(game.field[i],
                                game.field[i + 3],
                                game.field[i + 6],
                                symb)
            if _:
                game.field[_ - 1] = self.move_symb
                return True
        for i in range(0, 4, 2):
            _ = self.is_can_win(game.field[i],
                                game.field[4],
                                game.field[8 - i],
                                symb)
            if _:
                game.field[_ - 1] = self.move_symb
                return True
        return False

    def move(self, game):
        print('\n  *  *  *    Хід комп\'ютера!   *  *  * \n')
        if game.field[4] == 5:
            game.field[4] = self.move_symb
            return
        else:
            if self.sub_check(game, self.move_symb):
                return
            elif self.sub_check(game, self.opponent_symb):
                return
            else:
                for i in range(0, 9, 2):
                    if game.field[i] != game.player.move_symb and\
                       game.field[i] != game.computer.move_symb:
                        game.field[i] = self.move_symb
                        return
                else:
                    for i in range(1, 8, 2):
                        if game.field[i] != game.player.move_symb and\
                           game.field[i] != game.computer.move_symb:
                            game.field[i] = self.move_symb
                            return


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print('Виберіть режим:',
              '\n  * (1) - гра з другом\n  * (2) - самостійна гра')
        try:
            choose = int(input())
        except ValueError:
            print('Введіть число!')
        else:
            if choose == 1:
                game = Game('two players')
                game.play()
            elif choose == 2:
                while True:
                    print('Хто починає перший?',
                          '\n  * (1) - гравець\n  * (2) - комп\'ютер')
                    try:
                        choose2 = int(input())
                    except ValueError:
                        print('Введіть число!')
                    else:
                        if choose2 == 1:
                            game = Game('player')
                            game.play()
                        elif choose2 == 2:
                            game = Game('computer')
                            game.play()
                        else:
                            print('Введіть правильне число!')
                            break
            else:
                print('Введіть правильне число!')
                break


if __name__ == '__main__':
    main()
