from src.utils import get_operations


def test_file_is_exist():
    assert get_operations('operations.json', '../data') != None
    assert get_operations('operation.json', 'data') == None
