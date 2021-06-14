import requests
from bs4 import BeautifulSoup


def main():
    url = 'http://www.codeabbey.com/index/user_ranking'

    _ = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    _ += '(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    headers = {'User-agent': _}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    peoples = soup.find_all('tr', class_='centered none')

    f = open('rank.csv', 'wt')

    f.write('sep=|\n')

    for i in peoples:
        temp = i.find_all('td')
        _ = temp[2].a.text + '|'
        _ += temp[3].text + '|'
        _ += temp[4].text + '|'
        _ += temp[5].text + '|\n'
        f.write(_)

    f.close()


if __name__ == '__main__':
    main()
