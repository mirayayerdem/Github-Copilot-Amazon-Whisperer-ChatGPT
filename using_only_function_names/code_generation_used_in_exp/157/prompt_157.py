
def right_angle_triangle(a, b, c):
    """
    Checks if the triangle is right angled.
    :param a: Side a.
    :param b: Side b.
    :param c: Side c.
    :return: True if the triangle is right angled, False otherwise.
    """
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False
