import csv
import datetime
import os

path = "c:/Users/homei/OneDrive/Рабочий стол/Projects/Totalwork_Python/data.csv"

def read_id():
    if os.path.exists(path) and os.path.getsize(path) > 0:
        data_list = read_csv()
        return data_list[len(data_list)-1][0]
    else:
        return 0

def note_add(title, text, id):        
    now_str = datetime.datetime.today().strftime('%d.%m.%Y')  
    list_of_data = []
    list_of_data.append(id)
    list_of_data.append(title)
    list_of_data.append(text) 
    list_of_data.append(now_str)

    if len(list_of_data)==4: 
        write_csv(list_of_data)
        
    else: input("Something wrong!!! Нажмите <ENTER>...")
  
def print_fine(data_list):
    print("\n{a:5s} | {b:25s} | {c:55s} | {d:10s} ".format(a="id", b="Заголовок", c="Текст", d="Дата"))
    print("--------------------------------------------------------------------------------------------------------")
    for i in range(len(data_list)):
        print("{a:5s} | {b:25s} | {c:55s} | {d:10s} ".format(a=data_list[i][0], b=data_list[i][1], c=data_list[i][2], d=data_list[i][3]))
            
    
def filter_list(data_f):

    def filter_data(data):
 
        dt = data[3].split('.') 
        dt_f = data_f.split('.') 
        if dt[2]>=dt_f[2] and dt[1]>=dt_f[1] and dt[0]>=dt_f[0]:
            return True
        else:
            return False
        
    out_filter = list(filter(filter_data, read_csv()))
    print_fine(out_filter)


def notes_read():

    data_list = read_csv()
    print_fine(data_list)
        
def notes_read_sort(col):
 
    def col_number(notes):
        return notes[col]
    
    data_list = read_csv()        
    for i in range(len(data_list)):
        dt=data_list[i][3].split('.')
        data_list[i][3]=dt[2]+'.'+dt[1]+'.'+dt[0]
    data_list.sort(key=col_number)
    print("\nОтсортировали по дате: \n")
    print_fine(data_list)
  
    
def notes_del(id):
    data_list = read_csv()
    for i in range(len(data_list)-1):
        if data_list[i][0] == id:
            data_list.pop(i)
    print_fine(data_list)  
    rewrite_csv(data_list)
    
    
def read_csv():
    with open(path, newline='\n', encoding = 'utf-8') as File:  
            reader = csv.reader(File, delimiter=';', lineterminator='\n')
            file_reader = []        
            for row in reader:
                file_reader.append(row)
            file_reader.sort()
      
    return file_reader
    

def write_csv(array):
    with open(path, mode ='a', encoding='utf-8') as file:
     
        file_writer = csv.writer(file, delimiter=';', lineterminator='\n')
        file_writer.writerow(array)
        
def rewrite_csv(array):
    with open(path, mode ='w', encoding='utf-8') as file:
    
        file_writer = csv.writer(file, delimiter=';', lineterminator='\n')
        for row in array:
            file_writer.writerow(row)