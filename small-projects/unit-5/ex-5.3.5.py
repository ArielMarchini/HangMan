def distance(num1, num2, num3):
    is_difference_of_1 = (abs(num1 - num2) == 1 or abs(num1 - num3)) == 1
    is_difference_of_at_least_2 = ((abs(num2 - num1) >= 2) or (abs(num2 - num3) >= 2) or (abs(num3 - num1) >= 2))
    if is_difference_of_1 and is_difference_of_at_least_2:
        return True
    return False
