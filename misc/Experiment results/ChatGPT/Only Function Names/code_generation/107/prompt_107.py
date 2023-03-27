
def even_odd_palindrome(n):
    return str(n) == str(n)[::-1] and (len(str(n)) % 2 == 0)
