import csv
from datetime import datetime, timedelta

def main():
    try:
        KEY_COLUMN_INDEX = 0
        NAME_COLUMN_INDEX = 1
        AMOUNT_COLUMN_INDEX = 2
        DAY_COLUMN_INDEX = 3

        SKILL_NAME = 'Learning to draw'

        # Date vars
        current_date = datetime.now()
    
        # List and dictionary
        activ_list = read_list('activities.csv')
        summarized_dictionary = summarize_list_into_dictionary(activ_list, KEY_COLUMN_INDEX, AMOUNT_COLUMN_INDEX)

        # Print title
        print(f'\nGoal title: {SKILL_NAME}')

        # Table 1
        print('\nTable of activities and practice hours')

        table_cell_width = 15
        header_list = ['Day #', 'Time (hours)', 'Activity']
        header = create_header(header_list, table_cell_width)
        print(header)

        table = list_to_table(activ_list, table_cell_width, [DAY_COLUMN_INDEX, AMOUNT_COLUMN_INDEX, NAME_COLUMN_INDEX])
        print(table)

        # Table 2
        print('\nTable of total practice hours by activity')

        table_cell_width = 20
        header_list = ['Type of activity', 'Time (hours)']
        header = create_header(header_list, table_cell_width)
        print(header)

        sum_list = dictionart_to_list(summarized_dictionary)

        table = list_to_table(sum_list, table_cell_width, [0, 1])
        print(table)

        # Show expected finish date
        days_list = create_list_of_single_value(activ_list, DAY_COLUMN_INDEX)
        highest_day = calculate_highest_number(days_list)
        finish_date = calculate_finish_date(current_date, highest_day)
        date_output = finish_date.strftime("%B %d, %Y")
        print(f'\nYour expected goal finish date within {highest_day} days is: {date_output}\n')
    
    except FileNotFoundError as file_err:
        print(file_err)
    except TypeError as type_err:
        print(type_err)
    except IndexError as inx_err:
        print(inx_err)  

def dictionart_to_list(dictionary):
    """
    Parameters
        dictionart: each key with only one value
    Return: list
    """

    list = []

    for key, value in dictionary.items():
        list.append([key, str(value)])

    return list


def create_header(header_list, header_width):
    """
    Parameters
        header_list: titles
        header_width: int, amount of spaces
    Return: string in a header format
    """

    header = ''

    header += '\n'

    for item in header_list:
        header += item.center(header_width) + ' ' 
    
    header += '\n'

    for _ in range(len(header_list)):
        header += '_' * header_width + ' '

    header += '\n'

    return header

def list_to_table(content_list, cell_width, order_list):
    """
    Parameters
        content_list: of items
    Return: String in format of table
    """
    table = ''

    for list in content_list:
        for index in order_list:
            to_add = list[index].strip().capitalize()
            table += to_add.center(cell_width) + ' '

        table += '\n'

    return table

def create_list_of_single_value(list, column_index):
    """Return a list of values with a single element from a compound list (lists into a list)
    Parameters
        list: compund_list. Has the format of [[list 1], [list 2], ...]
        column_index: the index of where to find in each list the single value 
            with which you will create a new list.
    Return: a simple list with single elements from the given list.
    """
    list_with_values = []

    for line in list:
        value_to_append = int(line[column_index])
        list_with_values.append(value_to_append)

    return list_with_values

def calculate_highest_number(num_list):
    """
    Parameters
        num_list: a set of integers.
    Return: the single highest integer.
    """
    highest_num = 0

    for number in num_list:
        if number > 0:
            highest_num = number
    
    return highest_num

def calculate_finish_date(start_date, days_to_add):
    """
    Parameters
        start_date: in datetime format.
        days_to_add: as integer.
    Return: the end date calculated with the days elapsed.
    """
    end_date = start_date + timedelta(days=days_to_add)
    
    return end_date

def summarize_list_into_dictionary(list, key_column_index, amount_column_index):
    """
    Add repeated values in a list according to a given key indedx 
    and create a dictionary.
        For example,
        the list [['A', 1], ['A', 2], ['B', 1]]
        and given the key index 0
        the result would be the dictionary {'A': 3, 'B': 1}
    Parameters
        list: a compound list.
        key_column_index
        amount_column_index
    Return: a dictionary with a summary of repeated values in a list.
    """
    dictionary = {}

    for item_list in list:
        key = item_list[key_column_index]
        amount_value = int(item_list[amount_column_index])

        if key in dictionary:
            # Add amount of practice
            dictionary[key] += amount_value
            
        else:
            # Create key of practice
            dictionary[key] = amount_value

    return dictionary

def read_list(filename):
    """
    Parameters
        filename: of a csv file.
    Return: a list of rows of a csv file.
    """
    list = []
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        
        next(reader)
        for row_list in reader:
            list.append(row_list)

    return list

if __name__ == '__main__':
    main()