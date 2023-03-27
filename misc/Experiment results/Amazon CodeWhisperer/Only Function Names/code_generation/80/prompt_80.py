
def is_happy(s):
    if s == "1":
        return True
    else:
        return is_happy(str(sum([int(i) ** 2 for i in s])))