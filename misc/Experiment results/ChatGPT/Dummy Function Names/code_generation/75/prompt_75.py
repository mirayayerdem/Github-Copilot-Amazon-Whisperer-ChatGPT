
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def foo(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    foo(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 2:
        return False
    prime_factors = []
    for i in range(2, a+1):
        if a % i == 0 and is_prime(i):
            prime_factors.append(i)
    return len(prime_factors) == 3
