
def foo(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    foo(1, 2.5) ➞ 2.5
    foo(1, "2,3") ➞ "2,3"
    foo("5,1", "6") ➞ "6"
    foo("1", 1) ➞ None
    """
    try:
        a = float(a.replace(",", "."))
    except:
        pass
    try:
        b = float(b.replace(",", "."))
    except:
        pass
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None
