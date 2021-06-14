# -*- coding: utf-8 -*-
import sys
import random
board = [1,2,3,4,5,6,7,8,9]
win_coords = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

def drawBoard (board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Ваш хід " + player_token + ": ")
        try:
            player_answer = int(player_answer)
        except:
            print("Ви точно ввели число? Перевірте, будь ласка)")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Клітинка вже занята :(")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")  
            
def win_check(board):
    for each in win_coords:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def bot_check(board, token):
        for each in win_coords:
            if str(board[each[2]]) not in token and str(board[each[0]]) not in token and str(board[each[1]]) not in token :
                if board[each[0]] == board[each[1]] :
                    board[each[2]] = "O"
                    return True
                elif board[each[1]] == board[each[2]]:
                    board[each[0]] = "O"
                    return True
                elif board[each[0]] == board[each[2]]:
                    board[each[1]] = "O"
                    return True
        return False

def bot_turn (board, counter):
    if counter == 1 and str(board[4]) not in "XO":
        board[4] = "O"
    else:
        if counter > 2:
            tmp1 = bot_check(board, "X")
            if tmp1:
                drawBoard(board)
                print("Перемагає Комп`ютер!")
                sys.exit()
                input()
            else:
                tmp2 = bot_check(board, "O")
                if tmp2 == True:
                    return 0
                else: 
                    valid = False
                    while not valid:
                        turn = random.randint(0,9)
                        if turn >=0 and turn <=8:
                            if (str(board[turn]) not in "XO"):
                                board[turn] = "O"
                                valid = True    
        else:
            turn = random.choice([0,2,6,8])
            if (str(board[turn]) not in "XO"):
                    board[turn] = "O"
                    valid = True
                    return 0
            tmp2 = bot_check(board, "O")
            if tmp2 == True:
                return 0
            else: 
                valid = False
                while not valid:
                    turn = random.randint(0,9)
                    if turn >=0 and turn <=8:
                            if (str(board[turn]) not in "XO"):
                                board[turn] = "O"
                                valid = True    

                
def main(board):
    counter = 0
    win = False
    print("Ви граєте за Х!")
    while not win:
        drawBoard(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            print("Комп'ютер ходить:")
            bot_turn (board, counter)
        counter += 1
        if counter > 2:
            tmp = win_check(board)
            if tmp:
                print(tmp, "переміг!!")
                win = True
                break
                input()
        if counter == 9:
            print( "Нічия!")
            break
            input()
    drawBoard(board)
    
    
main(board)