#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import mysql.connector
import cgi
from mysql.connector import Error
from wsgiref.simple_server import make_server

CODE_HTML_BEFORE = '''
<html>
    <head>
        <title>Atestation teachers!</title>
        <meta charset="utf-8">
        <style type="text/css">
            html{
                background-color: #ffffe0;
                color: white;
            }
            #container{
                margin: auto;
                width: 1000px;
                margin-top: 60px;
                height: 600px;
                text-align: center;
                background: #777125;
                border: 1px solid white;
                box-shadow: 0 0 5px white, 0 0 15px gray;
            }
            #button1{
                border-radius: 10px;
                height: 35px;
                width: 200px;
                background-color: #a9a357;
                border: 4px solid #4f4900;
                box-shadow: 0 0 3px #4f4900, inset 0 0 3px #4f4900,
                            0 0 5px #efe99d;
                font-family: 'Chilanka', cursive;
                cursor: pointer;
                transition: all 1.2s;
            }
            #button1:hover{
                background-color: #4f4900;
                color: #a9a357;
                box-shadow: 0 0 10px #c7c175;
                transition: all 0.8s;
            }
            #button1:active{
                background-color: #59530a;
                color: #e5df93;
                outline: none;
                box-shadow: 0 0 10px #958f43, 0 0 15px #958f43;
                transition: all 0.2s;
            }
            #button1:visited{
                outline: none;
            }
            #table_atestation{
                width: 800px;
                margin: auto;
                margin-top: 35px;
                border-collapse: collapse;
                box-shadow: 0 0 5px white;
            }
            .td_1, .td_2, .td_3, .td_4, .td_5, th{
                border: 1px solid white;
                padding: 3px;
            }
            .td_1{
                width: 350px;
            }
            .td_2{
                text-align: center;
                width: 150px;
            }
            .td_3, .td_4, .td_5{
                width: 110px;
                text-align: center;
            }
            .image{
                width: 600px;
                margin: auto;
                margin-top: 20px;
                border-radius: 40px;
                box-shadow: 5px 5px 7px #4f4900;
            }
        </style>
    </head>
    <body>
        <div id="container">
            <form method="post">
'''.encode('utf-8')
CODE_HTML = '''
                <h1> База даних "Атестація вчителів" </h1>
                <p> Натисніть на кнопку, щоб отримати інформацію про вчителів,
                 кому потрібно пройти атестацію </p>
                <input type="submit" id="button1" name="button1"
                 value="Отримати дані!"><br>
                <img
src="https://www.elearningmaster.ru/pluginfile.php/5202/course/overviewfiles/WOW_2_pic.png"
                class="image">
'''.encode('utf-8')
CODE_HTML_AFTER = '''
            </form>
        </div>
    </body>
</html>
'''.encode('utf-8')


def create_connection(host_name, user_name, user_password, user_database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=user_database
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def get_query_result(cursor):
    query = """SELECT Teachers_personal.name, date_last_atestation, category,
                        experience, Schools.name
               FROM Teachers_profesional
            JOIN Teachers_personal
            ON teachers_profesional.id_teacher = teachers_personal.id_teacher
            JOIN Teachers_schools
            ON Teachers_profesional.id_teacher = Teachers_schools.id_teacher
            JOIN Schools ON Teachers_schools.id_school = Schools.id_school
               WHERE date_last_atestation + INTERVAL 5 YEAR < CURDATE();"""

    cursor.execute(query)
    return cursor.fetchall()


def get_table(result):
    table = []

    table.append("""<h2>Вчителі кому обов'язково потрібно пройти атестацію:
                 </h2>
                <table id="table_atestation"><tr><th>Ім'я</th>
                <th class="td_2">Дата останньої атестації</th>
                <th>Категорія</th><th>Досвід</th>
                <th>Школа</th></tr>""".encode('utf-8'))
    for x in result:
        string = '<tr>'
        index = 0
        for y in x:
            index += 1
            string += '<td class="td_{0}">'.format(index) + str(y) + '</td>'
        table.append((string + '</tr>').encode('utf-8'))
    return table


def set_result_to_string(result):
    string = ''.encode('utf-8')
    for i in result:
        string += i
    return string


def post_app(environ, start_response):
    html = CODE_HTML
    if environ['REQUEST_METHOD'] == 'POST':

        result = get_query_result(mycursor)
        result = get_table(result)
        html = set_result_to_string(result)

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [CODE_HTML_BEFORE + html + CODE_HTML_AFTER]


def get_post(environ):
    post_env = environ.copy()
    post_env['QUERY_STRING'] = ''

    post = cgi.FieldStorage(
        fp=environ['wsgi.input'],
        environ=post_env,
        keep_blank_values=True
    )
    return post


connection = create_connection("localhost",
                               "root",
                               "Ivanochko1",
                               "Atestation")

mycursor = connection.cursor()

servak = make_server('localhost', 8000, post_app)
print("Serving HTTP on port 8000...")
servak.serve_forever()
