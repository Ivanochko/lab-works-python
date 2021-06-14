#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server
import cgi
import math


class HTML:
    form_do = b'''
    <html>
        <head>
            <title>Area of triangle!</title>
            <style type="text/css">
                html{
                    background-color: black;
                    color: white;
                }
                #forma{
                    width: 400px;
                    margin: auto;
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <form method="post" id="forma">
                <br>
    '''
    form = b'''
                <label>Please input values</label> <br>
                A = <input type="text" name="a"> <br>
                B = <input type="text" name="b"> <br>
                C = <input type="text" name="c"> <br> <br>
                <input type="submit" value="Submit">
    '''
    form_after = b'''
            </form>
        </body>
    </html>
    '''


class View:
    def post_app(environ, start_response):
        html = HTML.form
        if environ['REQUEST_METHOD'] == 'POST':

            post = Triangle.get_post(environ)

            a = float(post['a'].value.encode('utf-8'))
            b = float(post['b'].value.encode('utf-8'))
            c = float(post['c'].value.encode('utf-8'))

            if Triangle.check(a, b, c):
                html = b'Area is: ' + str(Triangle
                                          .get_area(a, b, c)).encode('utf-8')
            else:
                html = b'Triangle cannot exist!'

        start_response('200 OK', [('Content-Type', 'text/html')])
        return [HTML.form_do + html + HTML.form_after]


class Triangle:
    def check(a, b, c):
        if a + b < c or a + c < b or b + c < a:
            return False
        return True

    def get_area(a, b, c):
        p = (a + b + c) / 2
        area = p * (p - a) * (p - b) * (p - c)
        return math.sqrt(area)

    def get_post(environ):
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''

        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        return post


servak = make_server('localhost', 8000, View.post_app)
print("Serving HTTP on port 8000...")
servak.serve_forever()
