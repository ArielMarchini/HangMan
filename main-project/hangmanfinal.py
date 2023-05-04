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

def print_hangman(num_of_tries, HANGMAN_PHOTOS):
    """
    This function prints the status.
    :param num_of_tries: The number of times the user failed to guess.
    :type num_of_tries: Int.
    :return: None.
    :rtype: None.
    """
    print(HANGMAN_PHOTOS[num_of_tries + 1])

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

def show_hidden_word(secret_word, old_letters_guessed):
    """
    This function is responsible for showing the player which letters he has already discovered.
    This function doing so by building and returning
    a string that displays the letters from the list old_letters_guessed
    which are in the string of secret words in their appropriate position,
    and the rest of the letters in the string (which the player has not yet guessed) as an underscore.

    :param secret_word:  The string represents the secret word that the player has to guess
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
        print("->".join(sorted(old_letters_guessed)))
        return False

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function will check if the letter_guessed is valid.
    Valid means that the length of the letter_guessed is 1, the letter_guessed contains only alphabetic letters
    and the letter_guessed is never guessed before.
    :param letter_guessed: The letter guessed
    :type letter_guessed: String
    :return: Return true if the parameter is valid and false otherwise.
    :rtype: Boolean
    """
    #Check if the letter is valid.
    if (letter_guessed.isalpha()) and (len(letter_guessed) == 1) and (not letter_guessed.lower() in old_letters_guessed):
        return True
    else:
        return False

def print_home_screen():
    """
    This function prints the the opening screen of the game.
    :return: None.
    :rtype: None.
    """
    print("""
Welcome to the game Hangman! \n
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/\n
""")

def main():
    """
    This is the main function, this function start the game.
    """
    MAX_TRIES = 6 # The max tries the user can guess wrong
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
            """} # The pictures of the hanging man
    old_letter_guessed = []  # The letters the user has guessed so far
    num_of_tries = 0  # The current number of failed attempts
    print_home_screen() # Prints the opening screen of the game
    # We keep asking until we get a valid path
    while True:
        path = input("Please enter the file path: ")
        try:
            with open(path, 'r') as file:
                break
        except FileNotFoundError:
            print("File not found, please try again.")
    index = int(input("Please enter index: "))
    secret_word = choose_word(path, index)[1] # Take a secret word from the file
    # Print the hangman and the hidden word
    print_hangman(0, HANGMAN_PHOTOS)
    print(show_hidden_word(secret_word, old_letter_guessed))
    # Keep asking for guesses until the player wins or loses
    while (num_of_tries < MAX_TRIES) and (not check_win(secret_word, old_letter_guessed)):
        letter = input("Please enter a letter: ")
        trying = try_update_letter_guessed(letter.lower(), old_letter_guessed)
        while not trying:
            letter = input("Please enter your guess: ")
            trying = try_update_letter_guessed(letter.lower(), old_letter_guessed)

        if letter.lower() in secret_word:
            print(show_hidden_word(secret_word, old_letter_guessed))
        else:
            num_of_tries += 1
            print(":(")
            print_hangman(num_of_tries, HANGMAN_PHOTOS)
            print(show_hidden_word(secret_word, old_letter_guessed))

    # Print the result (win/lose)
    if check_win(secret_word, old_letter_guessed):
        print("WIN!")
    else:
        print("LOSE!")

if __name__ == '__main__':
    main()




