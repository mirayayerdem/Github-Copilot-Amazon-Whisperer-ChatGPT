
def triangle_area(a, b, c):
    """Returns the area of the triangle with sides of length a, b, and c."""
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5