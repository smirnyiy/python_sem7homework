def person_to_find():
    return input('Введите информацию для поиска: ')


def choose_mode():
    return input('------------------------------------------------------------------------------------\n\
"1" - Ввод новых данных, \
"2" - Поиск по базе, \
"3" - Выход из программы \
\nВыберите комманду: ')


def new_person():
    name = input('Введите имя: ')
    telephone = input('Введите номер: ')
    return f'{name} | {telephone}'


def show_found(result):
    print('Результаты поиска: ')
    for i in result:
        print(i)