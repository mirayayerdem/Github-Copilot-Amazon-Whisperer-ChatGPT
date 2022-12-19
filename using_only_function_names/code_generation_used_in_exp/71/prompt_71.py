
def triangle_area(a, b, c):
    """
    Calculates the area of a triangle.
    :param a: side a of the triangle.
    :param b: side b of the triangle.
    :param c: side c of the triangle.
    :return: area of the triangle.
    """
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
