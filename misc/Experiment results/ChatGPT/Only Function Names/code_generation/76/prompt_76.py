
def is_simple_power(x, n):
    if x == 1:
        return True
    elif x < 1 or n < 1:
        return False
    else:
        for i in range(2, int(x ** (1/n)) + 1):
            if x == i ** n:
                return True
        return False
