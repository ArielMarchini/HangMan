def mult_tuple(tuple1, tuple2):
    """
    The function accepts two tuples as parameters and returns a tuple containing all pairs that can be created from the
    members of the tuples passed as arguments, including pairs with members in reverse order.

    :param tuple1: The first tuple
    :type tuple1: tuple
    :param tuple2: The second tuple
    :type tuple2: tuple
    :return: A tuple containing all pairs that can be created from the members of the tuples passed as arguments
    :rtype: tuple
    """

    all_pairs = []
    for x in tuple1:
        for y in tuple2:
            all_pairs.append((x, y))
            all_pairs.append((y, x))

    return tuple(all_pairs)
