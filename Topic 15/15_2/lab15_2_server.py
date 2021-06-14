#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import datetime

host = '127.0.0.1'
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))


class Data():
    def open_users():
        f = open('users.txt')
        users = {}
        for i in f:
            temp = i.split(' ')
            users[temp[0]] = temp[1][:-1]

        f.close()
        return users

    def write_users(users):
        f = open('users.txt', 'w+t')
        for i in users:
            f.write(i + ' ' + users[i] + '\n')
        f.close()

    def open_public():
        f = open('public.txt')
        text = f.read()
        return text

    def write_public(text):
        f = open('public.txt', 'w+t')
        f.write(text)
        f.close()

    def add_user(users, login, password):
        users[login] = password
        Data.write_users(users)
        return users

    def add_to_public_file(login, text):
        text = login + ': ' + text + '\n'
        text = str(datetime.datetime.today()
                   .strftime('%d.%m.%y %H:%M:%S')) + text
        f = open('public.txt', 'a')
        f.write(text)
        f.close()


class User():
    def log_in(clientsocket, users) -> (dict, str):
        work = True
        while work:
            clientsocket.send('\n Enter you login(name):'.encode('utf-8'))
            clientsocket.send('->    '.encode('utf-8'))
            login = clientsocket.recv(1024).decode('utf-8')
            if login in users:
                work = False
                attempt = 0
                clientsocket.send(('Your login is ' + login).encode('utf-8'))
                while True:
                    clientsocket.send('\n Enter your password:'
                                      .encode('utf-8'))
                    password = clientsocket.recv(1024).decode('utf-8')
                    if password != users[login]:
                        attempt += 1
                        if attempt == 3:
                            clientsocket.send('\n Too many attempts!-1+3$5%1'
                                              .encode('utf-8'))
                            clientsocket.close()
                            print('Client close!')
                            return (users, login)
                        clientsocket.send('\n Wrong password, try again:'
                                          .encode('utf-8'))
                    else:
                        clientsocket.send(('\n Welcome, ' + login)
                                          .encode('utf-8'))
                        print('Client logined,', login)
                        return (users, login)
            else:
                clientsocket.send('\n Could not find this user!\n'
                                  .encode('utf-8'))
                _ = ' 1 - Create new\n'
                _ += ' 2 - Search again\n'
                _ += ' 3 - Exit\n'
                clientsocket.send(_.encode('utf-8'))
                choose = clientsocket.recv(1024).decode('utf-8')

                if choose == '1':
                    users, login = User.sign_in(clientsocket, users, login, 1)
                    return (users, login)
                elif choose == '2':
                    pass
                elif choose == '3':
                    clientsocket.send('Goodbye! -1+3$5%1'
                                      .encode('utf-8'))
                    clientsocket.close()
                    print('Client close!')
                    raise ValueError
                    return (users, login)
                else:
                    clientsocket.send('\n Out of range!'.encode('utf-8'))

    def sign_in(clientsocket, users, login='', type=2):
        if type == 1:
            clientsocket.send(('\n Your login is ' + login).encode('utf-8'))
            _ = ' 1 - Ok\n'
            _ += ' 2 - Another login'
            clientsocket.send(_.encode('utf-8'))
            choose = clientsocket.recv(1024).decode('utf-8')

            if choose == '1':
                clientsocket.send('Ok\n'.encode('utf-8'))
            elif choose == '2':
                _ = ''
                clientsocket.send('  '.encode('utf-8'))
                while True:
                    clientsocket.send('\n Enter you login(name):'
                                      .encode('utf-8'))
                    new_login = clientsocket.recv(1024).decode('utf-8')
                    if new_login in users:
                        clientsocket.send('\n This login is already used!'
                                          .encode('utf-8'))
                        _ += ' 1 - try to input again\n'
                        _ += ' 2 - use old login\n'
                        _ += ' 3 - exit'
                        clientsocket.send(_.encode('utf-8'))
                        choose = clientsocket.recv(1024).decode('utf-8')

                        if choose == '1':
                            pass
                        elif choose == '2':
                            break
                        elif choose == '3':
                            clientsocket.send('Goodbye! -1+3$5%1'
                                              .encode('utf-8'))
                            clientsocket.close()
                            print('Client close!')
                        else:
                            _ = '\n Out of range!'.encode('utf-8')
                    else:
                        login = new_login
                        clientsocket.send('\n This login is OK'
                                          .encode('utf-8'))
                        break

        elif type == 2:
            clientsocket.send('\n Now you will registrated!'.encode('utf-8'))
            _ = ''
            while True:
                clientsocket.send('\n Enter you login(name):'
                                  .encode('utf-8'))
                new_login = clientsocket.recv(1024).decode('utf-8')
                if new_login in users:
                    clientsocket.send('\n This login is already used!\n'
                                      .encode('utf-8'))
                    _ += ' 1 - try to input again\n'
                    _ += ' 2 - exit'
                    clientsocket.send(_.encode('utf-8'))
                    choose = clientsocket.recv(1024).decode('utf-8')
                    clientsocket.send('Ok\n'.encode('utf-8'))
                    if choose == '1':
                        pass
                    elif choose == '2':
                        clientsocket.send('Goodbye! -1+3$5%1'
                                          .encode('utf-8'))
                        clientsocket.close()
                        print('Client close!')
                    else:
                        _ = '\n Out of range!'.encode('utf-8')
                else:
                    login = new_login
                    clientsocket.send('\n This login is OK'
                                      .encode('utf-8'))
                    break
        clientsocket.send('\n Enter your password:'.encode('utf-8'))
        password = clientsocket.recv(1024).decode('utf-8')
        clientsocket.send(('\n You are registred, ' + login)
                          .encode('utf-8'))
        print('Client registred!', login)
        users = Data.add_user(users, login, password)
        User.create_file(login)

        return users, login

    def create_file(login):
        f = open('users\\' + login + '.txt', 'w')
        f.write('Created at ' + str(datetime.datetime.today()
                                    .strftime('%d.%m.%y %H:%M:%S')) + '\n')
        f.close()

    def add_to_file(clientsocket, login):
        clientsocket.send('\n Please, enter text'.encode('utf-8'))
        clientsocket.send(' '.encode('utf-8'))
        text = clientsocket.recv(1024).decode('utf-8')

        clientsocket.send('\n Got a text'.encode('utf-8'))

        _ = ''

        while True:
            pass
            _ += '\n  1 - private note\n'
            _ += ' 2 - public note \n'

            clientsocket.send(_.encode('utf-8'))

            choose = clientsocket.recv(1024).decode('utf-8')

            if choose == '1':
                User.add_to_private_file(login, text)
                break
            elif choose == '2':
                Data.add_to_public_file(login, text)
                break
            else:
                clientsocket.send('\n Out of range, try again!'
                                  .encode('utf-8'))
        clientsocket.send('\n Added to file!'.encode('utf-8'))
        return text

    def add_to_private_file(login, text):
        f = open('users\\' + login + '.txt', 'a+t')
        text = str(datetime.datetime.today()
                   .strftime('%d.%m.%y %H:%M:%S')) + '  ' + text + '\n'
        f.write(text)
        f.close()

    def print_private(login) -> str:
        f = open('users\\' + login + '.txt', 'rt')
        text = f.read()
        f.close()
        return text


def main():
    users = Data.open_users()
    public = Data.open_public()

    while True:
        try:
            print('server is waiting!')
            server.listen(5)

            clientsocket, addr = server.accept()
            print('Got a connection from {}'.format(addr))

            _ = '\nPlease choose: \n'
            _ += '1 - log in \n'
            _ += 'any another - sign in\n'

            clientsocket.send(_.encode('utf-8'))
            choose = clientsocket.recv(1024).decode('utf-8')

            if choose == '1':
                users, login = User.log_in(clientsocket, users)
            else:
                users, login = User.sign_in(clientsocket, users)

            _ = '\nPlease choose: \n'
            _ += '1 - out public chat\n'
            _ += '2 - out private chat\n'
            _ += '3 - add new note\n'
            _ += '0 - Close connection :('

            while True:
                try:
                    clientsocket.send(_.encode('utf-8'))
                    choose = clientsocket.recv(1024).decode('utf-8')
                    print(choose)
                    if choose == '0':
                        clientsocket.send('\nGoodbye, '.encode('utf-8'))
                        clientsocket.send('-1+3$5%1'.encode('utf-8'))
                        clientsocket.close()
                        break

                    elif choose == '1':
                        text = 'Public notes:\n'
                        text += public
                        clientsocket.send(text.encode('utf-8'))

                    elif choose == '2':
                        text = 'Private notes:\n'
                        text += User.print_private(login)
                        clientsocket.send(text.encode('utf-8'))

                    elif choose == '3':
                        public += User.add_to_file(clientsocket, login)

                    else:
                        fail = '\nIt`s out of numbers!'
                        clientsocket.send(fail.encode('utf-8'))
                except OSError:
                    print('Disconnect!')
                    break
        except ValueError:
            print('Disconnect!')
            continue
        except ConnectionResetError:
            print('Strong disconnect!')
            continue


if __name__ == '__main__':
    main()
