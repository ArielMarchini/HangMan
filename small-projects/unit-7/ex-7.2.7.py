def arrow(my_char, max_length):
    """
    This function accepts a single character and a maximum size as parameters,
    and returns a string representing an "arrow" structure built from the input.
    :param my_char: The character that will be print inside the arrow.
    :type my_char: String.
    :param max_length: The maximum length of the arrow, the center.
    :type max_length: Int.
    :return: A string representing arrow structure.
    :rtype: String.
    """
    arrow_string = ""
    for i in range(1, max_length + 1):
        arrow_string += my_char * i + "\n"
    for j in range(max_length - 1, 0, -1):
        arrow_string += my_char * j + "\n"
    return arrow_string
