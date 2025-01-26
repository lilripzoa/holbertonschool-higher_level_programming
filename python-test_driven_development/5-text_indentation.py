#!/usr/bin/python3

"""Module for text_indentation method
text_indentation: prints text with 2 new lines
after each of these characters: ., ? and :
prototype: def text_indentation(text)
raises:
TypeError: if text is not a string
no space at the beginning of the printed lines
text is a string
must use the characters ., ? and :
all characters must be separated by 2 new lines
"""


def text_indentation(text):
    """Prints text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The text to be printed.

    Raises:
        TypeError: if text is not a string
        no space at the beginning of the printed lines
        text is a string
        must use the characters ., ? and :
        all characters must be separated by 2 new lines
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")