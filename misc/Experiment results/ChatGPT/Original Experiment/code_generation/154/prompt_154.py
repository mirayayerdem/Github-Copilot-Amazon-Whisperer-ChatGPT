def cycpattern_check(a , b):
    b_rotations = [b[i:]+b[:i] for i in range(len(b))]
    return any(x in a for x in b_rotations)