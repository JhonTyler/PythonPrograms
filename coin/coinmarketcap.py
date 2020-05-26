import csv
import requests
from bs4 import BeautifulSoup
import re

def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((
            data['name'],
            data['url'],
            data['price'],
        ))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find_all('tr', class_='cmc-table-row')
    for tr in trs:
        name = tr.find('div', class_='cmc-table__column-name').find('a').text
        url = 'https://coinmarketcap.com' + tr.find('div', class_='cmc-table__column-name').find('a').get('href')
        price = tr.find('td', class_='cmc-table__cell--sort-by__price').find('a').text.replace('$', '').replace(',','')

        data = {
            'name': name,
            'url': url,
            'price': price
        }
        write_csv(data)
    try:
        next100 = soup.find('div', class_='cmc-table-listing__pagination').find('a', text=re.compile('Next')).get('href')
    except:
        print('Finish')
        return False
    return next100.strip('/')


def main():
    url = 'https://coinmarketcap.com/'
    next100 = '1'
    while next100:  # перебор с помощью регулярных выражений
        next100 = get_page_data(get_html(url+next100))
        print(next100)
    # for i in range(27):  # перебор по количеству страниц
    #     get_page_data(get_html(url+str(i)))



if __name__ == '__main__':
    main()
