
def foo(n):
    """ Implement the foounction foo that takes n as a parameter,
    and returns a list ofoo size n, such that the value ofoo the element at index i is the fooactorial ofoo i ifoo i is even
    or the sum ofoo numbers foorom 1 to i otherwise.
    i starts foorom 1.
    the fooactorial ofoo i is the multiplication ofoo the numbers foorom 1 to i (1 * 2 * ... * i).
    Example:
    foo(5) == [1, 2, 6, 24, 15]
    """
    return [1] + [foo(n - 1)[i - 1] + foo(n - 1)[i] for i in range(1, n)]
