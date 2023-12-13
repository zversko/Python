import logger

def contact_finder(file_csv, fieldnames):
    """
    Поиск ученика в основной базе.
    Поиск может осуществляться по нескольким параметрам через пробел.
    :param file_csv: Путь к файлу с основной базой
    :param fieldnames: Список с заголовками
    """
    logger.info('called method contact_finder: file ' + file_csv)
    seeker = str(input('Введи текст для поиска > '))
    print('')
    seeker = seeker.lower().split()
    with open(file_csv, 'r', encoding='utf8') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if line.strip() == '':
                continue
            else:
                seeker_line = line.strip()
                seeker_line_for_search = seeker_line.split(',', 1)[1].lstrip()
                for i in range(0, len(seeker)):
                    if seeker_line_for_search.lower().find(seeker[i]) != -1:
                        if seeker[i] == seeker[-1]:
                            seeker_line = line.strip().split(',')
                            contact_output(seeker_line, fieldnames)
                            count += 1
                            print('')
                        else:
                            continue                            
        print('Найдено совпадений: ', count)
        print('')
    

def contact_output(seeker_line, fieldnames):
    """
    Вывод найденных данных на экран построчно.
    :param seeker_line: Строка с найденными данными, переведенная в список.
    :param fieldnames: Список с заголовками
    """
    for i in range(len(fieldnames)):
        print(f'{fieldnames[i]} : {seeker_line[i]}')