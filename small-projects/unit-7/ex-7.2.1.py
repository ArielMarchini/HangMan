def is_greater(my_list, n):
    """
    The function accepts two parameters: a list and a number n.
    The function returns a new list containing all the elements that are greater than the number n.
    :param my_list: A list that contains a numbers.
    :type my_list: List of floats.
    :param n: A number that can be used to filter the elements in the list.
    :type n: Float.
    :return: Returns a new list containing all the elements that are greater than the number n.
    :rtype: List of floats.
    """
    new_list = []
    for number in my_list:
        if number > n:
            new_list.append(number)
    return new_list

