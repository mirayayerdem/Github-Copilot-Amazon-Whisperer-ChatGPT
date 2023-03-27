
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    return (sum(1 for i in range(1, n+1) if is_palindrome(i) and is_even(i)),
            sum(1 for i in range(1, n+1) if is_palindrome(i) and not is_even(i)))


def is_palindrome(n):
    """
    Given a positive integer n, return true if it is a palindrome, and false otherwise.
    """
    return str(n) == str(n)[::-1]


def is_even(n):
    """
    Given a positive integer n, return true if it is even, and false otherwise.
    """
    return n % 2 == 0

    





