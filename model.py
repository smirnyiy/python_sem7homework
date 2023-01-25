def serch_person(base, person):
    base = base.split('\n')
    serch = True
    result = []
    for i in base:
        if person in i:
            result.append(i)
            serch = False
    if serch:
        result.append(f'Контакт |{person}| не найден')
    return result