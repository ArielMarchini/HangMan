def count_chars(my_str):
    """
    The function accepts a string as a parameter.
    The function returns a dictionary, so that each element in it is a pair consisting of a key:
    a character from the passed string (not including spaces), and an array:
    the number of times the character appears in the string.
    :param my_str: A string to count the characters.
    :type my_str: A string.
    :return: A dictionary with each character and its count.
    :rtype: Dictionary.
    """
    my_str = my_str.replace(" ", "")
    char_count = {}
    for char in my_str:
        if char in char_count:
            char_count[char][0] += 1
        else:
            char_count[char] = [1]
    return char_count