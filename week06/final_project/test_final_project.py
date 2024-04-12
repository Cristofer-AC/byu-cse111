import pytest
from datetime import datetime
from final_project import \
    read_list,\
    summarize_list_into_dictionary,\
    create_list_of_single_value,\
    calculate_highest_number,\
    calculate_finish_date,\
    dictionart_to_list,\
    create_header,\
    list_to_table

def test_list_to_table():
    assert list_to_table([['C']], 1, [0]) == 'C \n'
    assert list_to_table([['I']], 1, [0]) == 'I \n'
    assert list_to_table([['T']], 1, [0]) == 'T \n'
    assert list_to_table([['A', 'B']], 1, [0, 1]) == 'A B \n'


def test_create_header():
    assert create_header(['B'], 1) == '\nB \n_ \n'
    assert create_header(['Y'], 1) == '\nY \n_ \n'
    assert create_header(['U'], 1) == '\nU \n_ \n'
    assert create_header(['Pathway', 'Worldwide'], 1) == '\nPathway Worldwide \n_ _ \n'

def test_dictionart_to_list():
    assert dictionart_to_list({'A': '1'}) == [['A', '1']]
    assert dictionart_to_list({'B': '1'}) == [['B', '1']]
    assert dictionart_to_list({'Y': '1'}) == [['Y', '1']]
    assert dictionart_to_list({'U': '1'}) == [['U', '1']]
    assert dictionart_to_list({'Idaho': '1'}) == [['Idaho', '1']]



def test_read_list():
    list = read_list('activities.csv')
    length = len(list)
    exp_len = 6
    assert length == exp_len

    assert read_list('activities.csv')[1] == ['tutorial exercise', ' practice exercised proposed in tutorial video 1', ' 1', ' 2']
    assert read_list('activities.csv')[2] == ['practice by myself', ' practice to draw a chosen subject', ' 2', ' 3']

def test_summarize_list_into_dictionary():
    assert summarize_list_into_dictionary([['A', 1], ['A', 2], ['B', 1]], 0, 1) == {'A': 3, 'B': 1}
    assert summarize_list_into_dictionary([['A', 5], ['A', 12], ['B', 78]], 0, 1) == {'A': 17, 'B': 78}
    assert summarize_list_into_dictionary([['X', 58], ['Y', 87], ['X', 30]], 0, 1) == {'X': 88, 'Y': 87}
    assert summarize_list_into_dictionary([['Z', 12345], ['CIT', 1], ['CIT', 110]], 0, 1) == {'Z': 12345, 'CIT': 111}

def test_create_list_of_single_value():
    DAY_COLUMN_INDEX = 3

    assert create_list_of_single_value([['CIT', '111', 1, 1]], DAY_COLUMN_INDEX) == [1]
    assert create_list_of_single_value([['Introduction', 'to', 1, 6]], DAY_COLUMN_INDEX) == [6]
    assert create_list_of_single_value([['Databases', 'in BYU-Idaho', 2, 8]], DAY_COLUMN_INDEX) == [8]

def test_calculate_highest_number():
    assert calculate_highest_number([0, 3, 2, 2, 1, 3]) == 3
    assert calculate_highest_number([0, 6, 2, 6, 2, 7]) == 7

def test_calculate_finish_date():
    assert calculate_finish_date(datetime(2020, 5, 10), 2) == datetime(2020, 5, 12)
    assert calculate_finish_date(datetime(2024, 4, 8), 7) == datetime(2024, 4, 15)
    assert calculate_finish_date(datetime(2024, 4, 9), 12) == datetime(2024, 4, 21)
    assert calculate_finish_date(datetime(2024, 2, 28), 4) == datetime(2024, 3, 3)
    assert calculate_finish_date(datetime(2024, 4, 30), 5) == datetime(2024, 5, 5)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])