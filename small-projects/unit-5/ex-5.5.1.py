def is_valid_input(letter_guessed):
    """
    This function will check if the parameter is valid.
    Valid means that the length of the parameter is 1 and the parameter contains only alphabetic letters.
    :param letter_guessed: The letter guessed
    :type letter_guessed: String
    :return: Return true if the parameter is valid and false otherwise.
    :rtype: Boolean
    """
    #Check if the letter is valid.
    if letter.isalpha() and len(letter) == 1:
        return True
    else:
        return False

MAX_TRIES = 6
HANGMAN_ASCII_ART = """
Welcome to the game Hangman! \n
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/\n
"""
print(HANGMAN_ASCII_ART)
word_to_guess = input("Enter a word please: ")
print("_ " * len(word_to_guess))
letter = input("Enter a letter please: ").lower()
print("The letter you enterd is: ", letter)
