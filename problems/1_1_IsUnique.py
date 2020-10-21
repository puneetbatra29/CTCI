"""
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""


def is_unique(string):
    """
    :param string:
    """
    # If ASCII character set (128 characters)
    if len(string) > 128:
        return False
    char_set = [False for _ in range(128)]

    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True
