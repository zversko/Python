import csv
import m_import
import m_delete
import logger

def search_id(id, file_csv, fieldnames):
    """
    Осуществляется поиск по ID.
    При нахождении такой записи, вызывается функция добавления
    новой записи с клавиатуры. 
    После чего старая записаь удаляется.
    :param file_csv: Путь к файлу с основной базой
    :param id: Уникальный ID для каждой записи
    :param fieldnames: Список с заголовками
    """
    logger.info('called method search_id with: id =' + id + ', file ' + file_csv)
    with open(file_csv, encoding='utf8', newline='') as csvfile:
        print('')
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            if row['ID'] == id:
                print('')
                for i in range(len(fieldnames)):
                    print(f'{fieldnames[i]} : {row[fieldnames[i]]}')
                print('')
                m_import.new_contact_keyboard_input(file_csv, fieldnames)
                m_delete.delete_string(id, file_csv)
                print(f'Старый ID[{id}] был удален')
                count += 1
        if count == 0:
            print(f'ID[{id}] - не найден')
        print('')
