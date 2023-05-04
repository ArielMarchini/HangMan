HANGMAN_PHOTOS = {
1: """
    x-------x
""",
2:
"""
    x-------x
    |
    |
    |
    |
    |
""",
3:
"""
    x-------x
    |       |
    |       0
    |
    |
    |
""",
4:
"""
    x-------x
    |       |
    |       0
    |       |
    |
    |
""",
5:
"""
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""",
6:
"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""",
7:
"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""}

def print_hangman(num_of_tries):
    """
    This function prints the status.
    :param num_of_tries: The number of times the user failed to guess.
    :type num_of_tries: Int.
    :return: None.
    :rtype: None.
    """
    print(HANGMAN_PHOTOS[num_of_tries + 1])
