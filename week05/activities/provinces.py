def main():
    provinces_list = read_compound_list('provinces.txt')

    # Print entire list
    print('Entire list')
    print(provinces_list)
    print()

    # Remove the first element from the list
    provinces_list.pop(0)
    print(provinces_list)
    print()

    # Remove the last element from the list
    provinces_list.pop(-1)
    print(provinces_list)
    print()

    replace_element(provinces_list, 'AB', 'Alberta')
    print(provinces_list)

    count = provinces_list.count('Alberta')
    print(count)

def replace_element(list, which_element, new_element):
    index = 0

    for item in list:
        if item == which_element:
            list[index] = new_element
        index += 1

def read_compound_list(filename):
    compound_list = []

    with open(filename, mode='rt') as csv_file:
        
        for row_list in csv_file:
            row_list = row_list.strip()
            # If the current row is not blank,
            # append it to the compound_list.
            if len(row_list) != 0:
                # Append one row from the CSV
                # file to the compound list.
                compound_list.append(row_list)

    return compound_list

main()