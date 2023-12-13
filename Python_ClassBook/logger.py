import datetime

"""
Логер предназначен для фиксации хода выполнения программы. 
Он реализует шесть функций. Согласно которым в отдельный 
файл пишется информация об ошибках, предупреждениях, 
дебагинг, исключениях и общая информация.
"""

def info(string):
    file = open('log.txt', 'w')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'debug: ' + string)
    file.close

def debug(string):
    file = open('log.txt', 'w')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'info: ' + string)
    file.close

def warn(string):
    file = open('log.txt', 'w')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'warn: ' + string)
    file.close

def exception(string):
    file = open('log.txt', 'w')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'debug: ' + string)
    file.close

def error(string):
    file = open('log.txt', 'w')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'error: ' + string)
    file.close    

def critical(string):
    file = open('log.txt', 'w')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'critical: ' + string)
    file.close