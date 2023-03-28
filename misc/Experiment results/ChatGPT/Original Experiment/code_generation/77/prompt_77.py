def iscube(a):
    return a == 0 or (a > 0 and int(a ** (1 / 3)) ** 3 == a) or (a < 0 and int(-a ** (1 / 3)) ** 3 == -a)
