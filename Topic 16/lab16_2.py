import requests
from bs4 import BeautifulSoup
import re


def get_items():
    url = 'https://price.ua/catc839t14.html'

    _ = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    _ += '(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    headers = {'User-agent': _}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    items = soup.find_all('div', class_='product-block-shadow')

    return items


def get_photo(item):
    return item.find_all('a')[1].span.img.attrs['src']


def get_src(item):
    return item.find_all('a')[0].attrs['href']


def get_name(item):
    return item.find_all('a')[0].text


def get_price(item):
    return re.sub('\D', '', item.span.text)


def get_descript(item):
    i = item.find('div', class_='characteristics_overlay')
    char = i.find_all('div', class_='short-descr-line')
    return {'diagonal': char[0].span.text,
            'processor': char[1].span.text,
            'freq': char[2].span.text,
            'screen': char[3].span.text,
            'video': char[4].span.text}


def get_information(items):
    desc = {'diagonal': 'Diagonal', 'processor': 'Processor',
            'freq': 'Frequency', 'screen': 'Screen', 'video': 'Video'}

    information = [{'name': 'Name',
                    'price': 'Price',
                    'descript': desc,
                    'item': 'Item',
                    'photo': 'Photo'}]

    for i in items:
        temp = i.find('div', class_='white-wrap')
        temp2 = i.find('div', class_='price-wrap')

        information.append({'name': get_name(temp),
                            'photo': get_photo(temp),
                            'item': get_src(temp),
                            'descript': get_descript(temp),
                            'price': get_price(temp2)})
    return information


def out_desc(desc):
    _ = desc['diagonal'] + '|'
    _ += desc['processor'] + '|'
    _ += desc['freq'] + '|'
    _ += desc['screen'] + '|'
    _ += desc['video']
    return _


def check(dict_):
    if dict_['price'] == 'Price':
        return True
    if int(dict_['price']) > 20000 and int(dict_['price']) < 40000:
        return True
    return False


def out_information(information):
    f = open('items.csv', 'w')
    f.write('sep=|\n')
    for i in information:
        if check(i):
            _ = i['name'] + '|'
            _ += str(i['price']) + '|'
            _ += out_desc(i['descript']) + '|'
            _ += i['item'] + '|'
            _ += i['photo'] + '|\n'
            f.write(_)
    f.close()


def main():
    items = get_items()

    information = get_information(items)

    out_information(information)


if __name__ == '__main__':
    main()
