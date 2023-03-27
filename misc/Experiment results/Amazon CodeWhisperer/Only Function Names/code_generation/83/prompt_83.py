
def starts_one_ends(n):
    '''
    n is a positive integer
    returns True if the number is a palindrome, False otherwise
    '''
    # Your code here
    n = str(n)
    if n[0] == n[-1]:
        return True
    else:
        return False
