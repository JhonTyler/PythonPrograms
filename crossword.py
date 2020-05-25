import requests, json, csv
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('pazzl.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['solution'],
                         data['clue']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    crossword = soup.find('div', class_='js-crossword').get('data-crossword-data')
    return crossword


def main():
    url = 'https://www.theguardian.com/crosswords/quick/15594'
    json_obj = get_data(get_html(url))
    d = json.loads(json_obj)
    for i in d["entries"]:
        write_csv(i)


if __name__ == '__main__':
    main()
