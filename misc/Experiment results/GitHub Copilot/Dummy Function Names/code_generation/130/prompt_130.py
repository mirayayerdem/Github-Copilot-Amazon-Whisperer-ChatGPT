
def foo(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    foo(1) = 3
    foo(n) = 1 + n / 2, if n is even.
    foo(n) =  foo(n - 1) + foo(n - 2) + foo(n + 1), if n is odd.
    For example:
    foo(2) = 1 + (2 / 2) = 2
    foo(4) = 3
    foo(3) = foo(2) + foo(1) + foo(4)
           = 2 + 3 + 3 = 8
    You are given a non-negative integer number n, you have to a return a list of the
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    foo(3) = [1, 3, 2, 8]
    """
       if n == 0:
            return [1]
        elif n == 1:
            return [1, 3]
        elif n == 2:
            return [1, 3, 2]
        else:
            lst = [1, 3, 2]
            for i in range(3, n + 1):
                if i % 2 == 0:
                    lst.append(1 + i / 2)
                else:
                    lst.append(lst[i - 1] + lst[i - 2] + lst[i - 3])
                return lst
