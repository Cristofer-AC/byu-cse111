# Cristofer Miguel Amachi Cervantes
# CSE 111

# Exceeded the requirements by:
# Write code to discount the product prices by 10% if today 
# is Tuesday or Wednesday.

import csv
from datetime import datetime

def main():
    try:     
        store_name = 'Inkom Emporium'

        PRODUCT_NUMBER_INDEX = 0
        PRODUCT_NAME_INDEX = 1
        PRODUCT_PRICE_INDEX = 2
        QUANTITY_INDEX = 1

        print(store_name)

        products_dict = read_dictionary('products.csv', PRODUCT_NUMBER_INDEX)

        print()

        total_items = 0
        subtotal = 0
        tax = 0.06
        sales_tax = 0
        total = 0
        thankyou_message = f'Thank you for shopping at the {store_name}.'
        current_date_and_time = datetime.now()
        current_date = f'{current_date_and_time:%a %b %-d %X %Y}'
        weekday = current_date_and_time.weekday()
        discount = 0.10
        offer_day = False

        with open('request.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)

            next(reader)

            for row_list in reader:
                    prod_number = row_list[PRODUCT_NUMBER_INDEX]

                    prod_info_list = products_dict[prod_number]
                    product_quantity = int(row_list[QUANTITY_INDEX])

                    product_name = prod_info_list[PRODUCT_NAME_INDEX]
                    product_price = float(prod_info_list[PRODUCT_PRICE_INDEX])

                    print(f'{product_name}: {product_quantity} @ {product_price}')

                    total_items += int(product_quantity)
                    
                    # Add special offer if today it's Tuesday or Wednesday
                    if weekday == 1 or weekday == 2:
                        offer_day = True

                        subtotal += product_quantity * (product_price - product_price * discount)
                    else:
                        subtotal += product_quantity * product_price

        sales_tax = subtotal * tax
        total = subtotal + sales_tax

        print()
        if offer_day:
            print('Today you have 10% off!')

        print(f'Number of Items: {total_items}')
        print(f'Subtotal: {subtotal:.2f}')
        print(f'Sales Tax: {sales_tax:.2f}')
        print(f'Total: {total:.2f}')
        print()
        print(thankyou_message)  
        print(current_date)

    except FileNotFoundError as file_err:
        print(file_err)
    except PermissionError as perm_err:
        print(type(perm_err).__name__, perm_err)
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

      

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]

                dictionary[key] = row_list
    return dictionary

if __name__ == '__main__':
    main()
