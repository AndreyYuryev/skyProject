import utils


def main():
    ''' Основная функция '''
    # считать данные из файла
    operations = utils.get_operations()
    # отсортировать по дате
    sorted_operations = utils.get_sorted_list(operations)
    # взять пять последних записей
    executed_operations = utils.get_last_executed(sorted_operations)
    # вывести записи в нужном формате
    for operation in executed_operations:
        pass


if __name__ == '__main__':
    main()
