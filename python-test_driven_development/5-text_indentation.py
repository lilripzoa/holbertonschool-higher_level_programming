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

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
            if i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        else:
            print(text[i], end="")
