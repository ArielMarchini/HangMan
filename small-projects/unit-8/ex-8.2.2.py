def sort_prices(list_of_tuples):
    """
    The function receives a list of tuples that each have an item and a price and
    returns a list of tuples sorted by the price of the items in them from the largest to the smallest.
    :param list_of_tuples: A list of tuples where each tuple contains an item and a price.
    :type list_of_tuples: List[tuple[str, float]].
    :return: A list of tuples sorted by the price of the items in them from the largest to the smallest.
    :rtype: List[tuple[str, float]].
    """

    def get_price(tuple):
        return tuple[1]

    sorted_tuples = sorted(list_of_tuples, key=get_price, reverse=True)
    return sorted_tuples

products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))
