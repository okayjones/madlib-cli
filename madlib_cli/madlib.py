import re

welcome_text = """
*******************

Welcome to MadLibs!

*******************
"""


def welcome():
    print(welcome_text)


def read_template(path: str):
    with open(path, 'r') as file:
        return file.read()
    

def parse_template(string: str):

    regex = r"{([a-zA-z]*)}"
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

