import csv
import os
import m_read
import m_search
import m_import
import m_export
import m_delete
import m_edit
import m_next_year
from os import system
from curses.ascii import isdigit

def choice_method(num):
    """
    Выбор метода для работы с базой.
    """
    fieldnames = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Класс', 'Литера', 'Дата_рождения', 'Номер_телефона', 'Пометка_перевода']
    file_csv = 'class.csv'
    if num == 1:
        os.system('dir')
        main()
        exit()
    elif num == 2:
        system("cls")
        m_read.read_base_and_display(file_csv, fieldnames)
        main()
        exit()
    elif num == 3:
        system("cls")
        file_csv_new = input('Введите файл *.csv > ')
        m_import.read_base_and_write_csv_file(file_csv_new, file_csv, fieldnames)
        main()
        exit()
    elif num == 4:
        system("cls")
        file_txt = input('Введите файл *.txt > ')
        m_import.import_base_shcoolchildren_txt_file(file_csv, fieldnames, file_txt)
        main()
        exit()
    elif num == 5:
        system("cls")
        m_import.new_contact_keyboard_input(file_csv, fieldnames)
        main()
        exit()
    elif num == 6:
        system("cls")
        file_txt = input('Введите файл *.txt куда необходимо сделать экспорт > ')
        m_export.export_in_txt_file(file_csv, file_txt)
        main()
        exit()
    elif num == 7:
        system("cls")
        сlass_ = input('Введите класс > ')
        litera = input('Введите литеру класс > ')
        file_txt = input('Введите файл *.txt куда необходимо сделать экспорт > ')
        m_export.export_class_in_txt_file(file_csv, file_txt, сlass_, litera.upper())
        main()
        exit()
    elif num == 8:
        system("cls")
        m_search.contact_finder(file_csv, fieldnames)
        main()
        exit()
    elif num == 9:
        system("cls")
        print('Укажите ID ученика для внесения изменений')
        print('(Для просмотра ID, воспользуйтесь поиском, п.8)')
        id = input('>  ')
        m_edit.search_id(id, file_csv, fieldnames)
        main()
        exit()
    elif num == 10:
        system("cls")
        print('Укажите ID для удаления ученика')
        print('(Для просмотра ID, воспользуйтесь поиском, п.8)')
        id = input('>  ')
        m_delete.search_id(id, file_csv)
        main()
        exit()
    elif num == 11:
        system("cls")
        print('Укажите файл *.csv, куда перенести базу')
        file_csv_new = input('>  ')
        m_next_year.shcoolchildren_transfer(file_csv, file_csv_new, fieldnames)
        main()
        exit()
    elif num == 12:
        exit()

def main():
    """
    Основное меню с проверкой ввода цифры
    """
    print('Добро пожаловать в список классов! \n Выберите один из пунктов:')
    print('1. Вывести список файлов в папке на экран ')
    print('2. Вывести основной список классов(class.csv) на экран')
    print('3. Импортировать список из csv файла')
    print('4. Импортировать список из txt файла')
    print('5. Ввести данные нового ученика с клавиатуры ')
    print('6. Экспортировать весь список в txt файл')
    print('7. Экспортировать определенный класс в txt файл')
    print('8. Поиск')
    print('9. Внести изменения')
    print('10. Удалить ученика')
    print('11. Перевести учеников на след. учебный год')
    print('12. Выход \n')
    num = input('Введите число от 1 до 12 > ')
    try:
        num = int(num)
    except:
        system("cls")
        print('Это не число')
        main()
        exit()
    if 1 <= int(num) <= 12:
        choice_method(num)
    else:
        system("cls")
        print('Неправильное число')
        main()
        exit()

main()
