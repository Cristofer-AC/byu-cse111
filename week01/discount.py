from datetime import datetime

# STRETCH 2

subtotal = 0

print('\nEnter the price and quantity of products. (Enter "0" for price to continue)')

while True:
    item_price = float(input('Price: '))
    if item_price == 0.0:
        break

    quantity = int(input('Quantity: '))

    subtotal += item_price * quantity

print()
print(f"Subtotal: ${subtotal}")

discount = 0.10

current_date = datetime.now()
day_of_week = current_date.weekday()

if day_of_week == 1 or day_of_week == 2:
    if subtotal >= 50:
        discount_amount = subtotal * discount
        print(f"Discount: ${discount_amount:.0f}")
        subtotal -= discount_amount
    else:
        # STRETCH 1
        difference = 50 - subtotal
        print(f"\nWe have a special offer for you! You just need to purchase the amount of ${difference} to receive a discount of 10%.\n")

sales_tax = 0.06
sales_tax_amount = subtotal * sales_tax

subtotal += sales_tax_amount

print(f"Sales Tax: ${sales_tax_amount:.2f}")
print(f"Total: ${subtotal:.2f}")