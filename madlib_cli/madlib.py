import re

template_path = "../assets/template.txt"
result_path = "../assets/result.txt"

welcome_text = """
*************************************************

              Welcome to MadLibs!

Provide creative inputs to build your own story. 

            Enter 'quit' at anytime.

*************************************************
"""

result_text = """
*************************************************

           Thanks for playing MadLibs!
         Find your completed story below.

*************************************************
"""


def welcome():
    print(welcome_text)


def word_prompt(word_type: str):
    prompt = f"\nEnter a(n) {word_type}:\n> "
    return prompt


def print_result(string: str):
    print(result_text)
    print(string)


def read_template(path: str):
    try:
        with open(path, "r") as file:
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

    regex = r"{}"
    matches = re.finditer(regex, string)

    for word in words:
        string = re.sub(regex, word, string, 1)

    return string


def save_output(string: str):
    with open(result_path, "w") as file:
        file.write(string)


def start():

    welcome()

    template = read_template(template_path)
    stripped, parts = parse_template(template)
    new_words = []

    for part in parts:
        new_word = input(word_prompt(part)).strip()
        if new_word.lower() == "quit":
            quit()
        else:
            new_words.append(new_word)

    story = merge(stripped, tuple(new_words))

    print_result(story)

    save_output(story)


# Run it
if __name__ == "__main__":
    start()
