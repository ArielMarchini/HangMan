def numbers_letters_count(my_str):
    """
    The function accepts as a string parameter.
    The function returns a list where the first elements represent the number of digits in the string,
    and the second elements represent the number of letters in the string, including spaces,
    periods, punctuation marks, and anything other than numbers.
    :param my_str: A string that may contains any kinf oh characters.
    :type my_str: String.
    :return: Returns a list where the first elements represent the number of digits in the string,
    and the second elements represent anything other than numbers.
    :rtype: List.
    """
    count_digits = 0
    count_not_digits = 0
    for char in my_str:
        if char.isdigit():
            count_digits += 1
        else:
            count_not_digits += 1
    return [count_digits, count_not_digits]
