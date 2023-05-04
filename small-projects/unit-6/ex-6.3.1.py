def are_lists_equal(list1, list2):
    """
    This function check if two lists contain exactly the same elements.
    :param list1: List1.
    :type list1: List
    :param list2: List2.
    :type list2: List
    :return: Return True if two lists contain exactly the same elements, otherwist False.
    :rtype: Boolean.
    """
    if sorted(list1) == sorted(list2):
        return True
    return False
