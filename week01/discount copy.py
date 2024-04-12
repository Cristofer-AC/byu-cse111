from datetime import datetime

subtotal = float(input('What is the subtotal? '))
discount = 0.10

current_date = datetime.now()
day_of_week = current_date.weekday()

# print(subtotal)
# print(day_of_week)


if subtotal >= 50:
    if day_of_week == 1 or day_of_week == 2:
        discount_amount = subtotal * discount
        print(f"Discount: {discount_amount}")
        subtotal -= discount_amount

sales_tax = 0.06
sales_tax_amount = subtotal * sales_tax

subtotal += sales_tax_amount

print(f"Sales Tax: {sales_tax_amount}")
print(f"Total: {subtotal}")