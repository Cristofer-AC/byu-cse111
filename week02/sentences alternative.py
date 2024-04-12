# Cristofer Amachi CSE 111

import random

# I exceeded the requirements by
# adding an extra call in the 'make_sentence' function to
# include two prepositional phrases.

# Optional list for making it automatic in 'main' function
# required_sentences = [
#     [1,'past'],
#     [1,'present'],
#     [1,'future'],
#     [2,'past'],
#     [2,'present'],
#     [2,'future']
# ]

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb.
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == 'past':
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present':
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        else:
            # plural
            words = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]
    else:
        # future
        words = [ "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
       

    # Randomly choose and return a noun.
    word = random.choice(words)
    return word

def get_preposition():
    """Return: a randomly chosen preposition.
    """
    words = [  "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    word = random.choice(words)
    return word
        
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    phrase = f"{preposition} {determiner} {noun}"
    return phrase

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase_1 = get_prepositional_phrase(quantity)
    prepositional_phrase_2 = get_prepositional_phrase(quantity)

    sentence = f"{determiner} {noun} {prepositional_phrase_1} {verb} {prepositional_phrase_2}."
    sentence = sentence.capitalize()

    return sentence

def main():
    """Call your make_sentence function six times
    and print six sentences.
    """

    # Below, a way to make it automatic:

    # for required_items in required_sentences:
    #     quantity = required_items[0]
    #     tense = required_items[1]

    #     # Generates and prints sentence
    #     sentence = make_sentence(quantity, tense)
    #     print(sentence)

    print() # Blank line
    
    sentence = make_sentence(1, 'past')
    print(sentence)
    
    sentence = make_sentence(1, 'present')
    print(sentence)

    sentence = make_sentence(1, 'future')
    print(sentence)

    sentence = make_sentence(2, 'past')
    print(sentence)

    sentence = make_sentence(2, 'present')
    print(sentence)

    sentence = make_sentence(2, 'future')
    print(sentence)

    print() # Blank line

main()