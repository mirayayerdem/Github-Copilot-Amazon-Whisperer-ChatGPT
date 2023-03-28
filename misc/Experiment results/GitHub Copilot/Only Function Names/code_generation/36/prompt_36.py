

def fizz_buzz(n: int):

    """Return a string of length n consisting of the numbers 1 through n
    separated by spaces, except that multiples of 3 are replaced by "fizz",
    multiples of 5 are replaced by "buzz", and multiples of both 3 and 5
    are replaced by "fizzbuzz".

    >>> fizz_buzz(1)
    '1'
    >>> fizz_buzz(2)
    '1 2'
    >>> fizz_buzz(3)
    '1 2 fizz'
    >>> fizz_buzz(4)
    '1 2 fizz 4'
    >>> fizz_buzz(5)
    '1 2 fizz 4 buzz'
    >>> fizz_buzz(6)
    '1 2 fizz 4 buzz fizz'
    >>> fizz_buzz(7)
    '1 2 fizz 4 buzz fizz 7'
    >>> fizz_buzz(8)
    '1 2 fizz 4 buzz fizz 7 8'
    >>> fizz_buzz(9)
    '1 2 fizz 4 buzz fizz 7 8 fizz'
    >>> fizz_buzz(10)
    '1 2 fizz 4 buzz fizz 7 8 fizz buzz'
    >>> fizz_buzz(11)
    '1 2 fizz 4 buzz fizz 7 8 fizz buzz 11'
    >>> fizz_buzz(12)
    '1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz'
    >>> fizz_buzz(13)
    '1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13'
    >>> fizz_buzz(14)
    '1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14'
    >>> fizz_buzz(15)
    '1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz'
    >>> fizz_buzz(16)
    '1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16'
    >>> fizz_buzz(17)
    '1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17'
    >>> fizz_buzz(18)
    '1 2 fizz 4 buzz fizz 7 8
    """

    i = 1
    result = ""
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            result += "fizzbuzz"
        elif i % 3 == 0:
            result += "fizz"
        elif i % 5 == 0:
            result += "buzz"
        else:
            result += str(i)

        if i < n:
            result += " "

        i += 1

    return result