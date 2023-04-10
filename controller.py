import datetime
import function as f
import view as v


def run():    
    make = ' '
    while make != 0:
        v.menu()
        make = input("\nВыберите действие: ") 
        match make:
            case "1":
                print("\nСоздаем новую заметку")
                title = input("Введите заголовок: ")
                text = input("Введите текст: ")
                id = f.read_id()
                f.note_add(title,text,int(id)+1)
                print("Заметка добавлена!")
                
            case "2":
                print("\nРедактируем заметку")
                f.notes_read()
                id = input("Введите id заметки: ")
                f.notes_del(id)
                title = input("Введите заголовок: ")
                text = input("Введите текст: ")
                f.note_add(title,text,id)
                print("Заметка заменена!")
                
            case "3":
                print("\nУдаляем заметку")
                f.notes_read()
                id = input("Введите id заметки: ")
                f.notes_del(id)
                print("Заметка удалена!")
            
            case "4":
                print("\nЗаметки списком")
                f.notes_read()
                
            case "5":
                print("\nЗаметки, отсортированные по дате")
                sort_col=3
                f.notes_read_sort(sort_col)
                
            case "6":
                date_f = 0 
                while date_f == 0:
                    date_ = input("\nВведите дату для фильтра (ДД.ММ.ГГГГ): ")
                    try:
                        date_f = datetime.datetime.strptime(date_, '%d.%m.%Y')
                        # print("Дата корректна", date_f)
                        f.filter_list(date_)
                    except ValueError:
                        err = input("Введена некорректная дата. Введите 1, чтобы ввести ещё раз: ")
                        if err != "1": 
                            break
            case "0": 
                print("Хорошего дня, до встречи")
                break