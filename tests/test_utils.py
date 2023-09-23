from src.utils import get_operations, get_sorted_list, get_last_executed


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
