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
    """

    Prints a text with indentation

    Args:
        text (str): The text to prints.

    Raises:
        TypeError: If `text` isn't string.

    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    text_length = len(text)
    idx = 0
    new_string = ''
    starting = True

    while idx < text_length:
        if text[idx] == ' ' and starting is True:
            idx += 1
            continue

        starting = False

        if text[idx] in '.?:':
            new_string += text[idx]
            new_string += '\n'
            new_string += '\n'
            idx += 1

            while idx < text_length and text[idx] == ' ':
                idx += 1

            continue

        if idx < text_length:
            new_string += text[idx]
            idx += 1

    print(new_string, end='')
