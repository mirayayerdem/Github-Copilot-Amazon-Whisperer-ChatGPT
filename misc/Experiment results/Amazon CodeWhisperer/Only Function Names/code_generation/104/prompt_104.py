
def unique_digits(x):
    """
    x: int or str
    Returns True if all digits of x are unique, and False otherwise.
    """
    # Your code here
    return len(set(str(x))) == len(str(x))

