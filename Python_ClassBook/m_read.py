import csv
import logger

def read_base_and_display(file_csv, fieldnames):
    """
    Вывод на экран основной базы
    :param file_csv: Путь к файлу с основной базой
    :param fieldnames: Список с заголовками
    """
    logger.info('called method read_base_and_display: file ' + file_csv)
    with open(file_csv, encoding='utf8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print('')
        for row in reader:
            string = [row[i] for i in fieldnames]
            print(*string[1:7])
        print('')