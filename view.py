


def run ():
    while True:
        print('\n\
            1 - Создать заметку\n\
            2 - Посмотреть заметку\n\
            3 - Посмореть все заметки\n\
            4 - Откорректировать заметку\n\
            5 - Удалить заметку\n\
            0 - Выход')
        task = int(input('Выберите действие: '))
        match task:
            case 1: write()
            case 2: read()
            case 3: read_all()
            case 4: rewrite()
            case 5: delete()
            case 0: print ('Хорошего дня, до встречи') 
        break

