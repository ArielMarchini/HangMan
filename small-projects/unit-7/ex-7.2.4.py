def seven_boom(end_number):
    """
    The function accepts an integer, end_number.
    The function returns a list in the range of numbers 0 to end_number inclusive,
    with certain numbers replaced by the string 'BOOM', if they meet one of the following conditions:
    1. The number is a multiple of the number 7.
    2. The number contains the digit 7.
    :param end_number: A number to count to.
    :type end_number: Int
    :return: List in the range of numbers 0 to end_number inclusive,
    with certain numbers replaced by the string 'BOOM'.
    :rtype: List.
    """
    seven_boom_list = []
    for i in range(end_number + 1):
        if (i % 7 == 0) or ('7' in str(i)):
            seven_boom_list.append("BOOM")
        else:
            seven_boom_list.append(i)
    return seven_boom_list
