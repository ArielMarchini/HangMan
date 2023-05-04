def inverse_dict(my_dict):
    """
   Returns a new dictionary with a "reverse" mapping of the input dictionary. Each key in the input dictionary
   becomes a value in the returned dictionary, and each value in the input dictionary becomes a key in the returned
   dictionary. If multiple keys in the input dictionary have the same value, the returned dictionary will map the
   value to a list of corresponding keys, sorted in ascending order.

   :param my_dict: The dictionary to invert.
   :type my_dict: dict
   :return: A new dictionary with a "reverse" mapping of the input dictionary.
   :rtype: dict
   """
    inv_dict = {}
    for key, value in my_dict.items():
        if value not in inv_dict:
            inv_dict[value] = [key]
        else:
            inv_dict[value].append(key)
            inv_dict[value].sort()
    return inv_dict
