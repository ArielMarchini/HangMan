def format_list(my_list):
    """
    This function get a list of strings of even length, and return a
    string that contains all the elements in even index. In addition, in the end add to the new str ""
    :param my_list:
    :return:
    """
    str = ", ".join(my_list[::2])
    str += ", and " + my_list[-1]
    return str
