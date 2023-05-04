def fix_age(age):
    if (13 <= age <=14) or (17 <= age <= 19):
        return 0
    return age

def filter_teens(a = 13, b = 13, c = 13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    return (a + b + c)
