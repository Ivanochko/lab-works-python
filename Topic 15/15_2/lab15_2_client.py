#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

host = '127.0.0.1'
port = 9999


def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serversocket.connect((host, port))

    while True:
        server_responve = serversocket.recv(1024)

        if '-1+3$5%1' in server_responve.decode('utf-8'):
            print(server_responve.decode('utf-8')[:-8])
            serversocket.close()
            return

        print(server_responve.decode('utf-8'))

        a = input()

        serversocket.send(a.encode('utf-8'))

        server_responve = serversocket.recv(1024)

        if '-1+3$5%1' in server_responve.decode('utf-8'):
            print(server_responve.decode('utf-8')[:-8])
            serversocket.close()
            return

        print(server_responve.decode('utf-8'))


if __name__ == '__main__':
    main()
