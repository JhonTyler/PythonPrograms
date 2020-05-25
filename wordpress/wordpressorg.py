import requests, csv
from bs4 import BeautifulSoup


def get_html(url):
    print('get_html')
    r = requests.get(url)
    return r.text


def refind(s):
    print('refind')
    # 1,488 total ratings
    r = s.split(' ')[0]  # разбил строку по пробелу и взял первый элемент
    result = r.replace(',','')  # удалил запятые
    return result


def write_csv(data):
    print('write_csv')
    with open('plugins.csv', 'a') as f:  # создал\открыл файл с возможностью дозаписи
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['url'],
                         data['rating'],))  # дозаписал в файл кортеж из трех элементов


def get_data(html):  # выборка информации из страницы
    print('get_data')
    soup = BeautifulSoup(html, 'lxml')
    featured = soup.find_all('section')[1]
    plugins = featured.find_all('article')
    for plugin in plugins:
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a').get('href')
        r = plugin.find('span', class_='rating-count').find('a').text
        rating = refind(r)
        data = {'name': name,
                'url': url,
                'rating': rating}
        write_csv(data)  # отправил на запись


def main():
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
