def choose_word(file_path, index):
    """
    This function get a path of a text file and an index position of a word, this function returns a tuple consisting of two elements.
    The first element is the number of different words in the file, not including repeated words.
    The second element is a word in the position received as an argument, which will be used as the secret word for guessing.

    :param file_path: A string representing a path to the text file.
    :type file_path: String.
    :param index: An integer representing the position of a certain word in the file.
    :type index: Int.
    :return: A tuple consisting of two members in the following order: the number of different words in the file,
    and a word in the position received as an argument to the function (index), which will be used as the secret word for guessing.
    :rtype: Tuple.
    """
    with open(file_path, 'r') as file:
        text = file.read().lower()
        words = text.split()
        unique_words = set(words)
        num_unique_words = len(unique_words)
        num_words = len(words)
        word_index = (index - 1) % num_words
        secret_word = words[word_index]
    return num_unique_words, secret_word

# print(choose_word(r"C:\Users\97250\PycharmProjects\check.txt", 15))
