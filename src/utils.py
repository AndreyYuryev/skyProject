import json
import os


def get_operations(filename='operations.json', folder='data'):
    '''
    Прочитать файл с выпиской операций и вернуть список с операциями
    :param filename имя json-файла
    :param folder имя папки в структуре проекта где лежит json
    :return список содержащий операции
    '''
    operation_list = []
    filepath = os.path.join(filename, folder)
    if os.path.isfile(filepath):
        with open(file=filepath, encoding='utf-8', mode='r') as file:
            operation_list = json.load(file)
        return operation_list
