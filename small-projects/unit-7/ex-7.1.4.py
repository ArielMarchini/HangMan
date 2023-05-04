def squared_numbers(start, stop):
    """
    This function receives two numbers, a start and a stop,
     and returns a list containing all the numbers to the power of 2 between these two numbers and including them.
    :param start: Number that hold the beginning of the range.
    :type start: Int
    :param stop: Number that hold the end of the range.
    :type stop: Int
    :return: Returns a list containing all the numbers to the power of 2 between these two numbers and including them.
    :rtype: List of integers.
    """
    list_numbers = []
    while start <= stop:
        list_numbers.append(start ** 2)
        start += 1
    return list_numbers


