
def fruit_distribution(s,n):
    """
    Calculates the number of fruits in a basket of size s.
    :param s: size of the basket.
    :param n: number of fruits.
    :return: number of fruits in a basket of size s.
    """
    if s == 0:
        return 0
    elif s == 1:
        return n
    else:
        return fruit_distribution(s - 1, n) + fruit_distribution(s - 2, n)
