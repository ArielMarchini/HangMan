def extend_list_x(list_x, list_y):
    """
    This function adds list_y in the begining of list_x.\
    :param list_x: A list that needs to be extend.
    :type list_x: List
    :param list_y: A list to add in the begining of list_x.
    :type list_y: List
    :return: Return list_x
    :rtype: List
    """
    list_y[len(list_y):] = list_x
    list_x = list_y
    return list_x
