temperature = input("Insert the temperature you would like to convert: ")
temperature_number = float(temperature[:len(temperature) - 1])
if temperature[-1].lower() == 'c':
    print((9 * temperature_number + 32 * 5) / 5)
else:
    print((5 * temperature_number - 160) / 9)