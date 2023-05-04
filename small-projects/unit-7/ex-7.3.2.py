def check_win(secret_word, old_letters_guessed):
    """
    This function is responsible for checking if the player won.
    The player won if all the letters that make up the secret word are included
    in the list of letters that the user guessed.
    :param secret_word:  The string represents the secret word that the player has to guess.
    :type secret_word: String.
    :param old_letters_guessed: The list contains the letters the player has guessed so far.
    :type old_letters_guessed: List.
    :return: Returns True if all the letters that make up the secret word are included
    in the list of letters that the user guessed. Otherwise, the function returns false.
    :rtype: Boolean.
    """
    for letter in secret_word:
        if not letter in old_letters_guessed:
            return False
    return True
