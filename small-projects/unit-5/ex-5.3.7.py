def chocolate_maker(small, big, x):
    SMALL_SIZE = 1
    BIG_SIZE = 5
    max_big_needed = x // BIG_SIZE
    if max_big_needed <= big:
        small_needed = x - (max_big_needed * BIG_SIZE)
    else:
        small_needed = x - (big * BIG_SIZE)
    if small_needed > small:
        return False
    return True
print(chocolate_maker(3, 1, 8))
print(chocolate_maker(3, 1, 9))
print(chocolate_maker(3, 2, 10))
