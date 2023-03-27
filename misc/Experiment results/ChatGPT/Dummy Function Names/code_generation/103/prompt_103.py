
def foo(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    foo(1, 5) => "0b11"
    foo(7, 5) => -1
    foo(10, 20) => "0b1111"
    foo(20, 33) => "0b11010"
    """
    if n > m:
        return -1
    else:
        avg = round((n + m) / 2)
        return bin(avg)
