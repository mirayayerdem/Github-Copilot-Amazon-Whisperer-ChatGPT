
def iscube(a):
    if a < 0:
        return False
    elif int(a ** (1/3)) ** 3 == a:
        return True
    else:
        return False
