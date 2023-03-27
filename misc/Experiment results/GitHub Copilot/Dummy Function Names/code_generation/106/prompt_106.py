
def foo(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    foo(5) == [1, 2, 6, 24, 15]
    """
    if n == 1:
        return [1]
    else:
        if n % 2 == 0:
            return foo(n - 1) + [n * foo(n - 1)[-1]]
        else:
            return foo(n - 1) + [sum(range(1, n + 1))]
