#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import datetime

host = '127.0.0.1'
port = 9999

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((host, port))


while True:
    serversocket.listen(5)
    print('Server is waiting!')

    clientsocket, addr = serversocket.accept()
    print('Got a connection from {}'.format(addr))

    clientsocket.send('What is your name?'.encode('utf-8'))

    client_name = clientsocket.recv(1024)

    clientsocket.send('Hello, '.encode('utf-8') + client_name)

    print('It is  ', client_name.decode('utf-8'))

    _ = '\nPlease choose: \n'
    _ += '1 - What is your name?\n'
    _ += '2 - What is my name?(server)\n'
    _ += '3 - What day is now?\n'
    _ += '4 - What hour is now?\n'
    _ += '5 - When will be exam of Python?\n'
    _ += '0 - Close connection :('

    while True:

        clientsocket.send(_.encode('utf-8'))

        choose = clientsocket.recv(1024).decode('utf-8')

        print(choose)

        if choose == '0':
            clientsocket.send('\nGoodbye, '.encode('utf-8') + client_name)
            clientsocket.send('-1+3$5%1'.encode('utf-8'))
            clientsocket.close()
            break

        elif choose == '1':
            massage = '\nYour name is '.encode('utf-8')
            clientsocket.send(massage + client_name)

        elif choose == '2':
            massage = '\n My name is Pythonchik, I am server!'
            clientsocket.send(massage.encode('utf-8'))

        elif choose == '3':
            temp = datetime.datetime.today().strftime('%d.%m.%y')
            massage = '\n Now is ' + temp
            clientsocket.send(massage.encode('utf-8'))

        elif choose == '4':
            temp = datetime.datetime.today().strftime('%H:%M:%S')
            massage = '\n Now is ' + temp
            clientsocket.send(massage.encode('utf-8'))

        elif choose == '5':
            massage = '\n Python exam at 2021.01.19'
            clientsocket.send(massage.encode('utf-8'))

        else:
            fail = '\nIt`s out of numbers!'
            clientsocket.send(fail.encode('utf-8'))
