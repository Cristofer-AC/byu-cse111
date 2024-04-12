# Cristofer Amachi
# CSE 111 - Prove
# I exceeded the requirements by asking the user if he or she
# wants to buy the tire with the dimensions given and if so
# I ask for the user's phone number to add to the text file.

import math
from datetime import datetime

print('\nTIRE VOLUME CALCULATOR')
print('\nPlease enter the following:')

width = float(input('Width: '))
aspect_ratio = float(input('Aspect Ratio: '))
diameter = float(input('Diameter: '))
pi = math.pi

volume = pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000

print(f"The aproximate volume is {volume:.2f} liters.")
print()

current_date = datetime.now()

# STRETCH CHALLENGE
buy_answer = input('Would you like to buy a tire with the dimension you entered? (Yes/No) ')

with open('volumes.txt', 'at') as volumes_file:
    print(width, file=volumes_file)
    print(f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=volumes_file)

    if buy_answer.lower() == 'yes':
        phone_number = input('Enter your phone number')
        print(phone_number, file=volumes_file)
