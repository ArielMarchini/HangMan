str = input("Enter a string please: ")
print(str[:1] + str[1:].replace(str[0], 'e'))