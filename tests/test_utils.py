from src.utils import (get_operations,
                       get_sorted_list,
                       get_last_executed,
                       get_formatted_operation,
                       hide_account_number,
                       hide_card_number)


def test_file_is_exist():
    assert get_operations('operations.json', 'data') is not None
    assert get_operations('operation.json', 'data') is None


def test_get_sorted_list():
    unsorted_list = [{"id": 1, "date": "2018-06-30T02:08:58.425572"},
                     {"id": 2, "date": "2019-07-03T18:35:29.512364"},
                     {"id": 3, "date": "2019-08-26T10:50:58.294041"}]
    sorted_list = [{"id": 3, "date": "2019-08-26T10:50:58.294041"},
                   {"id": 2, "date": "2019-07-03T18:35:29.512364"},
                   {"id": 1, "date": "2018-06-30T02:08:58.425572"}]
    assert get_sorted_list(unsorted_list) == sorted_list
    assert get_sorted_list([]) == []


def test_last_operations():
    full_list = [{"id": 1, "state": "EXECUTED"},
                 {"id": 2, "state": "EXECUTED"},
                 {"id": 3, "state": "CANCELED"},
                 {"id": 4, "state": "EXECUTED"},
                 {"id": 5, "state": "CANCELED"},
                 {"id": 6, "state": "EXECUTED"},
                 {"id": 7, "state": "EXECUTED"},
                 {"id": 8, "state": "EXECUTED"}]
    last_list = [{"id": 1, "state": "EXECUTED"},
                 {"id": 2, "state": "EXECUTED"},
                 {"id": 4, "state": "EXECUTED"},
                 {"id": 6, "state": "EXECUTED"},
                 {"id": 7, "state": "EXECUTED"}]
    assert get_last_executed(full_list) == last_list
    assert get_last_executed([]) == []


def test_get_formatted_operation():
    operation1 = {"id": 441945886,
                  "state": "EXECUTED",
                  "date": "2019-08-26T10:50:58.294041",
                  "operationAmount": {
                      "amount": "31957.58",
                      "currency": {
                          "name": "руб.",
                          "code": "RUB"
                      }
                  },
                  "description": "Перевод организации",
                  "from": "Maestro 1596837868705199",
                  "to": "Счет 64686473678894779589"}
    formatted_operation1 = ['26.08.2019',
                            'Перевод организации',
                            'Maestro',
                            '1596837868705199',
                            'Счет',
                            '64686473678894779589',
                            '31957.58',
                            'руб.']
    assert get_formatted_operation(operation1) == formatted_operation1
    operation2 = {"id": 895315941,
                  "state": "EXECUTED",
                  "date": "2018-08-19T04:27:37.904916",
                  "operationAmount": {
                      "amount": "56883.54",
                      "currency": {
                          "name": "USD",
                          "code": "USD"
                      }
                  },
                  "description": "Перевод с карты на карту",
                  "from": "Visa Classic 6831982476737658",
                  "to": "Visa Platinum 8990922113665229"}
    formatted_operation2 = ['19.08.2018',
                            'Перевод с карты на карту',
                            'Visa Classic',
                            '6831982476737658',
                            'Visa Platinum',
                            '8990922113665229',
                            '56883.54',
                            'USD']
    assert get_formatted_operation(operation2) == formatted_operation2
    assert get_formatted_operation({}) == []


def test_hide_number():
    assert hide_account_number('64686473678894779589') == '**9589'
    assert hide_account_number('') == ''


def test_hide_card():
    assert hide_card_number('1596837868705199') == '1596 83** **** 5199'
    assert hide_card_number('') == ''
