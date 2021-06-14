import requests
from bs4 import BeautifulSoup
import re


user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
user += '(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

headers = {'User-agent': user}


def connect():
    url = 'https://if.isuo.org/authorities/schools-list/id/630'
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, 'lxml')


def decode_mail(string):
    string = string.replace('%', '')
    string = bytes.fromhex(string).decode('utf-8')
    left = string.find('>')
    right = string.rfind('<')
    return string[left + 1: right]


def set_string(string):
    string = string.replace('\n', '').replace('\r', '')
    return string.strip()


def get_list_links(soup):
    table = soup.find_all('table', class_='zebra-stripe list')
    elems = table[0].find_all('tr')
    links = []
    names = []

    for i in range(1, len(elems)):
        temp = elems[i].find_all('td')
        names.append(set_string(temp[1].text))
        links.append('https://if.isuo.org/' + temp[1].a.attrs['href'])

    return links, names


def find_phone(soup):
    r = re.findall(r'\(?0\d{2,4}\)?\d{1,2}-?\d{2}-?\d{1,3}', soup.text)
    print(r)


def get_information(links):
    phones = []
    emails = []
    directors = []
    amounts = []
    post = []
    for url in links:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find_all('table', class_='zebra-stripe')
        rows = table[0].find_all('tr')
        for i in range(len(rows)):
            if 'Телефони:' in rows[i].text:
                phones.append(str(rows[i].td)[4:-5])
            elif 'E-mail:' in rows[i].text:
                onclick = rows[i].td.a.attrs['onclick']
                email = onclick[25:-26]
                emails.append(decode_mail(email))
            elif 'Директор:' in rows[i].text:
                directors.append(rows[i].td.text)
            elif 'Кількість учнів:' in rows[i].text:
                amounts.append(rows[i].td.text)
            elif 'Поштова адреса' in rows[i].text:
                post.append(rows[i].td.text)

    return phones, emails, directors, amounts, post


def out(names, phones, emails, directors, amounts, post):
    f = open('schools.csv', 'w')
    f.write('sep=|\n')
    f.write('Name|Phone|Email|Director|Amount Of Pupils|Post|\n')

    for i in range(len(names)):
        _ = names[i] + "|"
        _ += phones[i] + '|'
        _ += emails[i] + '|'
        _ += directors[i] + '|'
        _ += amounts[i] + '|'
        _ += post[i] + '|\n'
        f.write(_)

    f.close()


def main():
    soup = connect()
    links, names = get_list_links(soup)
    phones, emails, directors, amounts, post = get_information(links)
    # out(names, phones, emails, directors, amounts, post)


if __name__ == '__main__':
    main()
