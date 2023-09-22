import json
import os


def get_operations(filename='operations.json',folder='./'):
    ''' Прочитать файл с выпиской операций и вернуть коллекцию '''
    operation_collection = {}
    filepath = os.path.join(filename, folder)
    if os.path.isfile(filepath):
        with open(file=filepath, encoding='utf-8', mode='r') as file:
            operation_collection = json.load(file)
        return operation_collection
