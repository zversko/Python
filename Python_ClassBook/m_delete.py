import csv
import logger

def search_id(id, file_csv):
    """
    Перед удалением необходимо убедиться, существуюет ли такая запись.
    Осуществуляется поиск по столбцу ID.
    :param file_csv: Путь к файлу с основной базой
    :param id: Уникальный ID для каждой записи
    """
    logger.info('request for search string: id =' + id + ', file ' + file_csv)
    with open(file_csv, encoding='utf8', newline='') as csvfile:
        print('')
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            if row['ID'] == id:                 
                delete_string(id, file_csv)
                print(f'Ученик с ID[{id}] удален')
                count += 1
        if count == 0:
            print(f'ID[{id}] - не найден')
        print('')

def delete_string(id, file_csv):
    """
    Удаляет запись(строку) по ID
    :param file_csv: Путь к файлу с основной базой
    :param id: Уникальный ID для каждой записи
    """
    logger.info('request for delete string: ' + id)
    file = open(file_csv, 'r', encoding='utf8')
    list_strings = file.readlines()
    file2 = open(file_csv, 'w', encoding='utf8')
            
    array = [line.split(',') for line in list_strings]
    [file2.write((','.join(i))) for i in array if not(i.__contains__(id))]


    file.close 
    file2.close
