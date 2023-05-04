def last_early(my_str):
    if my_str[len(my_str) - 1].lower() in my_str[:len(my_str) - 1].lower():
        return True
    return False
