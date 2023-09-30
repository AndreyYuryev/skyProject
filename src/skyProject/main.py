import skyProject.utils as utils


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
        formatted_operation = utils.get_formatted_operation(operation)
        hided_acc_from = utils.card_or_account(formatted_operation[2], formatted_operation[3])
        hided_acc_to = utils.card_or_account(formatted_operation[4], formatted_operation[5])
        print(formatted_operation[0], formatted_operation[1])
        if formatted_operation[2] == '':
            print(formatted_operation[4], hided_acc_to)
        else:
            print(formatted_operation[2], hided_acc_from,
                  '->', formatted_operation[4], hided_acc_to)
        print(formatted_operation[6], formatted_operation[7])
        print("")


if __name__ == '__main__':
    main()
