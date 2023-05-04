def are_files_equal(file1, file2):
    """
    This function takes in two file paths as input and checks if the contents of the files are identical.
    :param file1: The path of file1.
    :type file1: String.
    :param file2: The path of file2.
    :type file2: String.
    :return: If the contents of the files are identical, True. Otherwise, False.
    :rtype: Boolean.
    """
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()
