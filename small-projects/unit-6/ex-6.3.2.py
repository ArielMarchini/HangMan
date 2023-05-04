def longest(my_list):
    """
    This function finds the longest string inside my_list and returns it.
    :param my_list: List that contains strings.
    :type my_list: List
    :return: Return The longest string inside my_list and returns it.
    :rtype: string.
    """
    my_list = sorted(my_list, key=len)
    return my_list[-1]
