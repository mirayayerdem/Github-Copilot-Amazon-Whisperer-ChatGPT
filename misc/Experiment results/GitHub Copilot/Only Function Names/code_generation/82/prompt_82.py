
def prime_length(string):
    """Returns the number of prime length words in the string string."""
    count = 0
    for word in string.split():
        if is_prime(len(word)):
            count += 1
    return count

def is_prime(n):
    """Returns True if n is prime, and False otherwise."""
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True