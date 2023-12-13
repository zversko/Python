import csv
import re
import logger

def shcoolchildren_transfer(file_csv, file_csv_new, fieldnames):
    """
    Импортирование нового справочника(csv файл) в основной справочник.
    Так же осуществляется перевод учеников в другой класс (Колонка Пометка_перевода)
    :param file_csv_new: Путь к базе, в которую надо экспортировать основную базу
    :param file_csv: Путь к файлу с основной базой
    :param fieldnames: Список с заголовками
    """
    logger.info('called method read_base_and_write_csv_file: file ' + file_csv + ' new file csv = ' + file_csv_new)
    print('')
    with open(file_csv, encoding='utf8', newline='') as csvfile_in:
        reader = csv.DictReader(csvfile_in)
        with open(file_csv_new, 'a', encoding='utf8', newline='') as csvfile_out:
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                string = int(row['Класс']) + 1
                if row['Пометка_перевода'] != 'NONE':
                    litera = re.findall(r'[А-Д]+', row['Пометка_перевода'])
                    class_ = re.findall(r'\d+', row['Пометка_перевода'])
                    row[fieldnames[-1]] = 'NONE'
                    row[fieldnames[4]] = class_[0]
                    row[fieldnames[5]] = litera[0]
                    writer.writerow({fieldnames[i]: row[fieldnames[i]] for i in range(len(fieldnames))})
                    print(f'{row[fieldnames[1]]} {row[fieldnames[2]]} {row[fieldnames[3]]} перевелся в {class_}{litera} класс')    
                elif string == 12:
                    print(f'{row[fieldnames[1]]} {row[fieldnames[2]]} {row[fieldnames[3]]} окончил школу')
                else:
                    row[fieldnames[4]] = str(string) 
                    writer.writerow({fieldnames[i]: row[fieldnames[i]] for i in range(len(fieldnames))})
    print('')