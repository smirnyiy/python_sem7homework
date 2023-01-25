import csv

def get_base():
    with open('data.txt', "r", encoding='utf-8') as file:
        return file.read()


def add_person(person):
    try:
        with open('data.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n{person}')
        with open('data.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([person.split(' | ')])
    except FileNotFoundError:
        with open('data.txt', 'w', encoding='utf-8') as file:
            file.write(f'{person}')
        with open('data.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([person.split(' | ')])
