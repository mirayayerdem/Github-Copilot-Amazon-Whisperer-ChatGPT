
def even_odd_palindrome(n):
    """Returns a string that describes whether n is even, odd, or a palindrome."""
    if n == int(str(n)[::-1]):
        return 'palindrome'
    elif n % 2 == 0:
        return 'even'
    else:
        return 'odd'