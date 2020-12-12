import re

welcome_text = """
*************************************************************************

Welcome to MadLibs!

Provide creative inputs to build your own story. Enter 'quit' at anytime.

*************************************************************************
"""


def welcome():
    print(welcome_text)


def word_prompt(word_type):
    prompt = f"\nEnter a(n) {word_type}:\n> "
    return prompt
   

def read_template(path: str):
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise


def parse_template(string: str):

    regex = r"{([^}]*)}"
    subst = "{}"

    parts = tuple(re.findall(regex, string))
    stripped = re.sub(regex, subst, string)

    return stripped, parts


def merge(string: str, words: tuple):

    regex = r'{}'
    matches = re.finditer(regex, string)

    for word in words:
        string = re.sub(regex, word, string, 1)
    
    return string


def madlibs():
    
    template = read_template('../assets/template.txt')
    stripped, parts = parse_template(template)

    new_words = []

    for part in parts:
        new_word = input(word_prompt(part))
        if new_word == 'quit':
            quit()
        else:
            new_words.append(new_word)
    
    new = merge(stripped, tuple(new_words))
    print(new)


# Run it
welcome()
madlibs()
