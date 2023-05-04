def sequence_del(my_str):
    """
    The function accepts a string and deletes the letters appearing in sequence.
    :param my_str: A string that may contains letters appearing in sequence.
    :type my_str: String.
    :return: Returns a string in which only one character
    appears from each sequence of identical characters in the input string.
    :rtype: String.
    """
    list_letters_of_str = list(my_str)
    i = 0
    while i < len(list_letters_of_str) - 1:
        if list_letters_of_str[i] == list_letters_of_str[i + 1]:
            list_letters_of_str.remove(list_letters_of_str[i])
        else:
            i += 1
    return "".join(list_letters_of_str)

