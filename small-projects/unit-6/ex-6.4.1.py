def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    This function will check if the letter_guessed should be added to old_letters_guessed.
    :param letter_guessed: A string enterd by the user.
    :type: String
    :param old_letters_guessed: A list that contains all the strings that the user already guessed.
    :return: If the function check_valid_input return True, add letter_guessed to old_letters_guessed after that
    return True. Otherwise, False.
    :rtype: Boolean.
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print("->".join(old_letters_guessed))
        return False

