def sort_anagrams(list_of_strings):
    """
    The function accepts a list of strings as a parameter and returns a list of lists of anagrams,
    where each internal list consists of words that are anagrams of each other.

    :param list_of_strings: The list of strings to sort
    :type list_of_strings: list
    :return: A list of lists of anagrams
    :rtype: list
    """
    anagrams = {}
    for word in list_of_strings:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    result = []
    for key in anagrams:
        result.append(anagrams[key])

    return result

