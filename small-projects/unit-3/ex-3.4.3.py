str = input("Please enter a string: ")
print(str[:len(str)//2].lower() + str[len(str)//2:].upper())