import json
import os
from datetime import datetime


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


def get_formatted_operation(ioperation:dict):
    '''
    Функция составляет список из выводимых полей для операции
    :param ioperation: словарь с данными операции
    :return: список с полями
    '''
    elist = []
    if ioperation:
        operation_date = ioperation['date']
        idatetime = datetime.fromisoformat(operation_date)
        description = ioperation['description']
        operation_from = ioperation['from'].split()
        operation_to = ioperation['to'].split()
        amount = ioperation['operationAmount']['amount']
        currency = ioperation['operationAmount']['currency']['name']
        # дата
        elist.append(idatetime.strftime("%d.%m.%Y"))
        # описание
        elist.append(description)
        # отправитель
        elist.append(operation_from[0])
        elist.append(operation_from[1])
        # получатель
        elist.append(operation_to[0])
        elist.append(operation_to[1])
        # сумма и валюта
        elist.append(amount)
        elist.append(currency)
    return elist


def hide_account_number(inumber:str):
    enumber = []
    if inumber:
        enumber.append('**')
        sliced_number = slice(16, 20)
        enumber.append(inumber[sliced_number])
    return ''.join(enumber)


def hide_card_number(icard:str):
    ecard = []
    if icard:
        ecard.append(icard[slice(0, 4)])
        ecard.append(''.join([icard[slice(4, 6)], '**']))
        ecard.append('****')
        ecard.append(icard[slice(12, 16)])
    return ' '.join(ecard)