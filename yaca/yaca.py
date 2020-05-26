import requests, csv
from bs4 import BeautifulSoup


def get_html(url):
    print('get_html')
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    print('write_csv')
    with open('yaca.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['price'],
                         data['url'],))


def refine_price(pr):
    price = pr.split(' ')  # разбил по пробелу
    price.pop()  # удалил последний элемент
    return ''.join(price)  # склеил список


def get_page_data(html):
    print('get_page_data')
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('div', class_="rel listHandler").find('table', id='offers_table').find('tbody').find_all('tr', class_='wrap')

    for tr in trs:
        name = tr.find('td', class_='title-cell').find('strong').text
        dirty_url = tr.find('td', class_='title-cell').find('a').get('href')  # очистить URL
        url = dirty_url.split('#')[0]
        pr = tr.find('p', class_='price').find('strong').text  # очистить price
        price = refine_price(pr)
        print(name, price, url)
        data = {
            'name': name,
            'price': price,
            'url': url,
        }
        write_csv(data)


def main():
    pattern = 'https://www.olx.ua/nedvizhimost/kvartiry-komnaty/artemovsk/?page={}'
    for i in range(1,4):
        url = pattern.format(str(i))
        get_page_data(get_html(url))
        print(url)


if __name__ == '__main__':
    main()
