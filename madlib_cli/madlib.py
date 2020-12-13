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
    """Prints welcome text for the user.
    """
    print(welcome_text)


def word_prompt(word_type: str):
    """Prompts a user for a specific type of word or phrase (e.g. Adjective, Name)

    Args:
        word_type (str): Type of word of phrase

    Returns:
        (str): User input
    """
    prompt = f"\nEnter a(n) {word_type}:\n> "
    user_input = input(prompt).strip()
    return user_input


def print_result(story: str):
    """Prints story for the user.

    Args:
        story (str): Final story
    """
    print(result_text)
    print(story)


def read_template(path: str):
    """Reads a file and returns the content as a string.

    Args:
        path (str): File path

    Returns:
        [str]: Content of the file
    """
    try:
        with open(path, "r") as file:
            return file.read()
    except FileNotFoundError:
        raise


def parse_template(string: str):
    """Parses text for phrases wihin brackets. Returns text with phrases stripped, and a tuple of the removed phrases.

    Args:
        string (str): Text to parse

    Returns:
        str: Stripped text 
        tuple: Tuple of removed phrases
    """

    regex = r"{([^}]*)}"
    subst = "{}"

    parts = tuple(re.findall(regex, string))
    stripped = re.sub(regex, subst, string)

    return stripped, parts


def merge(string: str, words: tuple):
    """Merges a madlibs template with a tuple of phrases.

    Args:
        string (str): template
        words (tuple): phrases

    Returns:
        [str]: Merged story
    """

    regex = r"{}"
    matches = re.finditer(regex, string)

    for word in words:
        string = re.sub(regex, word, string, 1)

    return string


def save_output(string: str):
    """Saves provided text in a .txt file

    Args:
        string (str): text
    """
    with open(result_path, "w") as file:
        file.write(string)


def start()
    """Runs the MabLibs CLI
    """

    welcome()

    template = read_template(template_path)
    stripped, parts = parse_template(template)
    new_words = []

    for part in parts:
        new_word = word_prompt(part)
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
