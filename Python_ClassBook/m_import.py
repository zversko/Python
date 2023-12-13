import csv
import logger


def read_base_and_write_csv_file(file_csv_new, file_csv, fieldnames):
    """
    Импортирование нового справочника(csv файл) в основной справочник
    :param file_csv_new: Путь к базей, которую надо импортировать в основную базу
    :param file_csv: Путь к файлу с основной базой
    :param fieldnames: Список с заголовками
    """
    logger.info('called method read_base_and_write_csv_file with: file ' + file_csv + ' new file csv = ' + file_csv_new)
    last_id = read_last_id(file_csv)
    print('')
    with open(file_csv_new, encoding='utf8', newline='') as csvfile_in:
        reader = csv.DictReader(csvfile_in)
        with open(file_csv, 'a', encoding='utf8', newline='') as csvfile_out:
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            for row in reader:
                row[fieldnames[0]] = last_id
                writer.writerow({fieldnames[i]: row[fieldnames[i]] for i in range(len(fieldnames))})
                last_id = last_id + 1
    print('')

def new_contact_keyboard_input(file_csv, fieldnames):
    """
    Ввод нового ученика с клавиатуры
    :param file_csv: Путь к файлу с основной базой
    :param fieldnames: Список с заголовками
    """
    logger.info('called method new_contact_keyboard_input: file ' + file_csv)
    print('')
    print('Введите данные ученика')
    new_contact = []
    for i in range(1, len(fieldnames)):
        new_contact.append(str(input(f'{fieldnames[i]} : ')))
    if new_contact == '':
        new_contact.append('NONE')
    add_new_contact_in_base_shcoolchildren(new_contact, file_csv, fieldnames)
    print('')

def add_new_contact_in_base_shcoolchildren(new_contact, file_csv, fieldnames):
    """
    Построчное добавление нового ученика
    :param new_contact: Список с данным нового ученика
    :param file_csv: Путь к файлу с основной базой
    :param fieldnames: Список с заголовками
    """
    logger.info('called method add_new_contact_in_base_shcoolchildren: file ' + file_csv + ' new_contact = ' + new_contact)
    new_contact.insert(0, read_last_id(file_csv))
    with open(file_csv, 'a', encoding='utf8', newline='') as csvfile_out:
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames, restval=None)
            writer.writerow({fieldnames[i]: new_contact[i] for i in range(len(fieldnames))})

def import_base_shcoolchildren_txt_file(file_csv, fieldnames, file_txt):
    """
    Импортирование нового справочника из txt файла
    :param file_txt: Список с данными новых учениками
    :param file_csv: Путь к файлу с основной базой
    :param fieldnames: Список с заголовками
    """ 
    logger.info('called method import_base_shcoolchildren_txt_file: file ' + file_csv + ' file txt = ' + file_txt)
    with open(file_txt, 'r', encoding='utf8') as file:
        new_contact = []
        print('')
        lines = file.readlines()
        for line in lines:
            if line.strip() == '':
                continue
            else:
                new_contact = line.split()
            if len(new_contact) == 8:
                add_new_contact_in_base_shcoolchildren(new_contact, file_csv, fieldnames)
                print(new_contact)
                new_contact = []
            else:
                print(new_contact)
                new_contact = []
                print('Не соответствует формату базы')
        print('')

def read_last_id(file_csv):
    """
    Поиск в основной базе последнего ID
    :param file_csv: Путь к файлу с основной базой
    """  
    logger.info('called method read_last_id: file ' + file_csv)
    with open(file_csv, encoding='utf8', newline='') as csvfile:
        last_line = csvfile.readlines()[-1]
        last_line = last_line.strip().split(',')
        last_id = last_line[0]
        if last_id.isdigit() == False:
            last_id = 0
        else:
            last_id = int(last_id)
        return last_id + 1    
    
# def new_class(): 
#     with open('class.csv', 'w', encoding='utf8', newline='') as csvfile:
#         fieldnames = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Класс', 'Литера', 'Дата_рождения', 'Номер_телефона', 'Пометка_перевода']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval=None)

#         writer.writeheader()
#         writer.writerow({'ID': '1', 'Фамилия': 'Озерова', 
#             'Имя': 'Аделина', 'Отчество': 'Артемовна', 'Класс': '5', 'Литера': 'А', 'Дата_рождения': '10.10.2010', 
#             'Номер_телефона': '89123456789', 'Пометка': 'NONE'})