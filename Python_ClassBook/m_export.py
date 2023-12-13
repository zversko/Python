import csv
import logger

def export_class_in_txt_file(file_csv, output_txt, сlass_, litera):
    """
    Экпорт одного класса в *.txt файл
    :param file_csv: Путь к файлу с основной базой
    :param output_txt: Путь, куда будет направлен выборочный список
    :param сlass_: Параметр - класс
    :param litera: Параметр - литера
    """
    logger.info('called method export_class_in_txt_file with: from file ' + file_csv + ' file output_txt = ' + output_txt + ' klass ' + сlass_)
    with open(output_txt, 'w', encoding='utf8') as txtfile:
        with open(file_csv, encoding='utf8', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            titles = reader.fieldnames
            count = 0
            for row in reader:
                if row['Класс'] == сlass_ and row['Литера'] == litera:                 
                    for i in range(len(titles)):
                        txtfile.write(f'{titles[i]} : {row[titles[i]]} \n')
                    txtfile.write('\n')
                    count += 1
            print('')
            print('Найдено совпадений: ', count)
            print('')

def export_in_txt_file(file_csv, output_txt):
    """
    Экпорт всего списка в *.txt файл
    :param file_csv: Путь к файлу с основной базой
    :param output_txt: Путь, куда будет направлен выборочный список
    """
    logger.info('called method export_class_in_txt_file with: from file ' + file_csv + ' file output_txt = ' + output_txt)
    with open(output_txt, 'w', encoding='utf8') as txtfile:
        with open(file_csv, encoding='utf8', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            titles = reader.fieldnames
            for row in reader:
                for i in range(len(titles)):
                    txtfile.write(f'{titles[i]} : {row[titles[i]]} \n')
                txtfile.write('\n')