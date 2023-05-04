def shift_left(my_list):
    """
    This function moves every element in the list one step left.
    :param my_list: A list with 3 elements.
    :type my_list: List
    :return: The list, but every elements inside the list moved one step left.
    :rtype: List
    """
    if len(my_list) == 3:
        my_list[0], my_list[1], my_list[2] = my_list[1], my_list[2], my_list[0]
        return my_list
    else:
        print("The list needs to have 3 elements!")
