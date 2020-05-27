import requests
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('websites.csv', 'a') as f:
        order = ['link', 'rating', 'percent']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def main():
    for st in range(1, 2786):
        print(st)
        url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'.format(str(st))
        d = get_html(url).strip().split('\n')[1:]
        for i in d:
            row = i.split('\t')
            data = {
                'link': row[1],
                'rating': row[3],
                'percent': row[4]
            }
            write_csv(data)


if __name__=='__main__':
    main()
