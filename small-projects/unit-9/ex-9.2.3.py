def who_is_missing(file_name):
    """
    This function reads a comma-separated list of integers from a file and returns the missing number in the sequence.
    :param file_name: The name of the file to read from.
    :type file_name: String.
    :return: Returns the missing number in the sequence.
    :rtype: Int.
    """
    with open(file_path) as file:
        numbers = file.read().split(",")

    numbers = [int(num) for num in numbers]
    numbers.sort()

    for i in range(1, len(numbers) + 1):
        if numbers[i-1] != i:
            missing_number = i
            break

    with open("found.txt", "w") as found_file:
        found_file.write(str(missing_number))

    return missing_number
