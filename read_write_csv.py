import csv

def write_csv(data):
    with open('file.csv', 'a') as f:
        writer = csv.writer(f)  # записывает файл
        writer.writerow((
            data['name'],
            data['surname'],
            data['age'],
        ))

def write_csv2(data):
    with open('file.csv', 'a') as f:
        order = ['name', 'surname', 'age']
        wrirer = csv.DictWriter(f, fieldnames=order)  #записывает файл как словарь
        wrirer.writerow(data)

def reder_csv(file_name):
    with open(file_name) as f:
        order = ['name', 'surname', 'age']
        reader = csv.DictReader(f, fieldnames=order)  # читиет файл как словарь

        for row in reader:
            print(dict(row))

def main():
    d = {'name': 'Peter', 'surname': 'Ivanov', 'age': 21}
    d1 = {'name': 'Ivan', 'surname': 'Ivanov', 'age': 18}
    d2 = {'name': 'Ksu', 'surname': 'Petrova', 'age': 32}
    l = [d, d1, d2]
    # for i in l:
    #     write_csv(i)
    reder_csv('file.csv')


if __name__ == '__main__':
    main()
