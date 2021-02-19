#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    utf = 0
    for element in data:
        element = format(element, "#010b")[-8:]
        if utf != 0:
            utf -= 1
            if not element.startswith("10"):
                return False
        elif element[0] == "1":
            if utf == 1 or utf > 4:
                return false
            utf = len(element.split("0")[0])
            utf -= 1

    if utf == 0:
        return True
    return False
