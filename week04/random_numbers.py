import random
def main():
    numbers = []

    words = []

    print(numbers)

    append_random_numbers(numbers)

    print(numbers)

    append_random_numbers(numbers, 3)

    print(numbers)

    append_random_words(words)

def append_random_words(word_list, quantity=1):
    random_word = random.choice(['a','b','c'])

    print(random_word)

def append_random_numbers(numbers_list, quantity=1):
    random_number = random.uniform(1,100)
    random_number = round(random_number, 1)

    count = quantity

    while count > 0:
        numbers_list.append(random_number)
        count -= 1

if __name__ == "__main__":
    main()