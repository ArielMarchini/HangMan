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
if letter.isalpha() and len(letter) == 1:
    print(letter)
elif not(letter.isalpha()) and not(len(letter) == 1):
    print("E3")
elif not(letter.isalpha()):
    print("E2")
else:
    print("E1")
print("The letter you enterd is: ", letter)