import logger
import model
import view

def run():
    while True:
        mode = view.choose_mode()
        if mode == '1':
            person = view.new_person()
            logger.add_person(person)
        elif mode == '2':
            person = view.person_to_find()
            base = logger.get_base()
            result = model.serch_person(base, person)
            view.show_found(result)
        elif mode == '3':
            return False
        else:
            print('Некорректная команда')