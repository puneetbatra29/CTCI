"""
Given two strings, write a method to decide if one is a permutation of the
other
"""


def check_permutation(string1, string2):
    """
    :param string1:
    :param string2:
    :return:
    """
    if len(string1) != len(string2):
        return False
    values = [False for _ in range(128)]
    for char in string1:
        values[ord(char)] = True
    for char in string2:
        if not values[ord(char)]:
            return False
    return True
