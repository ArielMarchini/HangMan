def show_hidden_word(secret_word, old_letters_guessed):
    """
    This function is responsible for showing the player which letters he has already discovered.
    This function doing so by building and returning
    a string that displays the letters from the list old_letters_guessed
    which are in the string of secret words in their appropriate position,
    and the rest of the letters in the string (which the player has not yet guessed) as an underscore.

    :param secret_word:  The string represents the secret word that the player has to guess.
    :type secret_word: String.
    :param old_letters_guessed: The list contains the letters the player has guessed so far.
    :type old_letters_guessed: List.
    :return: Returns a string consisting of letters and underscores
    :rtype: String.
    """
    current_word_status = list(" ".join(secret_word))
    for i in range(0, len(current_word_status), 2):
        if not current_word_status[i] in old_letters_guessed:
            current_word_status[i] = "_"
    return "".join(current_word_status)


