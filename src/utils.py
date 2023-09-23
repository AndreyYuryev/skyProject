import json
import os


def get_operations(filename='operations.json', folder='../data'):
    '''
    Прочитать файл с выпиской операций и вернуть список с операциями
    :param filename имя json-файла
    :param folder имя папки в структуре проекта где лежит json
    :return список содержащий операции
    '''
    operation_list = []
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        with open(file=filepath, encoding='utf-8', mode='r') as file:
            operation_list = json.load(file)
        return operation_list


def get_sorted_list(ilist):
    '''
    Вернуть отсортированный по дате лист, поле date
    :param ilist: список операций
    :return: отсортированный по дате список операций, по убыванию
    '''
    sorted_list = []
    sorted_list = sorted(ilist, key=lambda d: d['date'], reverse=True)
    return sorted_list


def get_last_executed(ilist, max_operations=5):
    '''
    Вернуть пять последних по дате операций EXECUTED
    '''
    elist = []
    index = 0
    ilenght = len(ilist)
    elenght = 0
    while index < ilenght and elenght < max_operations:
        if ilist[index]['state'] == 'EXECUTED':
            elist.append(ilist[index])
            elenght += 1
        index += 1
    return elist


def get_formatted_operation(ioperation):
    pass
