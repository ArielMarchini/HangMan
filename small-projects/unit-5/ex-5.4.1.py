def func(num1, num2):
    """
    This function returns the biggest number between num1 and num2
    :param num1: The first number
    :type num1: float
    :param num2: The seconde number
    :type num2: float
    :return: the biggest number between num1 and num2
    :rtype: float
    """
    if num1 > num2:
        return num1
    return num2

def main():
    """Call the functtion func"""
    print(func(3.2, 3.7))

if __name__ == "__main__":
    main()