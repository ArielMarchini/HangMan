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
MAX_TRIES = 6
print(HANGMAN_ASCII_ART)
letter = input("Enter letter please: ")
print("The letter you enterd is: ", letter)
