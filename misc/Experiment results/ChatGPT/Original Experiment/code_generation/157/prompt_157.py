def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    # first find the hypotenuse of the triangle
    hypotenuse = max(a, b, c)
    # then find the other two sides of the triangle
    if hypotenuse == a:
        side1 = b
        side2 = c
    elif hypotenuse == b:
        side1 = a
        side2 = c
    else:
        side1 = a
        side2 = b

    # check if the Pythagorean theorem holds true
    if hypotenuse ** 2 == (side1 ** 2) + (side2 ** 2):
        return True
    else:
        return False
